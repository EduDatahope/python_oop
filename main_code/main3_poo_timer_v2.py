from datetime import datetime

class Greeting:
    def __init__(self , greeting_intro: str) -> None:
        self.greeting_intro = greeting_intro   
    
    def greet(self , name:str) ->   str:
        return f"{self.greeting_intro}, {name}"
    
    def greet_list(self, names: list[str]) -> list[str]:
        greetings_list: list[str] = []

        for name in names:
            greetings_list.append(self.greet(name))
        return greetings_list
    
def main() -> None:
     current_time = datetime.now()

     if current_time.hour < 12:
            my_greeting = ('Good Morning '+ str(current_time))
     elif 12 <= current_time.hour <18:
            my_greeting = ('Good Afterno ' + str(current_time))
     else:
            my_greeting = ('Good Evening ' + str(current_time))

     name=input('Enter your name:')

     greeting = Greeting(my_greeting)
     msj = greeting.greet(name)   
     print(msj) 

if __name__ == "__main__":
    main()