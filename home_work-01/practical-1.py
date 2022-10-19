# 24-მდე კლასში გავაკეთეთ

# 24) შეიყვანეთ რიცხვი კლავიატურიდან. პროგრამამ უნდა დაბეჭდოს შეყვანილი რიცხვის ყველა გამყოფი. (მაგ. 18-ისგამოყოფებია: 1, 2, 3, 6, 9, 18)
flag = False
num = int(input())
pas = 0
cout = num
while pas != num:
    if num // cout == num / cout:
        if num // cout != 0:
            pas = num // cout
            print(pas, end=' ')
    cout = cout - 1
if num == 1:
    print()
    print('ara')
elif num == 2:
    print()
    print('martivis')
elif num % 2 == 0:
    print()
    print('ara')
else:
    print()
    print('martivia')
    

print('============================================================================')
#26) დაბეჭდეთ 2-დან 1000-მდე ყველა მარტივი რიცხვი.
stop = False
for i in range(2,1000):
    for j in range(2, int((i/2)+1)):
            if(i % j !=0): 
                stop = True
            else:
                stop = False
                break
    if(stop == True):
        print(i)
        

print('============================================================================')
#28) შეიყვანეთ ნებისმიერი რიცხი. იპოვეთ ამ რიცხვის ციფრთა რაოდენობა და დაბეჭდეთ.
n = int(input())
s= 0
while n  :
    s += 1 
    n //= 10
print (s)


print('============================================================================')
# 31)შეიყვანეთ ნებისმიერი რიცხი. დაადგინეთ არის თუ არა შეტანილი რიცხვი პალინდრომი. (მითითება: პალინდრომია
# რიცხვი, რომელიც მარჯვნიდან და მარცხნიდან ერთნაირად იკითხება). მაგ. 12521
def isPal(n):
    r=0
    nn=n
    while (n>0):
        k=n%10
        r=r*10+k
        n=n//10
    return r==nn
    
p=int(input())
if isPal(p):
    print("aris")
else:
    print("ar aris")