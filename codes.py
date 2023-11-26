class Codes:
    def __init__(self):
        self.codes = {0:'НМ',
                      1:'ГЖ',
                      2:'ДТ',
                      3:'КХ',
                      4:'ЧЩ',
                      5:'ПБ',
                      6:'ШЛ',
                      7:'СЗ',
                      8:'ВФ',
                      9:'РЦ'}

    def __len__(self):
        return len(self.codes)
    def __str__(self):
        temp = ""
        for key in self.codes:
            temp += f"{str(key)}: {self.codes[key]}\n"
        return temp[0:-1]
    def values(self):
        return self.codes.values()
    
    #---
    
    def get_value(self, i):
        return self.codes[i]
    def is_correct(self, i, letters):
        return (self.codes[i] == letters)
        
