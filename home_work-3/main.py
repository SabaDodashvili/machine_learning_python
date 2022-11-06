# 2. 0-დან 100-მდე მთელი რიცხვები ჩაწერეთ data1.txt ფაილში. myFiles
# საქაღალდეში.

data1 = open('./myFiles/data1.txt', 'w', encoding='utf-8')

for i in range(1, 31):
    data1.write(str(i))

data1.close()

# 4. myFiles2 საქაღალდეში შექმენით 30 ფაილი, ფაილებში ჩაწერეთ სიტყვები
# „Programmer1“, „Programmer2“ .... „Programmer30“.

for i in range(1, 31):
    currentFile = open(f'./myFiles2/data{i}.txt', 'w', encoding='utf-8')
    currentFile.write(f'Programmer{i}')
    currentFile.close()

# 7. დაწერეთ პროგრამა, რომელიც ფუნქციის მნიშვნელობებს დაითვლის [0; 2 ]
# შუალედში მეასედების სიზუსტით და შესაბამის მნიშვნელობებს ჩაწერს
# function.txt ფაილში myFiles საქაღალდეში.
#
# ?

# 10. შექმენით ლექსიკონი: {0: 10, 1: 20}. დაამატეთ 2 ახალი ელემენტი და დაბეჭდეთ
# მიღებული ლექსიკონი. (გამოიყენეთ update მეთოდიც). წაშალეთ რომელიმე
# ელემენტი.

dict_1 = {0: 10, 1: 20}

dict_1[2] = 30
dict_1[3] = 40
print(dict_1)

dict_1.update({"name": "saba", "lastName": "dodashvili"})
print(dict_1)

dict_1.pop(3)
print(dict_1)

# 12. დაწერეთ პროგრამა რომელიც შეამოწმებს რომელიმე key (გასაღები) არის თუ
# არა ლექსიკონში: d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} და დაბეჭდეთ
# შესაბამისი შეტობინება. (მითითება: გამოიყენეთ in ოპერატორი).

dict_2 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
anyKey = 12

if anyKey in dict_2:
    print(f"the key-{anyKey} is in the dictionary")
else:
    print(f"key-{anyKey} not found")

# 15. შექმენით სიმრავლე შემდეგი ელემენტებით: 0, 1, 2, 3, 4. დაამატეთ ნებისმიერ
# 3 ელემენტი სურვილისამებრ. წაშალეთ ორი ელემენტი სიმრავლიდან.
# დაბეჭდეთ სიმრავლის ელემენტები ცალ-ცალკე ხაზზე (გამოიყენეთ for ციკლი).
# დაითვალეთ სიმრავლის ელემენტების რაოდენობა.

dict_3 = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}

dict_3["f"] = 5
dict_3["g"] = 6
dict_3["h"] = 7

dict_3.pop("b")
dict_3.pop("a")

for i in dict_3:
    print(i)

print("length - " + str(len(dict_3)))

# 18. შექმენით tuple ტიპის ობიექტი, რომლის ელემენტებია 1-დან 100-მდე
# არსებული 5-ის ჯერადი რიცხვების კუბები. გამოიყენეთ for ციკლის მოკლე
# ჩაწერის ფორმა. შესაბამისი ფუნქციის გამოყენებით იპოვეთ tuple-ის სიგრძე
# (ელემენტების რაოდენობა).

tuple_1 = tuple()

# solution - 1
for i in range(1, 101):
    if i % 5 == 0:
        tuple_1 = list(tuple_1)
        tuple_1.append(pow(i,3))
        tuple_1 = tuple(tuple_1)

print(tuple_1)
print(len(tuple_1))

# solution - 2

arr_11 = []

[arr_11.append(pow(i, 3)) for i in range(1, 101) if i % 5 == 0]

tuple_2 = tuple(arr_11)

print(tuple_2)
print(len(tuple_2))

