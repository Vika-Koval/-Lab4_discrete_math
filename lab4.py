import random

def prime(func):
    def wrapper(*args, **kwargs):
        v = func(*args, **kwargs)
        next(v) 
        return v
    return wrapper

class Vikas_day:
    def __init__(self) -> None:
        self.hour = 8
        self.day_start = self._create_start()
        self.sleep = self._sleep()
        self.study_math_analysis = self._study_math_analysis()
        self.study_discrete_math= self._study_discrete_math()
        self.eat = self._eat()
        self.relax = self._relax()
        self.walk = self._walk()
        self.day_end = self._create_end()
        self._current_state = self.day_start

    def my_day(self):
        print("Hello! Welcome to Vikas's day)\n")
        while self._current_state != self.day_end:
            if self._current_state != self.day_start and self._current_state != self.sleep:
                print(f"Hour - {self.hour}.00:")
            self._current_state.send(self.hour)
        print(f"Hour - {self.hour}:")
        self._current_state.send(self.hour)

    @prime
    def _create_start(self):
        while True:
            hour = yield
            rand = random.random()
            print('ZZZZZZZZZZZ')
            print(f'(Usually, Vika let herself sleep till {self.hour})\n')
            if rand > 0.4:
                self._current_state = self.study_math_analysis
            else:
                self._current_state = self.sleep

    @prime
    def _sleep(self):
        while True:
            hour = yield
            self.hour += 3
            print(f'Oh no, it seems like I had not woke up on time again, and it ia already {self.hour}!\n')
            self._current_state = self.eat
    
    @prime
    def _study_math_analysis(self):
        while True:
            hour = yield
            if self.hour==8:
                print('Today Vika woke up on time, and decided to learn several theorems from math analysis.\n')
            else:
                print("I did not manage to deal with my math analysis homework today, so time to do it!\n")
            self._current_state = self.eat
            self.hour += 3

    @prime
    def _eat(self):
        while True:
            hour = yield
            rand = random.random()
            print("I am so hungry. Let's eat something.\n")
            if self.hour==15:
                self._current_state = self.relax
            elif rand<0.4:
                self._current_state = self.study_math_analysis
            elif 0.4<rand<0.8:
                self._current_state = self.study_discrete_math
            else:
                self._current_state = self.relax
            self.hour += 1
            
    @prime
    def _relax(self):
        while True:
            hour = yield
            rand = random.random()
            print("Now I am too tired, so let's relax a little bit.\n")
            if self.hour==12:
                self._current_state = self.eat
                self.hour += 3
            elif self.hour==16 and rand<0.4:
                self._current_state = self.study_discrete_math
                self.hour += 3
            elif self.hour==16 and rand>0.4:
                self._current_state = self.walk
                self.hour += 3
            else:
                self._current_state = self.day_end
                self.hour += 2

    @prime
    def _study_discrete_math(self):
        while True:
            hour = yield
            if self.hour==19:
                print('Oh,unfortunetly,rain become, it seems like no park today(')
                print("I have a lot of gaps in discret math, so let's take it as a chance to study a little bit more.\n")
                self._current_state = self.relax
            else:
                print("Oh, session soon, I do not know number theory at all, let's do some exercises.\n")
                self._current_state = self.eat
            self.hour += 3
            
    @prime
    def _walk(self):
        while True:
            hour = yield
            print("Oh, such nice weather outside, let's walk a little bit.\n")
            self._current_state = self.relax
            self.hour += 3
            
    @prime
    def _create_end(self):
        while True:
            hour = yield
            self.hour = 8
            print('Vika went to bad.')
            print('ZZZZZZ\n')
            print("Vikas's day has ended.\n")

            
if __name__ == "__main__":
    day = Vikas_day()
    day.my_day()
