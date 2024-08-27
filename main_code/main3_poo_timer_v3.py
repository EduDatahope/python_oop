from datetime import datetime

def greet(name:str , greeting_intro:str) -> str:
    return f"{greeting_intro} : {name}"

def greet_list(names: list[str] , greeting_intro: str):
    return [greet(name , greeting_intro) for name in names]

def read_greeting() -> str:
    current_time = datetime.now()
    msj = 'Hola , Actual time is ' + str(current_time)
    return msj

def read_name() -> str:
    return input('enter your name: ')

def main():
    print(greet(read_name(),read_greeting()))
    print(greet_list(["maria","juan"] , read_greeting()))

if __name__ == "__main__":
    main()

