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
            # ToDo
            # вспомнить, почему я не переписал рабочую версию кода на VStudio
            # хз короче
            # разобраться, как работают переменные в методах функций
            # что-то еще... дописать эту функциюч
            # сделать первый коммит этого кода
            # и заккометить код на плюсах
            while (not self.codes.is_correct(rand_number, temp_letters)):
                temp_letters = ''
                print('Incorrect answer! Try again')
                temp_letters = input('Input letters for digit ' + str(rand_number) + ': ')
                temp_letters = temp_letters.upper()
            print('Right!')
            size -= 1
        return 0
            
a = App()
a.remember_letters()