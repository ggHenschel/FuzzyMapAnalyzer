import sys
import import_adjacency
import import_eventLog
import path_analisys
import replay
import networkx as nx


class Analiser:

    def __init__(self,path):
        if path.endswith(".csv"):
            self.Graph = import_adjacency.import_adj(path)
        elif path.endswith(".xml"):
            self.Graph = import_adjacency.import_full_graph(path)
        elif path=="":
            print("No Graph Loaded")
        else:
            print("EXTENSION ERROR, GRAPH COULD NOT BE LOADED")
        self.replay_results = None

    def reloadGraph(self,path):
        if path.endswith(".csv"):
            self.Graph = import_adjacency.import_adj(path)
        elif path.endswith(".xml"):
            self.Graph = import_adjacency.import_full_graph(path)

    def meanTime(self,start,end):
        return path_analisys.TempoMedioEntreGoldStd(self.Graph,start,end)

    def replay(self,eventlogpath):
        log = import_eventLog.import_eventlog(eventlogpath)
        self.replay_results = replay.replay_log(log,self.Graph)

    def findCicles(self):
        print("Processo Pode Demorar Alguns Minutos")
        ciclos = path_analisys.FindCyles(self.Graph)
        return ciclos

    def case_report(self,log):
        if self.replay_results is None:
            self.replay(log)
        r = replay.export_replay_results(self.replay_results)
        s = replay.rebuild_event_log(log,self.replay_results)
        return (r, s)

    def Class_Assistant(self,log,file,save_path=None):
        if self.replay_results is None:
            self.replay(log)
        return replay.Rebuild_Atributes_Log(file,self.replay_results,save_path=save_path)


    def Degree_Centrality(self):
        return nx.degree_centrality(self.Graph)

    def In_Degree_Centrality(self):
        return nx.in_degree_centrality(self.Graph)

    def Out_Degree_Centrality(self):
        return nx.out_degree_centrality(self.Graph)

    def Closeness_Centrality(self):
        return nx.closeness_centrality(self.Graph)

    def Betweenness_Centrality(self):
        return nx.betweenness_centrality(self.Graph)
