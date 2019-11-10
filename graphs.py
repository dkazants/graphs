
nodes = 10
edges = [(1,2),(1,3),(2,3),(3,4),(4,5),(4,6),(5,6),(5,7),(6,7),(7,8),(8,9),(8,10),(9,10)]

class Graphs():

    def __init__(self, edges_lst, nodes_num):
        self.nodes = nodes_num
        self.edges = edges_lst
        self.__graph_dict = self.conv_to_dict(self.nodes, self.edges)

    def conv_to_dict(self, nodes, edges):
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

    def __str__(self):
        a = ""
        for k,v in self.__graph_dict.items():
            a += f"{k} :  {v}\n"
        return(str(a))

    def get_keys(self):
        self.k_lst = []
        for k,v in self.nodes_rm_dic.items():
            self.k_lst.append(k)
        return (self.k_lst)

    def find_all_path(self,start_node,end_node, path=None):
        if path == None:
            path = []
        gr = self.nodes_rm_dic
        path = path + [start_node]
        if start_node == end_node:
            return [path]
        if start_node not in self.nodes_rm_dic:
            return []
        paths = []
        for node in gr[start_node]:
            if node not in path:
                extended_path = self.find_all_path(node,end_node,path)
                for a in extended_path:
                    paths.append(a)
        return(paths)

    def remove_node(self, node_num):
        self.nodes_rm_dic = dict(self.__graph_dict)
        if node_num in self.nodes_rm_dic:
            self.nodes_rm_dic.pop(node_num)

    def chk_if_broken(self,m):
        self.remove_node(m)
        for i in self.get_keys():
            for j in self.get_keys():
                if not self.find_all_path(i,j):
                    return True
                else:
                    continue
        return False

router = Graphs(edges, nodes)
print(router)

affected_nodes = set()
for remove_n in range(nodes):
    if router.chk_if_broken(remove_n):
        affected_nodes.add(remove_n)
        continue
    else:
        continue

print(affected_nodes)
