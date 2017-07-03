import networkx as nx
import datetime

def TempoMedioEntreGoldStd(Graph,start,end):
    path = nx.shortest_path(Graph,source=start,target=end,weight="meanTime");

    edges = []

    for i in range(0,len(path)-1):
        edges.append(Graph.get_edge_data(path[i],path[i+1]))

    sum = 0

    for edge in edges:
        sum += edge["meanTime"]

    Resultado = "Tempo Médio para Padrão Ouro:\n\tTempo Médio = "+str(datetime.timedelta(milliseconds=sum))+"\n\n\tCaminho:"

    for i in range(0,len(path)-1):
        Resultado += str(path[i])+" -> "

    Resultado += path[-1]

    return Resultado

def FindCyles(Graph):
    return nx.recursive_simple_cycles(Graph)