import qunex as qx

def multipath_purification_deutsch(
    graph,
    mad_paths,
    parameter_name,
    swap_rule=None,
    purification_rule=None
):
    def my_tilde(a1, a2, b1, b2, c1, c2, d1, d2):
        n = (a1 + b1) * (a2 + b2) + (c1 + d1) * (c2 + d2)
        a = (a1 * a2 + b1 * b2) / n
        b = (c2 * d1 + c1 * d2) / n
        c = (c1 * c2 + d1 * d2) / n
        d = (a1 * b2 + a2 * b1) / n
        return a, b, c, d
    if swap_rule is None:
        if parameter_name == "concurrence":
            swap_rule = qx.swapped_concurrence_werner
        elif parameter_name == "fidelity":
            swap_rule = qx.swapped_fidelity_werner
        elif parameter_name == "probability":
            swap_rule = qx.swapped_probability
        else:
            raise ValueError(f"swap_rule must be provided for parameter '{parameter_name}'")
    path_params = []
    for path in mad_paths:
        finder = qx.FindPathParameters(graph, path)
        path_params.append(
            finder.compute(parameter_name=parameter_name, rule=swap_rule)
        )
    if parameter_name == "probability":
        p = 1.0
        for x in path_params:
            p *= x
        return p
    if len(path_params) == 1:
        return path_params[0]
    if parameter_name in ["concurrence", "fidelity"] and purification_rule is None:
        a1 = (path_params[0] + 1) / 2
        a2 = (path_params[1] + 1) / 2
        b1 = c1 = d1 = (1 - a1) / 3
        b2 = c2 = d2 = (1 - a2) / 3
        a, b, c, d = my_tilde(a1, a2, b1, b2, c1, c2, d1, d2)
        for i in range(2, len(path_params)):
            a1, b1, c1, d1 = a, b, c, d
            a2 = (path_params[i] + 1) / 2
            b2 = c2 = d2 = (1 - a2) / 3
            a, b, c, d = my_tilde(a1, a2, b1, b2, c1, c2, d1, d2)
        if parameter_name == "concurrence":
            return 2 * a - 1
        else:
            return a
    if purification_rule is None:
        raise ValueError(
            f"purification_rule must be provided for parameter '{parameter_name}'"
        )
    return purification_rule(path_params)
