def shout(text): 
    return text.upper() 

def whisper(text): 
    return text.lower() 

def greet(msj:str , func): 
    # storing the function in a variable 
    greeting = func(msj) 
    print(greeting)

greet('hola eduardo',shout) 
greet('muy bien',whisper) 

print('--------- t1 ---------------')

def mi_first_decorator(msj:str , func):
    def inner1():
        print(msj)
        return (func(msj))    
    return inner1

test_decorator = mi_first_decorator('HOLA edu',whisper)
test_decorator() #aqui solo veremos el print del mensaje por que es el print de la ejecucion

print('--------- t2 ---------------')

test_decorator = mi_first_decorator('HOLA edu',shout)
msj = test_decorator()
print(msj) # aqui vemos como el decorator se aplico y se devolvio como funcion un resultado que podremos
#guardar en una variable


