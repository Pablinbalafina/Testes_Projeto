import re
from datetime import datetime

def validar_string(valor, campo):
    if not isinstance(valor, str) or not valor.strip():
        return False, f"O campo {campo} deve ser preenchido com texto."
    return True, ""

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False, "O CPF deve conter 11 dígitos numéricos."
    return True, ""

def validar_telefone(telefone):
    telefone = ''.join(filter(str.isdigit, telefone))
    if len(telefone) < 10 or len(telefone) > 11:
        return False, "O telefone deve ter 10 ou 11 dígitos numéricos."
    return True, ""

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(padrao, email):
        return False, "O e-mail informado é inválido."
    return True, ""

def validar_campos_preenchidos(**campos):
    for campo, valor in campos.items():
        if not valor:
            return False, f"O campo {campo} é obrigatório."
    return True, ""

def validar_data(data, campo):
    try:
        # Tenta converter o valor para um objeto de data
        datetime.strptime(data, "%Y-%m-%d")  # Formato esperado: YYYY-MM-DD
    except ValueError:
        # Se ocorrer um erro, a data não é válida
        return False, f"O campo {campo} deve conter uma data válida no formato YYYY-MM-DD."
    
    return True, ""  # Se a conversão for bem-sucedida, retorna True