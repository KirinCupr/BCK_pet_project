import time
def remove_from_list(lis, del_element):
    lis.pop(lis.index(del_element))
    
def awesome_print(string, delay = 0.22):
    for i in string:
        print(i, end='')
        time.sleep(delay)
    print()
    