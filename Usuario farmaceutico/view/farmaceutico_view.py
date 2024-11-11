import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from controller.farmaceutico_controller import FarmaceuticoController

class ViewFarmaceutico():
    def __init__(self):
        self.controller = FarmaceuticoController()
        self.configurar_janela()
    
    def configurar_janela(self):
        self.janela = ctk.CTk()
        self.janela.title("Tela Farmaceutico")
        self.janela.geometry(f"{self.janela.winfo_screenwidth()}x{self.janela.winfo_screenheight()}+0+0")
        self.janela.resizable(True, True)
        self.criar_interface_farmaceutico()

        
    def criar_interface_farmaceutico(self):
        self.frame = ctk.CTkFrame(self.janela, border_width=3, border_color="#00CED1", fg_color="white")
        self.frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.5, relheight=0.7)
        
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure((1, 2, 3), weight=1)
        
        self.titulo_frame = ctk.CTkLabel(self.frame, text="Tela Farmaceutico", font=("Montserrat", 24, "bold"))
        self.titulo_frame.grid(column=0, row=1, columnspan=2, padx=0, pady=0)
        
        self.botao_ver_medicamentos = ctk.CTkButton(self.frame, text="Ver medicamentos", command=self.controller.ver_medicamentos, width=100, height=30)
        self.botao_ver_medicamentos.grid(column=0, row=2, columnspan=2, padx=100 , pady=0, sticky='ew')  # Adicionando o botão à interface
        
        self.botao_adicionar_medicamentos = ctk.CTkButton(self.frame, text="Adicionar medicamentos", command=self.controller.adicionar_medicamento, width=100, height=30)
        self.botao_adicionar_medicamentos.grid(column=0, row=3, columnspan=2, padx=100, pady=0, sticky="ew")
        
        self.botao_mostrar_tabela = ctk.CTkButton(self.frame, text="Mostrar Tabela", command=self.mostrar_tabela)
        self.botao_mostrar_tabela.grid(row=4, column=0, columnspan=2, padx=0, pady=0, sticky='ew')
    
        
        
        
    
    def mostrar_tabela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()
            
        self.janela.withdraw()  # Esconde a janela de login
        self.janela_tabela = ctk.CTkToplevel(self.janela)
        self.janela_tabela.title("Tabela de medicamentos")
        self.janela_tabela.geometry(f"{self.janela.winfo_screenwidth()}x{self.janela.winfo_screenheight()}+0+0")

        self.janela_tabela.grid_columnconfigure(0, weight=1)
        self.janela_tabela.grid_rowconfigure(2, weight=1)

        # Título
        self.label_titulo = ctk.CTkLabel(self.janela, text="Lista de Pacientes", font=("Arial", 24, "bold"))
        self.label_titulo.grid(row=0, column=0, pady=20, sticky="ew")

        # Frame para filtros
        self.frame_filtros = ctk.CTkFrame(self.janela_tabela)
        self.frame_filtros.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.entry_pesquisa = ctk.CTkEntry(self.frame_filtros, placeholder_text="Digite o nome ou CPF", width=250, font=("Arial", 14))
        self.entry_pesquisa.pack(side="left", padx=5, pady=5)

        # Limpa a tabela antes de adicionar novos dados
        colunas = ("Nome", "Principio ativo", "Forma farmaceutica", "Validade")
        self.tabela = ttk.Treeview(self.janela_tabela, columns=colunas, show="headings")
        
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 14, "bold"))
        style.configure("Treeview", font=("Arial", 12))

        for col in colunas:
            self.frame_tabela.heading(col, text=col, anchor="center")
            self.frame_tabela.column(col, anchor="center", width=150)

        self.frame_tabela.column("Nome", width=200)
        self.frame_tabela.column("Email", width=200)
        self.frame_tabela.column("Endereço", width=300)

        self.frame_tabela.tag_configure('evenrow', background='#E8E8E8')
        self.frame_tabela.tag_configure('oddrow', background='#FFFFFF')

        self.frame_tabela.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        # Scrollbars
        scrollbar_y = ttk.Scrollbar(self.janela, orient="vertical", command=self.frame_tabela.yview)
        scrollbar_y.grid(row=2, column=1, sticky="ns")

        scrollbar_x = ttk.Scrollbar(self.janela, orient="horizontal", command=self.frame_tabela.xview)
        scrollbar_x.grid(row=3, column=0, sticky="ew")

        self.frame_tabela.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        # Frame para botões
        self.frame_acoes = ctk.CTkFrame(self.janela_tabela)
        self.frame_acoes.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

        self.botao_voltar = ctk.CTkButton(self.frame_acoes, text="Voltar", font=("Arial", 16, "bold"), width=150, height=40, command=self.exibir_tela_recepcionista)
        self.botao_voltar.pack(side="right", padx=5)


        

    
        
    def mostrar_mensagem(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

    def mostrar_erro(self, titulo, mensagem):
        messagebox.showerror(titulo, mensagem)

    def confirmar_acao(self, titulo, mensagem):
        return messagebox.askyesno(titulo, mensagem)

                
    