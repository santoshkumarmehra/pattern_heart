num = 4
for row in range(num):
    val = row+1
    dec = num-1
    for col in range(row+1):
        print(val, end='')
        val = val + dec
        dec = dec-1
    print()
