def collatz(num, i):
    if i==500: return -1
    if num == 1:return i
    
    i += 1

    if num % 2 == 0:
        return collatz(num/2, i) 
    else:
        return collatz((num*3)+1, i)
    
def solution(num):
    return collatz(num, 0)
