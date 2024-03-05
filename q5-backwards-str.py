       

'''
Author: Raphael Pereira
data: 04/03/2024
Entrada: Uma string qualquer
Saida: Uma string invertida
Descrição: Inverter uma string como entrada ou pré-definida.

'''
input_str = 'any random string'

def backwards_string(text_input):
    str_helper = ''
    for c in text_input:
        print(str_helper)
        str_helper = c + str_helper  
    return str_helper
    
print("backwards -->", backwards_string(input_str))
