import analyser
import textMenu
from kivy.app import App
from kivy.uix.widget import Widget

class SimpleGuiMenu(Widget):

    An = analyser.Analiser("")
    Graph_Loaded = False

    def LoadGraph(self):
        self.graph_path = self.f_path.text
        self.An.reloadGraph(self.graph_path)
        self.Graph_Loaded = True

    def LoadLog(self):
        self.NLine()
        if self.Graph_Loaded:
            self.log_path = self.f_dados.text
            if self.log_path == "":
                self.print_in_output("Empty Log Path")
            else:
                self.An.replay(self.log_path)
        else:
            self.print_in_output("Graph Not Loaded")

    def LogReport(self):
        self.NLine()
        if self.Graph_Loaded:
            self.LoadLog()
            (r, s) = self.An.case_report(self.log_path)
            self.print_in_output("Eventos salvos em: " + r + " e " + s)
        else:
            self.print_in_output("Graph Not Loaded")

    def LoadAttr(self):
        self.NLine()
        if self.Graph_Loaded:
            self.Attr_Log= self.f_attr.text
            r = self.An.Class_Assistant(self.log_path,self.Attr_Log)
            self.print_in_output("Log de Atributos armazenado no arquivo: "+ r)
        else:
            self.print_in_output("Graph Not Loaded")

    def print_in_output(self,text):
        self.f_text_output.text += "\n"+text

    def Centralidades(self):
        self.NLine()
        self.print_in_output("Calculando Centraliades")
        try:
            nodes_d = self.An.Degree_Centrality()
            self.print_in_output("Evento\t\t\tGrau:")
            for item in nodes_d:
                self.print_in_output(str(item)+"\t|\t"+str(nodes_d[item]))
        except:
            self.print_in_output("Erro ao Achar Centralidade")

    def In_Degree_Centrality(self):
        self.NLine()
        self.print_in_output("Calculando Centraliades")
        try:
            nodes_d = self.An.In_Degree_Centrality()
            self.print_in_output("Evento\t\t\tGrau de Entrada:")
            for item in nodes_d:
                self.print_in_output(str(item)+"\t|\t"+str(nodes_d[item]))
        except:
            self.print_in_output("Erro ao Achar Grau de entrada")

    def Out_Degree_Centrality(self):
        self.NLine()
        self.print_in_output("Calculando Centraliades")
        try:
            nodes_d = self.An.Out_Degree_Centrality()
            self.print_in_output("Evento\t\t\tGrau de Saida:")
            for item in nodes_d:
                self.print_in_output(str(item)+"\t|\t"+str(nodes_d[item]))
        except:
            self.print_in_output("Erro ao Achar Grau de Saida")

    def Betweeness_Centrality(self):
        self.NLine()
        self.print_in_output("Calculando Centraliades")
        try:
            nodes_d = self.An.Betweenness_Centrality()
            self.print_in_output("Evento\t\t\tGrau de Intermediação:")
            for item in nodes_d:
                self.print_in_output(str(item)+"\t|\t"+str(nodes_d[item]))
        except:
            self.print_in_output("Erro ao Achar Grau de Intermediação")

    def FindCicles(self):
        self.NLine()
        self.print_in_output("Calculando Ciclos")
        try:
            nodes_d = self.An.findCicles()
            self.print_in_output("Ciclos Determinados:")
            for item in nodes_d:
                self.print_in_output(str(item))
        except:
            self.print_in_output("Erro ao Achar Ciclos")

    def FindGoldPath(self):
        self.NLine()
        self.print_in_output("Calculando Caminho Ouro")
        try:
            start = self.f_start_input.text
            finish = self.f_end_input.text
            string = self.An.meanTime(start, finish)
            self.print_in_output(string)
        except:
            self.print_in_output("Erro ao Achar Caminho Ouro")

    def NLine(self):
        self.print_in_output("\n")

class SimpleGuiMenuApp(App):
    def build(self):
        return SimpleGuiMenu()
