import math 
print("YEAR","POPULATION",'INCREASING',sep = " | ")
population = 80000
increasing = 0 
for i in range (1,101):
    First = 80000
    if i < 10 :
        print(i,end= '    | ')
    elif i >= 10 and i < 100 :
        print(i,end = '   | ')
    else :
        print(i,end = '  | ')
    if population < 100000 :
        print(population ,end =  '      | ')
    else :
        print(population ,end =  '     | ')
    print('+',increasing)
        
    Last = population
    population  = math.floor(population *  1.02)
    increasing = (population - Last)
    

