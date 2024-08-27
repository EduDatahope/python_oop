from datetime import datetime
from typing import Callable
from functools import partial

func_GreetingReader = Callable[[],str]


def greet(name:str , greeting_reader:func_GreetingReader) -> str:
    if name == 'edu':
       return 'hola :D'
    return f"{greeting_reader()} : {name}"


def greet_list(names: list[str] , greeting_reader:func_GreetingReader):
    return [greet(name , greeting_reader) for name in names] #aqui va sin parentesis el greeting reader
#por que usas la funcion greet que a su vez esa si invoca a la funcion


def read_greeting() -> str:
    current_time = datetime.now()
    msj = 'Hola , Actual time is ' + str(current_time)
    return msj

def read_name() -> str:
    return input('enter your name: ')

def main():
    greet_fn = partial(greet ,greeting_reader=read_greeting)
    print(greet_fn(read_name()))
    print(greet(read_name(),read_greeting))
    print(greet_list(["maria","juan"] , read_greeting))

if __name__ == "__main__":
    main()

