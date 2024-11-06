import customtkinter as ctk
from tkinter import messagebox

class ViewFarmaceutico():
    def __init__(self, janela, controller):
        self.janela = janela
        self.controller = controller     
    
    def configurar_janela(self):
        self.janela = ctk.CTk()
        self.janela.title("Tela Farmaceutico")
        self.janela.geometry(f"{self.janela.winfo_screenwidth()}x{self.janela.winfo_screenheight()}+0+0")
        self.janela.resizable(True, True)
        
    def criar_interface_farmaceutico(self):
        if self.frame:
            self.frame.destroy()
        self.frame = ctk.CTkFrame(self.janela, border_width=3, border_color="#00CED1", fg_color="white")
        self.frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.8, relheight=0.8)
        
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure((1, 2, 3), weight=1)
        
        self.botao_ver_medicamentos = ctk.CTkButton(self.frame, text="Ver medicamentos", comand=self.ver_medicamentos)
        
        
    def mostrar_mensagem(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

    def mostrar_erro(self, titulo, mensagem):
        messagebox.showerror(titulo, mensagem)

    def confirmar_acao(self, titulo, mensagem):
        return messagebox.askyesno(titulo, mensagem)

                
           