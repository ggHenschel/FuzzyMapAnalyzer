import tkinter as tk
from tkinter import filedialog,messagebox
import analyser


class GUI(tk.Frame):

    An = None
    graph_path = None
    log_path = None
    attr_path = None

    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.root = master
        self.init_window()

    def init_window(self):
        self.root.title="Analise de Processos"

        self.pack(fill='both',expand=1)

        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file = tk.Menu(menu)

        #Comandos de Load,Export
        file.add_command(label="Load Process Graph",command=self.loadProcessGraph)
        file.add_command(label="Load Event Logs",command=self.loadEventLogs)
        file.add_command(label="Load Event Logs", command=self.loadAttrPath)
        file.add_command(label="Quit Programn",command=self.exit)

        menu.add_cascade(label="File",menu=file)

        operations = tk.Menu(menu)

        #Comandos de Algoritimo do Analisador
        operations.add_command(label="Rodar Algoritmo de Concatenação",command=self.runFullProcess)

        menu.add_cascade(label="Operações",menu=operations)

    def loadProcessGraph(self):
        file = filedialog.askopenfile()
        path = file.name
        file.close()
        self.graph_path = path
        self.An = analyser.Analiser(path)

    def loadEventLogs(self):
        if self.An is None:
            messagebox.showerror(title="Error",message="No Process Loaded")
        else:
            file = filedialog.askopenfile()
            path = file.name
            file.close()
            self.log_path = path
            self.An.replay(path)

    def loadAttrPath(self):
        if self.An is None:
            messagebox.showerror(title="Error",message="No Process Loaded")
        elif self.log_path is None:
            messagebox.showerror(title="Error",message="No Event Log Loaded")
        else:
            file = filedialog.askopenfile()
            path = file.name
            file.close()
            self.attr_path = path


    def runFullProcess(self):
        if self.An is None:
            messagebox.showerror(title="Error",message="No Process Loaded")
        elif self.log_path is None:
            messagebox.showerror(title="Error",message="No Event Log Loaded")
        elif self.attr_path is None:
            messagebox.showerror(title="Error", message="No Attribute Log Loaded")
        else:
            ttt = messagebox.askyesno(title="Use Default Path?",message="Use Default Path?")
            print(ttt)
            if ttt == True:
                self.An.Class_Assistant(self.log_path,self.attr_path)
            else:
                file = filedialog.asksaveasfile()
                self.An.Class_Assistant(self.log_path, self.attr_path,save_path=file)

    def exit(self):
        exit(9)

    def run(self):
        self.root.mainloop()

class GUIFactory:
    def create(self):
        self.root = tk.Tk()
        self.root.geometry("400x300")
        return GUI(self.root)