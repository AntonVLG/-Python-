# Сортировка вставками

def sortirovka(lst):
    
    for i in range(len(lst)):
        key = lst[i]
        j = i - 1
        print(lst[j])
        print(key)
        print(j)
        #print(lst)
        while lst[j] > key and j >= 0:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
        print(lst)
    return lst 


l = [43,1,11,2,12,7,234,35,3]

print(sortirovka(l))
