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
            while (not self.codes.is_correct(rand_number, temp_letters, "check_letters")):
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

