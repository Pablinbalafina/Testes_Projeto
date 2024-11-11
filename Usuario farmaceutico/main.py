from view.farmaceutico_view import ViewFarmaceutico
import customtkinter as ctk

def main():
    # Inicializando a janela principal
    view = ViewFarmaceutico()  
    view.criar_interface_farmaceutico()
    view.janela.mainloop()    
    

if __name__ == "__main__":
    main()