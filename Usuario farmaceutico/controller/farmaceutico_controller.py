from model.farmaceutico_model import Medicamentos, get_session
from validacoes.validacao import (validar_campos_preenchidos,validar_string, validar_data)
from tkinter import messagebox


class FarmaceuticoController:
    def __init__(self):
        self.model = Medicamentos()
        self.session = get_session()
        
        
    def ver_medicamentos(self):
        return self.session.query(Medicamentos).all()
    
    def adicionar_medicamento(self, medicamento):
        self.model.session.add(medicamento)
        self.model.session.commit()
    
    
    def adicionar_medicamentos(self, nome, principio_ativo, forma_farmaceutica, validade):
        
        campos_preenchidos, msg = validar_campos_preenchidos(
            nome=nome, principio_ativo=principio_ativo, forma_farmaceutica=forma_farmaceutica, validade=validade
        )
        if not campos_preenchidos:
            self.mostrar_erro("Erro de Validação", msg)
            return
        
        validacoes =  [
            validar_string(nome, "Nome"),
            validar_string(principio_ativo, "Princípio ativo"),
            validar_string(forma_farmaceutica< "Forma farmaceutica"),
            validar_data(validade, "Validade")
        ]
        
        for validacao, msg in validacoes:
            if not validacao:
                self.mostrar_erro("Erro de validação", msg)
                return
            
        novo_medicamento = Medicamentos(nome, principio_ativo, forma_farmaceutica, validade)
        self.adicionar_medicamento(novo_medicamento)
        self.mostrar_mensagem("Medicamento inserido com sucesso")
        
            
            
            
    def mostrar_mensagem(self, titulo, mensagem):
            messagebox.showinfo(titulo, mensagem)

    def mostrar_erro(self, titulo, mensagem):
        messagebox.showerror(titulo, mensagem)

    def confirmar_acao(self, titulo, mensagem):
        return messagebox.askyesno(titulo, mensagem)
            
            
            
            