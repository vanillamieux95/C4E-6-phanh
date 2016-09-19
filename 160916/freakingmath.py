#[self.num1, self.num2, self.sign, self.answer] = generate_quiz()
#check_answer(self.num1, self.num2, self.sign, self.answer, True):

from random import *
def generate_quiz():
    num1 = randint(0, 20)
    num2 = randint(1, 10)
    sign = choice(['+', '-', '*', '/'])
    a = choice([num1+num2, num1-num2, num1*num2, num1/num2])
    answer = a + choice([0,1,2])
#    answer = choice([sign])
    return num1, num2, sign, answer

    def check_answer(num1, num2, sign, answer, user_choice):
        num1 = randint(0, 20)
        num2 = randint(0, 10)
        sign = choice(['+', '-', '*', '/'])
        a = choice([num1+num2, num1-num2, num1*num2, num1/num2])
        answer = a + choice([0,1,2])
    #    user_choice == True and user_choice == False
    #    answer = choice([sign])
        return num1, num2, sign, answer

    #user_choice = True
        if answer == choice([num1+num2, num1-num2, num1*num2, num1/num2]):
            if user_choice == True:
                return True
            elif user_choice == False:
                return False
            else:
                print ("None")

        elif answer != choice([num1+num2, num1-num2, num1*num2, num1/num2]):
            if user_choice == True:
                return False
            elif user_choice == False:
                return True
            else:
                print ("None")

        else:
            print ("None")
