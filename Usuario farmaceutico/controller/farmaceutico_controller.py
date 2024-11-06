from model.farmaceutico_model import Medicamentos
from view.farmaceutico_view import ViewFarmaceutico
from validacoes.validacao import (validar_campos_preenchidos,validar_string)

class FarmaceuticoController:
    def __init__(self):
        pass
        
        
    def ver_medicamentos(self):
        return self.session.query(Medicamentos).all()
    
    
    def adicionar_medicamentos(self, nome, principio_ativo, forma_farmaceutica, validade):
        
        campos_preenchidos, msg = validar_campos_preenchidos(
            nome=nome, principio_ativo=principio_ativo, forma_farmaceutica=forma_farmaceutica, validade=validade
        )
        if not campos_preenchidos:
            self.view.mostrar_erro