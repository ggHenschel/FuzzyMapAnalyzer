class TextMenu:
    def __init__(self,Analiser,log="",AtributeLog=""):
        self.An = Analiser
        self.log = log
        self.AtributeLog = AtributeLog

    def run(self):
        while True:
            option = input("Opções:\n0 - Exit Program\n1 - Import Event Log\n2 - Find Cycles\n3 - Find meanTime Between Process\n4 - Replay Event Log\n5 - Grau de Todos os Nós\n6 - Grau de Saida\n7 - Grau de Entrada\n8 - Centralidade\n9 - Intermediação\n10 - Exportar Novo Log de Attributos Com Nova Classe")
            if int(option)==0:
                exit(0)
            elif int(option)==1:
                self.log = input("Digite o caminho até o log: ")
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
