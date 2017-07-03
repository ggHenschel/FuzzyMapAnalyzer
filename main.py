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
        else:
            print("EXTENSION ERROR, GRAPH COULD NOT BE LOADED")
        self.replay_results = None

    def reloadGraph(self,path):
        self.Graph = import_adjacency.import_adj(path)

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

    def Class_Assistant(self,log,file):
        if self.replay_results is None:
            self.replay(log)
        return replay.Rebuild_Atributes_Log(file,self.replay_results)


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

class Menu:


    def __init__(self,Analiser,log="",AtributeLog=""):
        self.An = Analiser
        self.log = log
        self.AtributeLog =AtributeLog

    def Run(self):
        while True:
            option = input("Opções:\n0 - Exit Program\n1 - Import Event Log\n2 - Find Cycles\n3 - Find meanTime Between Process\n4 - Replay Event Log\n5 - Grau de Todos os Nós\n6 - Grau de Saida\n7 - Grau de Entrada\n8 - Centralidade\n9 - Intermediação\n10 - Exportar Novo Log de Attributos Com Nova Classe")
            if int(option)==0:
                quit()
            elif int(option)==1:
                self.log == input("Digite o caminho até o log: ")
            elif int(option)==2:
                print(self.An.findCicles())
            elif int(option)==3:
                start = input("Digite processo de Inicio: ")
                finish = input("Digite processo Fim: ")
                print(self.An.meanTime(start,finish))
            elif int(option)==4:
                if self.log == "":
                    print("Não há log de Eventos carregados")
                else:
                    self.An.replay(self.log)
                    (r ,s) = self.An.case_report(self.log)
                    print("Eventos salvos em: "+r+" e "+s)
            elif int(option)==5:
                nodes_d = self.An.Degree_Centrality()
                print("Evento\t\t\tGrau:")
                for item in nodes_d:
                    print(item,"\t|\t",nodes_d[item])
            elif int(option)==6:
                nodes_d = self.An.In_Degree_Centrality()
                print("Evento\t\t\tGrau de Entrada:")
                for item in nodes_d:
                    print(item,"\t|\t",nodes_d[item])
            elif int(option)==7:
                nodes_d = self.An.Out_Degree_Centrality()
                print("Evento\t\t\tGrau de Saida:")
                for item in nodes_d:
                    print(item,"| ",nodes_d[item])
            elif int(option)==8:
                nodes_d = self.An.Closeness_Centrality()
                print("Evento\t\t\tGrau de Proximidade:")
                for item in nodes_d:
                    print(item,"\t|\t",nodes_d[item])
            elif int(option)==9:
                nodes_d = self.An.Betweenness_Centrality()
                print("Evento\t\t\tGrau de Centralidade:")
                for item in nodes_d:
                    print(item,"\t|\t",nodes_d[item])
            elif int(option)==10:
                if self.AtributeLog=="":
                    self.AtributeLog = input("Digite o caminho até o log: ")
                r = self.An.Class_Assistant(self.log, self.AtributeLog)
                print("Log de Atributos armazenado no arquivo: ", r)
            else:
                print("Opção invalida")

if len(sys.argv)==1:
    print("É necessario a entrada de pelo menos 1 argumento:\n Argumento 1: Grafo\n Argumento 2: Report Log\n Argumento 3: Log de Atributos")
    quit()
elif len(sys.argv)==2:
    An = Analiser(sys.argv[1])
    M = Menu(An)
elif len(sys.argv)==3:
    An = Analiser(sys.argv[1])
    log = sys.argv[2]
    M = Menu(An,log)
elif len(sys.argv)==4:
    An = Analiser(sys.argv[1])
    log = sys.argv[2]
    AttLog = sys.argv[3]
    M = Menu(An, log, AttLog)

M.Run()


