import functools
import os
import time
from random import randint
import logging


logging.basicConfig(filename='machine.log', format='%(message)s', level=logging.INFO)


def log(func):

    @functools.wraps(func)
    def function(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start)
        name_function = func.__name__.replace('_', ' ').title()
        logging.info(f"({os.environ['USER']})Running: {name_function:<20}[ exec-time = {elapsed:0.3f} {'s' if elapsed >= 1.0 else 'ms'} ]")
        return result

    return function


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
