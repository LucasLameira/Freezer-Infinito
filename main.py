"""
Equipe 7 BRASA Hacks 2020

Freezer Infinito
"""

from qrcode_generator import QRcode
import pandas as pd
import os.path

try:
    # Python2
    import Tkinter as tk
    from Tkinter import ttk
except ImportError:
    # Python3
    import tkinter as tk
    from tkinter import ttk

class Main:
    
    def __init__(self):
        self.city = ""
    
    def interface(self):
        self.window = tk.Tk()
        self.window.title("Freezer Infinito")
        
        # add labels
        self.label_1 = tk.Label(self.window, text="ASs cadastradas:")
        self.label_1.grid(column=0, row=2)
        
        self.label_2 = tk.Label(self.window, text="Cadastro de nova AS:")
        self.label_2.grid(column=2, row=0)
        
        self.label_3 = tk.Label(self.window, text="Nome")
        self.label_3.grid(column=3, row=0)
        
        self.label_4 = tk.Label(self.window, text="Rua")
        self.label_4.grid(column=3, row=1)

        self.label_5 = tk.Label(self.window, text="n")
        self.label_5.grid(column=5, row=1)
                
        self.label_6 = tk.Label(self.window, text="Bairro")
        self.label_6.grid(column=5, row=0)
        
        self.label_7 = tk.Label(self.window, text="Cep")
        self.label_7.grid(column=3, row=2)
        
        self.label_8 = tk.Label(self.window, text="Escolha a cidade")
        self.label_8.grid(column=0, row=0)
        
        # function to save data into file
        def save():
            file = open("data_base_AS/"+self.city+".csv", "w")
            file_list = self.listbox.get(0,'end')
            if file_list != ():
                for item in file_list:
                    i = 0
                    for name in item:
                        file.writelines(str(name))
                        if i == 4:
                            file.writelines('\n')
                        else:
                            file.writelines(",")
                        i += 1
            file.close()         
        
        # function called when combobox changes
        def callbackFunc(event):
            save()
            self.listbox.delete(0, 'end')
            self.city = self.combo.get()
            self.var_5.set("Ordenar ASs")
            if os.path.isfile("data_base_AS/"+self.city+".csv"):
                if os.stat("data_base_AS/"+self.city+".csv").st_size != 0:
                    self.df = pd.read_csv("data_base_AS/"+self.city+".csv", header = None)
                    self.textList = self.df.values.tolist()
                    for name in self.textList:
                        self.listbox.insert(tk.END, name)
            
        # add combobox
        self.combo = ttk.Combobox(self.window, values=["Curitiba", "Belo Horizonte", "Recife", "Rio de Janeiro", "São Paulo Capital", "São Paulo Interior", "São Paulo Litoral"])
        self.combo.grid(column=0, row=1)
        self.combo.bind("<<ComboboxSelected>>", callbackFunc)

        # function called when listbox is selected        
        def onSelect(event):
            selection = self.listbox.curselection()
            self.var_1.set("")
            self.var_2.set("")
            self.var_4.set("Apagar As")
            if selection==():
                self.var_3.set("")
            else:
                name = self.listbox.get(selection)
                self.var_3.set(name)
            
        # add listbox
        self.listbox = tk.Listbox(self.window, width=30, height=15)
        self.listbox.grid(column=0, row=3, rowspan=10)
        self.listbox.bind('<<ListboxSelect>>', onSelect)
        
        # add scrollbars to listbox 
        self.scrollbar_y = tk.Scrollbar(command=self.listbox.yview, orient=tk.VERTICAL)
        self.scrollbar_y.grid(column=1, row=3, rowspan=10, sticky='ns')
        
        self.scrollbar_x = tk.Scrollbar(command=self.listbox.xview, orient=tk.HORIZONTAL)
        self.scrollbar_x.grid(column=0, row=13, sticky='we') 
        self.listbox.config(xscrollcommand=self.scrollbar_x.set, yscrollcommand=self.scrollbar_y.set)
        
        # add inputs
        self.entry_1 = tk.Entry()
        self.entry_1.grid(column=4, row=0)
        
        self.entry_2 = tk.Entry()
        self.entry_2.grid(column=4, row=1)
        
        self.entry_3 = tk.Entry()
        self.entry_3.grid(column=6, row=1)
        
        self.entry_4 = tk.Entry()
        self.entry_4.grid(column=6, row=0)
        
        self.entry_5 = tk.Entry()
        self.entry_5.grid(column=4, row=2)

        # add label variables
        self.var_1 = tk.DoubleVar()
        self.var_1.set("")
        self.label_9 = tk.Label(self.window, textvar = self.var_1)
        self.label_9.grid(column=2, row=10, columnspan=3)
        
        self.var_2 = tk.DoubleVar()
        self.var_2.set("")
        self.label_10 = tk.Label(self.window, textvar = self.var_2)
        self.label_10.grid(column=6, row=3, columnspan=2)

        self.var_3 = tk.DoubleVar()
        self.var_3.set("")
        self.label_11 = tk.Label(self.window, textvar = self.var_3)
        self.label_11.grid(column=1, row=8, columnspan=6)        

        self.var_4 = tk.DoubleVar()
        self.var_4.set("Apagar AS")
        self.label_12 = tk.Label(self.window, textvar = self.var_4)
        self.label_12.grid(column=0, row=15)  

        self.var_5 = tk.DoubleVar()
        self.var_5.set("Ordenar ASs")
        self.label_13 = tk.Label(self.window, textvar = self.var_5)
        self.label_13.grid(column=2, row=15)  
        
        # function to generate QRcode
        def generate_qrcode(): 
            selection = self.listbox.curselection()
            if selection==():
                self.var_1.set("Selecione uma AS") 
            else:
                data = self.listbox.get(selection)
                print(data)
                QRcode.qr_generator(data)
                self.var_1.set("QRcode gerado com sucesso")
                
        self.gen_qrcode = tk.Button(self.window, text="Gerar QRcode", command=generate_qrcode)
        self.gen_qrcode.grid(column=3, row=9)
        
        # Delete listbox selection
        def delete():
            selection = self.listbox.curselection()
            if selection==():
                self.var_4.set("Selecione uma AS")
            else:
                self.listbox.delete(selection)
                self.var_4.set("AS deletada")
            save()
        
        self.delete_name = tk.Button(self.window, text="Deletar", command=delete)
        self.delete_name.grid(column=0, row=14)        
        
        # add entry inputs to listbox
        def add():
            last_index = self.listbox.size()
            new_name = str(self.entry_1.get())
            new_street = str(self.entry_2.get())
            new_number = str(self.entry_3.get())
            new_nei = str(self.entry_4.get())
            new_zip = str(self.entry_5.get())
            if new_name == "" or new_street == "" or new_number == "" or new_nei == "" or new_zip == "" :
                self.var_2.set("Insira os dados")
            elif self.city == "":
                self.var_2.set("Selecione uma cidade")              
            else:
                self.listbox.insert(last_index, (new_name, new_street, new_number, new_nei, new_zip))
                self.entry_1.delete(0, 'end')
                self.entry_2.delete(0, 'end')
                self.entry_3.delete(0, 'end')
                self.entry_4.delete(0, 'end')
                self.entry_5.delete(0, 'end')
                save()
                self.var_2.set("AS cadastrada")

        self.add = tk.Button(self.window, text="Adicionar", command=add)
        self.add.grid(column=6, row=2)   
                
        # sort listbox
        def sort():
            if self.city=="":
                self.var_5.set("Selecione uma cidade")
            else:                
                temp_list = list(self.listbox.get(0, tk.END))
                temp_list.sort()
                self.listbox.delete(0, tk.END)
                for item in temp_list:
                    self.listbox.insert(tk.END, item)
                save()

        self.sort_list = tk.Button(self.window, text="Ordenar", command=sort)
        self.sort_list.grid(column=2, row=14)  
     
        self.window.mainloop()
        
main = Main()
main.interface()

