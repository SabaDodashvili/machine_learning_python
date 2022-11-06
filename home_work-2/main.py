import random as rd

# 2. შეიტანეთ სამი რიცხვი, იპოვეთ მათ შორის მაქსიმუმი და დაბეჭდეთ შედეგი.
# გამოიყენეთ max ფუნქცია.

arr_1 = []
index_1 = 1

while True:
    if index_1 >= 4:
        break

    arr_1.append(int(input(f"enter number {index_1}: ")))
    index_1 += 1


print(max(arr_1))

#6 დააგენერირეთ 10 შემთხვევითი მთელი რიცხვი და დაბეჭდეთ ეკრანზე. მითითება:
# გამოიყენეთ ციკლის ოპერატორი.

arr_2 = []

for i in range(0, 10):
    arr_2.append(rd.randint(1,100))

print(arr_2)

# 8. დაწერეთ ფუნქცია, რომელსაც არგუმენტად გადაეცემა ორი რიცხვი და დაითვლის
# მათ საშუალო არითმეტიკულს და დაბეჭდავს შედეგს (გაითვალისწინეთ რომ
# დაბეჭდვა უნდა მოხდეს ფუნქციის შიგნით - ფუნქცია არ აბრუნებს
# მნიშვნელობას). გამოიძახეთ ფუნქცია 3-ჯერ სხვადასხვა რიცხვებისთვის.

def printAvg(num1, num2):
    print((num1+num2) / 2)

printAvg(5,10)
printAvg(2,4)
printAvg(5,15)

# 11. დაწერეთ ფუნქცია, რომელიც შეამოწმებს პარამეტრად გადაცემული რიცხვი არის
# თუ არა კენტი. თუ კენტია, დააბრუნოს მნიშვნელობა True, თუ არადა - False.
# შეამოწმეთ რამდენიმე რიცხვისთვის და დაბეჭდეთ შედეგი.

def checkOdd(num):
    if num%2!=0:
        return True
    return False

print(checkOdd(2))
print(checkOdd(3))
print(checkOdd(4))
print(checkOdd(5))

# 15. შექმენით სია numbs ნებისმიერ 5 რიცხვითი მნიშვნელობით. იპოვეთ ამ რიცხვების
# ჯამი, მინიმალური, მაქსიმალური და საშუალო არითმეტიკული. ასევე შეასრულეთ
# შემდეგი ოპერაციები:
# • სიას დაამატეთ ბოლო ელემენტად რიცხვი 102
# • სიის მესამე ელემენტად ჩასვით რიცხვი 205
# • წაშალეთ სიის მე-4 ელემენტი
# • დაალაგეთ სია ზრდადობის მიხედვით და დაბეჭდეთ.

arr_3 = [7,2,4,9,1]

def getListAvg(list):
    return sum(list) / len(list)

print(sum(arr_3))
print(min(arr_3))
print(max(arr_3))
print(getListAvg(arr_3))

arr_3.append(102)
arr_3.insert(2,205)
arr_3.pop(3)
print(arr_3.sort())

# 19. დაწერეთ პროგრამა, რომელიც რიცხვითი მნიშვნელობების სიაში ამოშლის კენტ
# რიცხვებს. დაბეჭდეთ მიღებული სია.

arr_4 = list(range(1, 16))
index_2 = 0

while index_2 < len(arr_4):
    if arr_4[index_2] % 2 == 0:
        index_2 += 1
    else:
        arr_4.pop(index_2)
        index_2 = 0

print(arr_4)

# 21. შექმენით 10 ელემენტიანი სია, რომლის ელემენტებია ნებისმიერი შემთხვევითი
# მთელი რიცხვები 25-დან 110-მდე. დაბეჭდეთ სია და იპოვეთ მინიმალური
# ელემენტი.

arr_5 = []

for i in range(0, 10):
    arr_5.append(rd.randint(25, 110))

print(arr_5)
print(min(arr_5))


# 24. შექმენით სია რიცხვითი ელემენტებით. shuffle ფუნქციის გამოყენებით (random
# მოდულიდან) მოახდინეთ სიის ელემენტების შემთხვევითად არევა და დაბეჭდეთ
# მიღებული სია. (მითითება: ფუნქცია იწერება შემდეგნაირად: random.shuffle(x)
# სადაც x სიის დასახელებაა)

arr_6 = list(range(1, 21))
rd.shuffle(arr_6)

print(arr_6)

# 27. იპოვეთ სიაში [1, 5, 23, 5, 12, 2, 5, 1, 18, 5] ყველაზე ხშირად განმეორებადი რიცხვი.
# დაბეჭდეთ შედეგი. ასევე მიუთითეთ რამდენჯერ შეგხვდათ სიაში ყველაზე
# ხშირად განმეორებადი რიცხვი.

arr_7 = [1, 5, 23, 5, 12, 2, 5, 1, 18, 5]
arr_7_set = set(arr_7)

mostCommon = None
iterationsCount = 0

for i in arr_7_set:
    iterationsCountLocal = arr_7.count(i)

    if iterationsCountLocal > iterationsCount:
        mostCommon = i
        iterationsCount = iterationsCountLocal

print(mostCommon)

# 29. სტრიქონი &#39;python php pascal javascript java c++&#39; წარმოადგინეთ სიის სახით
# (სტრიქონის თითოეული სიტყვა სიის თითოეული ელემენტად). იპოვეთ სიის
# ყველაზე გრძელი ელემენტი (ანუ ყველაზე გრძელი სიტყვა).

arr_8 = "python php pascal javascript java c++".split(' ')
mostLengthWord = 'a'

for i in arr_8:
    if len(i) > len(mostLengthWord):
        mostLengthWord = i

print(mostLengthWord)

# 30. შეიტანეთ სიის 10 ელემენტი. იპოვეთ ამ რიცხვების საშუალო არითმეტიკული,
# მედიანა და მოდა. გაითვალისწინეთ, მედიანა წარმოადგენს შუა ელემენტს,
# როდესაც რიცხვები დალაგებულია ზრდადობით (ან კლებადობით); თუ შუაში ორი
# ელემენტია, მაშინ მედიანა არის ამ შუა ელემენტების საშუალო არითმეტიკული.
# მოდა, არის მიმდევრობაში რიცხვი, რომელიც ყველაზე ხშირად გვხვდება.
# შეიძლება მიმდევრობას არ ქონდეს მოდა (თუ ყველა ელემენტს ერთნაირი სიხშირე
# აქვს), ან ქონდეს ერთი ან რამდენიმე მოდა.

def findMode(list):
    listSet = set(list)

    mostCommon = []
    iterationsCount = 0

    for i in listSet:
        iterationsCountLocal = list.count(i)

        if iterationsCountLocal > iterationsCount:
            iterationsCount = iterationsCountLocal

    for i in listSet:
        iterationsCountLocal = list.count(i)

        if iterationsCountLocal >= iterationsCount:
            mostCommon.append(i)

    if len(mostCommon) == len(list):
        print("mode not found")
    else:
        iterator_11 = 1

        for i in mostCommon:
            print(f"mode-{iterator_11}: {i}")
            iterator_11 += 1

def findMedian(list):
    list.sort()
    if len(list) % 2 != 0:
        middleIndex = int(len(list) / 2 - 0.5)
        print(f"median: {list[middleIndex]}" )
    else:
        median = (list[int(len(list) / 2)] + list[int(len(list) / 2 - 1)]) / 2
        print(median)

arr_9 = list(range(1, 11))

arr_9_avg = sum(arr_9) / len(arr_9)
print(arr_9_avg)

findMode(arr_9)
findMode([1,1,2,2,3,3])

findMedian(arr_9)
findMedian([3, 2, 4, 1])
