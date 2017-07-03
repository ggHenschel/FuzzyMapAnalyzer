import networkx as nx
import csv
from subprocess import call
from xml.dom import minidom

def import_adj(origin_path,destination=""):
    file = open(origin_path)
    read = csv.reader(file,delimiter=",")
    rows = []
    Graph = nx.DiGraph()
    for row in read:
        rows.append(row)
    legend = rows[0][1:]
    for item in legend:
        Graph.add_node(item)
    for item in rows[1:]:
        origin = item[0]
        for index in range(1,len(item)):
            if int(item[index]) > 0:
                Graph.add_edge(origin,legend[index-1],meanTime=int(item[index]))
                #print(item[index],legend[index-1])
    if destination != "":
        print("Running Graphviz.\n This Function Takes Time for Large Networks.\n Please Wait a Few Minutes.")
        exit_path = destination+".dot"
        nx.nx_pydot.write_dot(Graph,exit_path)
        call(["dot","-T","png","-O",exit_path])

    return Graph

def import_full_graph(origin_path,destination=""):
    xmldoc = minidom.parse(origin_path)

    nodeslist = xmldoc.getElementsByTagName('Node')
    edgelist = xmldoc.getElementsByTagName('Edge')

    Graph = nx.DiGraph()

    Dict = {-1:-1}

    for node in nodeslist:
        #print(node.attributes['index'].value,str(node.attributes['activity'].value))
        Dict[node.attributes['index'].value] = node.attributes['activity'].value
        Graph.add_node(node.attributes['activity'].value)

    Dict.pop(-1)

    StarNode = xmldoc.getElementsByTagName('StartNode')
    EndNode = xmldoc.getElementsByTagName('EndNode')

    for node in StarNode:
        #print(node.attributes['index'].value,str(node.attributes['activity'].value))
        Dict[node.attributes['index'].value] = "StartNode"
        Graph.add_node("StartNode")

    for node in EndNode:
        #print(node.attributes['index'].value,str(node.attributes['activity'].value))
        Dict[node.attributes['index'].value] = "EndNode"
        Graph.add_node("EndNode")

    for edge in edgelist:
        nodeS = Dict[edge.attributes['sourceIndex'].value]
        nodeT = Dict[edge.attributes['targetIndex'].value]
        minTime = int(edge.getElementsByTagName('Duration')[0].attributes['min'].value)
        meanTime = int(edge.getElementsByTagName('Duration')[0].attributes['mean'].value)
        maxTime = int(edge.getElementsByTagName('Duration')[0].attributes['max'].value)
        Graph.add_edge(nodeS,nodeT,minTime=minTime,maxTime=maxTime,meanTime=meanTime)

    return Graph