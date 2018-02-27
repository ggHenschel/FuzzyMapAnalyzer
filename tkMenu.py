import tkinter as tk
from tkinter import filedialog,messagebox,scrolledtext
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

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        file = tk.Menu(self.menu)

        #self.grid_configure(columnspan=3,rowspan=3)

        #Comandos de Load,Export
        file.add_command(label="Load Process Graph",command=self.loadProcessGraph)
        file.add_command(label="Load Event Logs",command=self.loadEventLogs)
        file.add_command(label="Load Attribute Logs", command=self.loadAttrPath)
        file.add_command(label="Quit Programn",command=self.exit_p)

        self.menu.add_cascade(label="File",menu=file)

        operations = tk.Menu(self.menu)

        #Comandos de Algoritimo do Analisador
        operations.add_command(label="Rodar Algoritmo de Concatenação",command=self.runFullProcess)

        self.menu.add_cascade(label="Operações",menu=operations)

        tk.Label(text='Processo Minerado:').grid(row=0,column=0)
        tk.Label(text='Log de Eventos:').grid(row=1,column=0)
        tk.Label(text='Log de Atributos:').grid(row=2,column=0)

        self.Grafl = tk.Label(self.root, text="None")
        self.Eventl = tk.Label(self.root, text="None")
        self.Attrl = tk.Label(self.root, text="None")

        self.Grafl.grid(row=0, column=1)
        self.Eventl.grid(row=1, column=1)
        self.Attrl.grid(row=2, column=1)

        self.TextBox = scrolledtext.ScrolledText(self.root)

        self.TextBox.grid(row=3,column=0,columnspan=3,rowspan=4)

        tk.Button(text="Export Text",command=self.export_text).grid(row=8,column=2)

    def loadProcessGraph(self):
        file = filedialog.askopenfile()
        path = file.name
        file.close()
        self.graph_path = path
        if self.An is None:
            self.An = analyser.Analiser(path)
        else:
            self.An.reloadGraph(path)
        self.Grafl.configure(text=path.split('/')[-1])
        text = "Process Map loaded: "+path+"\n\n"
        self.TextBox.insert("end",text)
        self.root.update_idletasks()

    def loadEventLogs(self):
        if self.An is None:
            messagebox.showerror(title="Error",message="No Process Loaded")
        else:
            file = filedialog.askopenfile()
            path = file.name
            file.close()
            self.log_path = path
            self.An.replay(path)
            self.Eventtxt = path
            self.Eventl.configure(text=path.split('/')[-1])
            text = "Event Log loaded: " + path + "\n\n"
            self.TextBox.insert("end", text)
            self.root.update_idletasks()

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
            self.Attrtxt = path
            self.Attrl.configure(text=path.split('/')[-1])
            text = "Attribute Log loaded: " + path + "\n\n"
            self.TextBox.insert("end", text)
            self.root.update_idletasks()

    def runFullProcess(self):
        if self.An is None:
            messagebox.showerror(title="Error",message="No Process Loaded")
        elif self.log_path is None:
            messagebox.showerror(title="Error",message="No Event Log Loaded")
        elif self.attr_path is None:
            messagebox.showerror(title="Error", message="No Attribute Log Loaded")
        else:
            file = filedialog.asksaveasfile(mode='w')
            if file is not None:
                r = self.An.Class_Assistant(self.log_path, self.attr_path,save_path=file)
                text = "Arquivos Salvos em: "+r
                self.TextBox.insert("end",text)

    def exportReplayResults(self):
        if self.An is None:
            messagebox.showerror(title="Error", message="No Process Loaded")
        elif self.log_path is None:
            messagebox.showerror(title="Error", message="No Event Log Loaded")
        else:
            ttt = messagebox.askyesno(title="Use Default Path?", message="Use Default Path?")
            print(ttt)
            if ttt == True:
                self.An.case_report(self.log_path)
            else:
                file = filedialog.asksaveasfile()
                self.An.case_report(self.log_path,arquivo=file)

    def export_text(self):
        file = filedialog.askopenfile()
        file.write(self.TextBox.get(1.0,"end"))
        file.close()


    def exit_p(self):
        self.quit()

    def run(self):
        self.root.mainloop()

class GUIFactory:
    def create(self):
        self.root = tk.Tk()
        self.root.geometry("720x480")
        return GUI(self.root)
