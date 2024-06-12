import time
from random import randint
import os

def log(ft):

    def wrapper(*args, **kwargs):
        # get the user from the environment variable
        user = os.getenv('USER', 'unknown')

        start = time.time()
        
        # Execute the ft
        res = ft(*args, **kwargs)
        
        end = time.time()
        
        # execution time in milliseconds (hence * 1000)
        exec_time = (end - start) * 1000
        
        # format the log message by using each decorator's name, replace the _ by a space and use title() method on it
        log_msg = f"({user})Running: {ft.__name__.replace('_', ' ').title():<20} [ exec-time = {exec_time:.3f} ms ]\n"
        
        # Write the log msg to the log file
        with open('machine.log', 'a') as log_file:
            log_file.write(log_msg)
        
        return res
    
    return wrapper


class CoffeeMachine():

    water_level = 100
    

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."


    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
