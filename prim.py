import networkx as nx
import matplotlib.pyplot as plt
class Prim():
    def __init__(self,graph, start):
        self.graph = graph
        self.start = start
        self.Preds = self.init_Preds()
        self.path = []
        self.calculate_way()

    def calculate_way(self):        
        self.path.append(self.start)       
        while (len(self.graph.keys()) > len(self.path)):
            min_vertex_weight = (float("inf"),float("inf"))
            for position in self.path:
                try:
                    weight, vertex = min([(weight, vertex)  
                                        for vertex, weight in self.graph.get(position).iteritems() 
                                        if not(vertex in self.path)]
                                        )
                    if (min_vertex_weight[1] > weight):
                        min_vertex_weight = (vertex,weight)
                        vertex_min_weight = position
                except:
                    pass
            self.path.append(min_vertex_weight[0])
            self.Preds[min_vertex_weight[0]-1] = vertex_min_weight

    def init_Preds(self):
        Preds = []
        for position in range(len(self.graph)):
            Preds.append(None)
        Preds[self.start-1] = self.start
        return Preds
    
    def show_graph(self):
        graph=nx.Graph(self.graph)
        pos=nx.circular_layout(graph)
        nx.draw_networkx_nodes(graph, pos, node_color='r', node_size=500, alpha=0.8)
        nx.draw_networkx_edges(graph,pos,width=1,alpha=0.5)
        nx.draw_networkx_edges(graph,pos,
                        edge_labels={},
                        edgelist=self.get_edgelist(),
                        width=8,alpha=0.5,edge_color='r')
        nx.draw_networkx_edge_labels(graph,pos, self.get_list_weights_edge(),label_pos=0.3)
        labels=self.set_labels()
        nx.draw_networkx_labels(graph,pos,labels,font_size=16)
        plt.title("Arvore Geradora Minima")
        plt.text(0.5, 0.97, "Start: "+str(self.start),
                     horizontalalignment='center',
                     transform=plt.gca().transAxes)
        plt.text(0.5, 0.94, "Vertex: "+str(self.path),
                     horizontalalignment='center',
                     transform=plt.gca().transAxes)
        plt.text(0.5, 0.90, "Pred: "+str(self.Preds),
                    horizontalalignment='center',
                    transform=plt.gca().transAxes)
        plt.axis('off')
        plt.show()
    
    def set_labels(self):
        labels={}
        for position in self.graph.keys():
            labels[position]=position
        return labels
    
    def get_edgelist(self):
        start =  self.start
        list_preds_path = []
        for position in range(len(self.path)):
            neighbor = (position+1,self.Preds[position])
            list_preds_path.append(neighbor)
        return list_preds_path

    def get_list_weights_edge(self):
        list_weights_edge={}
        for position in self.graph.keys():
            for vertex, weight in self.graph.get(position).iteritems():
                if not(list_weights_edge.get((vertex,position))):
                    list_weights_edge[(position,vertex)] = weight
        return list_weights_edge

if __name__ == '__main__':
   print "Exemplo 1 - Graph"
   graph = { 
           1: { 2: 10, 6: 3 },
           2: { 1: 10, 3: 8, 5: 5, 6: 6 },
           3: { 2: 8 , 4: 7 },
           4: { 3: 7 , 5: 6 },
           5: { 4: 6 , 2: 5, 6: 3 },
           6: { 1: 3 , 5: 3, 2: 6 },
           }
   prim = Prim(graph,1)
   print "Path   : %s" %(prim.path)
   print "Preds : %s" %(prim.Preds)
   prim.show_graph() 