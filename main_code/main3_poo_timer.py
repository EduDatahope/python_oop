from datetime import datetime

class Greeting:
    def __init__(self) -> None:
        current_time = datetime.now()
        if current_time.hour < 12:
            self.my_greeting = ('Good Morning '+ str(current_time))
        elif 12 <= current_time.hour <18:
            self.my_greeting = ('Good Afterno ' + str(current_time))
        else:
            self.my_greeting = ('Good Evening ' + str(current_time))
    
    def greet(self , name:str) ->   None:
        print(f"{self.my_greeting}, {name}")
    
    def greet_list(self, names: list[str]) -> None:
        for name in names:
            self.greet(name)
    
def main() -> None:
     name=input('Enter your name:')

     greeting = Greeting()
     greeting.greet(name)   

if __name__ == "__main__":
    main()