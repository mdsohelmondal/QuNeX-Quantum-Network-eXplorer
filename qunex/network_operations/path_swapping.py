def swapped_concurrence_werner(edge_concs_of_path):
    if len(edge_concs_of_path)!=0:
        for i in range(len(edge_concs_of_path)-1):
            c=max(0,(edge_concs_of_path[i]+edge_concs_of_path[i+1]+2*edge_concs_of_path[i]*edge_concs_of_path[i+1]-1)/3)
            edge_concs_of_path[i+1]=c
        return(edge_concs_of_path[-1])
    else:
      return 0

def swapped_fidelity_werner(edge_fids_of_path):
    if len(edge_fids_of_path)!=0:
        for i in range(len(edge_fids_of_path)-1):
            f=max(0,(-edge_fids_of_path[i]-edge_fids_of_path[i+1]+4*edge_fids_of_path[i]*edge_fids_of_path[i+1]+1)/3)
            edge_fids_of_path[i+1]=f
        return(edge_fids_of_path[-1])
    else:
      return 0

def swapped_probability(edge_probs_of_path):
    p = 1.0
    for x in edge_probs_of_path:
        p *= x
    return p