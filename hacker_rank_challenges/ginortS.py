# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
up = []
low = []
num = []
for el in s:
    if(el.isupper()):
        up.append(el)
    elif(el.islower()):
        low.append(el)
    elif(el.isdigit):
        num.append(el)
up = sorted(up)
low = sorted(low)
num = sorted(num)
upS = ''
for el in up:
    upS += el
lowS = ''
for el in low:
    lowS += el
numOdd = ''
numEven = ''
for el in num:
    if(int(el)%2==0):
        numEven += el
    elif(int(el)%2==1):
        numOdd += el
print(lowS+upS+numOdd+numEven)
