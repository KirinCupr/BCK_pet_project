import random
import codes
import support_funcs

class App:
    def __init__(self):
        self.codes = codes.Codes()
        
    def remember_letters(self):
        size = 10
        digits = [i for i in range(size)]
        
        while(size):
            rand_number = random.randint(0,9) #bla-bla write
            if (not rand_number in digits):
                continue
            support_funcs.remove_from_list(digits, rand_number)
            temp_letters = input('Input letters for digit ' + str(rand_number) + ': ')
            temp_letters = temp_letters.upper()
            
            while (not self.codes.is_correct(rand_number, temp_letters)):
                temp_letters = ''
                print('Incorrect answer! Try again')
                temp_letters = input('Input letters for digit ' + str(rand_number) + ': ')
                temp_letters = temp_letters.upper()
            print('Right!')
            size -= 1
        print('Exercise had completed!')
        return 0
    
    def remember_digits(self):
        size = 10
        digits = [i for i in range(size)]
        
        while(size):
            rand_number = random.randint(0,9) #bla-bla write
            if (not rand_number in digits):
                continue
            support_funcs.remove_from_list(digits, rand_number)
            temp_digit = int(input('Input digit for letters ' + str(self.codes.get_value(rand_number)) + ': '))

            while (rand_number != temp_digit):
                temp_digit = -1
                print('Incorrect answer! Try again')
                temp_digit = int(input('Input digit for letters ' + str(self.codes.get_value(rand_number)) + ': '))
            print('Right!')
            size -= 1
        print('Exercise had completed!')
        return 0

    def practice_letters(self):
        size = int(input('Enter count of number: '))
        temp_values = [size]
        
        while(size):
            rand_number = random.randint(10,99) #bla-bla write
            if (rand_number in temp_values):
                continue
            temp_values.append(rand_number)
            temp_letters = input('Input letters for number ' + str(rand_number) + ': ')
            temp_letters = temp_letters.upper()
            
            while (not (self.codes.is_correct(rand_number//10, temp_letters[:2]) and
                        self.codes.is_correct(rand_number%10, temp_letters[-2:]))):
                temp_letters = ''
                print('Incorrect answer! Try again')
                temp_letters = input('Input letters for digit ' + str(rand_number) + ': ')
                temp_letters = temp_letters.upper()
            print('Right!')
            size -= 1
        print('Exercise had completed!')
        return 0
    
    def practice_digits(self):
        size = int(input('Enter count of number: '))
        temp_values = [size]
        
        while(size):
            rand_number = random.randint(10,99) #bla-bla write
            if (rand_number in temp_values):
                continue
            temp_values.append(rand_number)
            temp_number = int(input('Input digits for ' + self.codes.get_value(rand_number//10) + self.codes.get_value(rand_number%10) + ': '))
            
            while (not (self.codes.is_correct(rand_number//10, self.codes.get_value(temp_number//10)) and
                        self.codes.is_correct(rand_number%10, self.codes.get_value(temp_number%10)))):
                temp_number = -1
                print('Incorrect answer! Try again')
                temp_number = int(input('Input digits for ' + self.codes.get_value(rand_number//10) + self.codes.get_value(rand_number%10) + ': '))
            print('Right!')
            size -= 1
        print('Exercise had completed!')
        return 0
    
    def run(self):
        titles = {
            1: "remember_letters",
            2: "remember_digits",
            3: "practice_letters",
            4: "practice_digits",
                }

        support_funcs.awesome_print('Greetings, my Dude!')
        support_funcs.awesome_print('Choose wisely what You want!')
        choise = 1
        while (1 <= choise < 5):
            for i, v in titles.items():
                print(str(i) + '. ' + v)
            
            support_funcs.awesome_print("Enter 0 or another digit to exit")
            support_funcs.awesome_print('What is Your choise, my Dude?')
            choise = int(input('>> '))
            if (choise == 1):
                self.remember_letters()
            elif (choise == 2):
                self.remember_digits()
            elif (choise == 3):
                self.practice_letters()
            elif (choise == 4):
                self.practice_digits()
            else:
                support_funcs.awesome_print('Goodbye, my Dude!')
        return 0