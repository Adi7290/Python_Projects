lis1 = [600, 707, 134, 717, 520, 775, 549, 700, 742, 394, 236, 98, 345]

def bubble(lis1):
    for i in range(len(lis1)-1,0,-1):
        for j in range(i):
            if lis1[j]>lis1[j+1]:
                lis1[j],lis1[j+1]=lis1[j+1],lis1[j]

print(f'list before sort\n\n {lis1}\n')

bubble(lis1)

print(f'\n list after bubble sort \n\n{lis1}')

