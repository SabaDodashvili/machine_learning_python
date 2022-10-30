# 2) დაწერეთ პროგრამა, რომელიც შეყვანილ ათობით რიცხვს გადაიყვანს ორობითში.

num_1 = int(input("enter number"))
bin(num_1)

# 4) დაწერეთ პროგრამა, სადაც მომხმარებელი შეიყვანს 3 რიცხვს და პროგრამა დაბეჭდავს რიცხვების საშუალო არითმეტიკულს.

count = 0
numsArr_1 = []

while True:
    if not count < 3: break

    numsArr_1.append(int(input("enter number: ")))
    count += 1

arrAvg = sum(numsArr_1) / len(numsArr_1)
print(arrAvg)

# 7) დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ ნებისმიერ რიცხვს. პროგრამამ შეამოწმოს, თუ შეყვანილი
# რიცხვი 10-ის ჯერადია, დაბეჭდოს “რიცხვი ბოლოვდება 0-ით”, თუ არადა დაბეჭდოს “რიცხვი არ ბოლოვდება 0-ით”.
# (გაითვალისწინეთ: 10-ის ჯერადი ნიშნავს რომ 10-ზე გაყოფისას ნაშთი არის 0).

num_2 = int(input("enter number: "))

if num_2 % 10 == 0:
    print("რიცხვი ბოლოვდება 0-ით")
else:
    print("რიცხვი არ ბოლოვდება 0-ით")

# 10) დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ წელს და დაადგენთ არის თუ არა შეყვანილი რიცხვი ნაკიანი
# წელიწადი. მაგ: 2012, 2016 წლები ნაკიანია. გაითვალისწინეთ, ნაკიანია წელიწადი, რომელიც უნაშთოდ იყოფა
# ოთხზე, გარდა იმ წლებისა რომლებიც იყოფა 100-ზე მაგრამ არ იყოფა 400-ზე. მაგ. 2100, 2200, 2300 წლები არ არის
# ნაკიანი. 2000 წელი ნაკიანია.

year = int(input("enter year: "))
isLeapYear = year % 4 == 0 and year % 100 == 0 and not year % 400 == 0

if isLeapYear:
    print("არ არის ნაკიანი")
elif year % 4 == 0:
    print("ნაკიანია")

# 11) დაბეჭდეთ 5-ის ჯერადი რიცხვები 20-დან 125-ის ჩათვლით.

for i in range(20, 126):
    if i % 5 == 0:
        print(i)

# 14) შეიყვანეთ 10 რიცხვი კლავიატურიდან ციკლის გამოყენებით. დაითვალეთ შეყვანილი რიცხვების საშუალო
# არითმეტიკული.

count_2 = 0
numsArr_2 = []

while True:
    if not count_2 < 10: break

    numsArr_2.append(int(input("enter number: ")))
    count_2 += 1

arrAvg = sum(numsArr_2) / len(numsArr_2)
print(arrAvg)

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


# 26) დაბეჭდეთ 2-დან 1000-მდე ყველა მარტივი რიცხვი.

stop = False
for i in range(2, 1000):
    for j in range(2, int((i / 2) + 1)):
        if (i % j != 0):
            stop = True
        else:
            stop = False
            break
    if (stop == True):
        print(i)

# 28) შეიყვანეთ ნებისმიერი რიცხი. იპოვეთ ამ რიცხვის ციფრთა რაოდენობა და დაბეჭდეთ.

n = int(input())
s = 0
while n:
    s += 1
    n //= 10
print(s)

# 31)შეიყვანეთ ნებისმიერი რიცხი. დაადგინეთ არის თუ არა შეტანილი რიცხვი პალინდრომი. (მითითება: პალინდრომია
# რიცხვი, რომელიც მარჯვნიდან და მარცხნიდან ერთნაირად იკითხება). მაგ. 12521

def isPal(n):
    r = 0
    nn = n
    while (n > 0):
        k = n % 10
        r = r * 10 + k
        n = n // 10
    return r == nn


p = int(input())
if isPal(p):
    print("aris")
else:
    print("ar aris")