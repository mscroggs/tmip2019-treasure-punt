#1702
#7
#14
#1998

def ben(n):
    if sum(int(i) for i in str(n)) == 10 and "7" in str(n):
        return True
    if sum(int(i) for i in str(n)) != 10 and "7" not in str(n):
        return False

def katie(n):
    if str(n)[0] == "7" and "1" in str(n):
        return True
    if str(n)[0] != "7" and "1" not in str(n):
        return False

def kevin(n):
    if n%14==0 and "2" in str(n):
        return True
    if n%14!=0 and "2" not in str(n):
        return False

def sam(n):
    if "37" in str(n) and "2" in str(n) and "0" in str(n):
        return True
    if "37" not in str(n) and "2" not in str(n) and "0" not in str(n):
        return False


from itertools import product
for i in product([True,False],repeat=4):
    options = []
    for n in range(1000,10000):
        if ben(n) == i[0] and katie(n) == i[1] and kevin(n) == i[2] and sam(n) == i[3]:
            options.append(n)
    print(i,len(options),options)
