n = int(input("Enter no = "))
for i in range(n):
    print(" "*(n-i-1), end="")
    count = 0
    for j in range(i+1):
        print("*", end="")
        if count<i:
            print("A", end="")
        count += 1
    print()