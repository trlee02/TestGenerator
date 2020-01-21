import random
from random import randint
import os

msg = "Hello"

print(msg)

def remove_test(file_name):
    if os.path.exists("{}".format(file_name)):
        os.remove("{}".format(file_name))
        print("File '{}' was deleted".format(file_name))
    else:
        print("This file does not exist")


class Test(object):

    answers = None

    def __init__(self, length, biggest, name):
        self.length = length
        self.biggest = biggest
        self.answers = [0]*length
        self.test = open("{}.txt".format(name), "w+")

    def generate(self):
        #questions = [[0] * 3] * self.length
        devices = "+-*/"

        for i in range(self.length):
            device = random.choice(devices)

            if device is '/':
                while True:
                    first, second = randint(2, self.biggest), randint(2, self.biggest - 1)
                    if first % second == 0 and first != second:
                        break
            else:
                first, second = randint(1, self.biggest), randint(1, self.biggest)

            #questions[i][0], questions[i][1], questions[i][2] = first, device, second
            if device is '+':
                self.answers[i] = first + second
            elif device is '-':
                self.answers[i] = first - second
            elif device is '*':
                self.answers[i] = first * second
            else:
                self.answers[i] = first / second

            self.test.write("{}. {} {} {}\n".format(i + 1, first, device, second))

        self.test.write("\nEND OF TEST\n===========\nScroll for answers.")
        for i in range(100):
            self.test.write("\n")

        print("Test made.")

    def generate_ans(self):
        i = 1
        self.test.write("ANSWERS:\n=========\n")
        for answer in self.answers:
            self.test.write("{}. {}\n".format(i, answer))
            i += 1

        print("Answers made.")
    
    def close_test(self):
        self.test.close()

t = Test(10,10,"Tristan")
t.generate()
t.generate_ans()
t.close_test()
remove_test("Tristan.txt")
