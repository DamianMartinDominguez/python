# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.

#Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales!
#Escribe un programa que use:

#un bucle for;
#el concepto de ejecución condicional (if-elif-else).
#la sentencia continue.
#Tu programa debe:

#pedir al usuario que ingrese una palabra.
#utiliza user_word = user_word.upper() para convertir la palabra ingresada 
#por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena
#y el método upper() muy pronto, no te preocupes
#utiliza la ejecución condicional y la instrucción continue para "devorar" 
#las siguientes vocales A, E, I, O, U de la palabra ingresada.
#imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada

user_word =input("ingrese una palabra: ")

user_word=user_word.upper()

for letter in user_word:
    # Completa el cuerpo del bucle for.
    if letter =="A" or letter =="E" or letter =="I" or letter =="O" or letter =="U":
        continue
    else:
        print(letter)
#con comando elif

user_word =input("ingrese una palabra: ")

user_word=user_word.upper()

for letter in user_word:
    # Completa el cuerpo del bucle for.
    if letter =="A":
        continue
    elif letter =="E":
        continue
    elif letter =="I":
        continue
    elif letter =="O":
        continue
    elif letter =="U":
        continue
    else:
        print(letter)
        
        
#version con variable de la palabra sin vocales


word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.

user_word =input("ingrese una palabra: ")

user_word=user_word.upper()

for letter in user_word:
    # Completa el cuerpo del bucle for.
    if letter =="A":
        continue
    elif letter =="E":
        continue
    elif letter =="I":
        continue
    elif letter =="O":
        continue
    elif letter =="U":
        continue
    else:
        word_without_vowels = word_without_vowels+letter
print(word_without_vowels)
