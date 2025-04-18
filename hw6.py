def multiple_table(n):
    for i in range (1,10):
        for j in range(n,n+4):
            print(f'{j}x{i}={j*i:2d}',end='\t')
        print()
    print()

multiple_table(2)
multiple_table(6)
