import re

def validate_numero_telefone(phone_number):
   
   padrao = r"[(]\d{2}[)] \d{5}-\d{4}"
   telefone = phone_number
   

   if re.match(padrao, telefone):
    
    print("Número de telefone válido.")
    
   else:
    print("Número de telefone inválido.")
       
phone_number = input()  

validate_numero_telefone(phone_number)
