
nodes = 10
edges = [(1,2),(1,3),(2,3),(3,4),(4,5),(4,6),(5,6),(5,7),(6,7),(7,8),(8,9),(8,10),(9,10)]

class Graphs():

    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def __str__(self):
        a = ""
        for k,v in self.graph_dict.items():
            a += f"{k} :  {v}\n"
        return(str(a))

    def get_keys(self):
        k_lst = []
        for k,v in self.graph_dict.items():
            k_lst.append(k)
        return (k_lst)

    def find_all_path(self,start_node,end_node, path=None):
        if path == None:
            path = []
        gr = self.graph_dict
        path = path + [start_node]
        if start_node == end_node:
            return [path]
        if start_node not in self.graph_dict:
            return []
        paths = []
        for node in gr[start_node]:
            if node not in path:
                extended_path = self.find_all_path(node,end_node,path)
                for a in extended_path:
                    paths.append(a)
        return(paths)

    def remove_node(self, node_num):
        nodes_tmp1 = dict(self.graph_dict)
        if node_num in nodes_tmp1:
            nodes_tmp1.pop(node_num)
        return(nodes_tmp1)


def conv_to_dict(nodes, edges):
    graph_dict = {}
    for node in range(nodes):
        final_edges = list()
        for edge in edges:
            if node in edge:
                for n in edge:
                    if n != node:
                        final_edges.append(n)
                        graph_dict[node] = final_edges
    return graph_dict



graph = conv_to_dict(nodes,edges)
#for k,v in conv_to_dict(nodes, edges).items():
#    print (k," : ", v)

router = Graphs(graph)
print(router)

#print (router.find_all_path(0,6))
affected_nodes = set()
for remove_n in range(nodes):
    r_node = router.remove_node(remove_n)
    rm_router = Graphs(r_node)
#    print(f"Removed node {remove_n} and new graph is " ,r_node)
    list_of_keys = rm_router.get_keys()
    for i in list_of_keys:
        for j in list_of_keys:
            if not rm_router.find_all_path(i,j):
                 affected_nodes.add(remove_n)
                 break
            else:
                continue
            break

print(affected_nodes)
