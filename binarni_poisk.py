# Бинарный поиск


l = [12, 21, 32, 37, 45, 51, 68]
n = 45

def poisk(lst, n):
    first = 0
    last = len(lst) - 1
    index = - 1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lst[mid] == n:
            index = mid
        else:
            if n < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index



			

rez = (poisk(l,n))
if rez==-1:
	print('Нет такого числа')
else:
	print('Индекс искомого числа в списке = ', rez)
	