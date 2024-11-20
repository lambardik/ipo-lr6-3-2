import random  
mat = [-3, -5, -2, -12, 0, 15, 4, 7, 2]   
m = random.randint(4,8)  
n = random.randint(4,8)   
matrix = [[random.choice(mat) for j in range(n)] for i in range(m) ]   
for m in matrix:  
    for n in m:    
        print(f"{n:3}", end =" ")    
    print()    
sum = 0
for m in matrix:  
    for n in m:    
        if n % 3 == 0: 
            sum += n  
print("Summa :",sum)