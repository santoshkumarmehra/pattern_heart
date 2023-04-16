# num = int(input("enter number: "))
num=8
msg = 'sant'
l = len(msg)
n = num//2
for i in range(n):
    print(' '*(n-i-1) + "* "*(i+1), end='')
    if num%2==0:
        for j in range(2*(n-i-1)):
            print(' ', end='')
    else:
        for j in range(2*(n-i-1)+1):
            print(' ', end='')
    print("* "*(i+1))
if num%2==0:
    if l%2==0:
        print("* "*((num-l)//2) + ' '.join(msg) + " *"*((num-l)//2))
    else:
        print("* "*((num-l)//2) + ' '.join(msg) + " *"*((num-l)//2)+1)
else:
    if l%2==0:
        print("* "*((num-l)//2) + ' '.join(msg) + " *"*((num-l)//2)+1)
    else:
        print("* "*((num-l)//2) + ' '.join(msg) + " *"*((num-l)//2))
for i in range(num, 0, -1):
    print(" "*(num-i) + "* "*(i))
