# Сортировка пузырьком

from random import randint

def sort_puz(lst):
    for i in range(0,len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                temp = lst[j+1]
                lst[j+1] = lst[j]
                lst[j] = temp  
    return lst


l = [l*randint(1,100) for l in range(1,11)]
print('Сортируем данный список ',l)
print('Результат ', sort_puz(l))