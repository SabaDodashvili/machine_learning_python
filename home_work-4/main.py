import numpy as np
import random as rd
# 3. შეიყვანეთ სტრიქონი. დაითვალეთ რამდენჯერ შეგხვდათ სიმბოლო “a” დაბეჭდეთ
# შედეგი.

str_1 = input("enter string: ")
print(str_1.count("a"))

# 5. text ცვლადს მიანიჭეთ სტრიქონი “სწავლის ძირი მწარე არის, კენწეროში გატკბილდების”.
# სტრიქონიდან წაიკითხეთ პირველი 20 სიმბოლო და დაბეჭდეთ შედეგი. დაითვალეთ
# რამდენჯერ არის ნახსენები სიმბოლო ‘ს’.

text = "სწავლის ძირი მწარე არის, კენწეროში გატკბილდების"

print(text[0:20])
print(f"ს - {text.count('ს')}")

# 11. text ცვლადს მიანიჭეთ შემდეგი ტექსტი: “Have a nice day”. დაბეჭდეთ ტექსტის
# თითოეული სიმბოლო ეკრანზე უკუ მიმართულებით ცალ-ცალკე ხაზზე (ანუ პირველად
# დაბეჭდავ ბოლო სიმბოლოს, შემდეგ ბოლოს წინა სიმბოლოს, და ა.შ).

text_2 = "Have a nice day"
text_2 = reversed(text_2)

[print(i) for i in text_2]

# 13. დაწერეთ პროგრამა, სადაც user შეიყვანს თავის სახელს და გვარს და პროგრამა
# დაუბეჭდავს შესაბამის იმეილის დასახელებას: მაგ: adam.giorgadze@edu.ge

user = {}

user["name"] = input("enter your name: ")
user["lastName"] = input("enter your last name: ")

print(f"{user['name']}.{user['lastName']}@edu.ge")

# 15. მოახდინეთ ორი მატრიცის შეკრების მოდელირება. მოიყვანეთ ორი მაგალითი
# (შემთხვევითი და სტატიკური რიცხვებისთვის)

a = np.array([[1,2,3],
     [4,2,1],
     [5,2,1]
     ])

b = np.array([[1,2,3],
     [4,2,1],
     [5,2,1]
     ])

sum_1 = a + b
print(sum_1)

a_1 = np.empty((3,3), dtype='int16')
b_1 = np.empty((3,3), dtype='int16')

sum_2 = a_1 + b_1
print(sum_2)

# 17. მოახდინეთ ორი მატრიცის გამრავლების მოდელირება. მოიყვანეთ ორი მაგალითი
# (შემთხვევითი და სტატიკური რიცხვებისთვის)
a_2 = np.array([[1,2,3],
     [4,2,1],
     [5,2,1]
     ])

b_2 = np.array([[1,2,3],
     [4,2,1],
     [5,2,1]
     ])

multiply_1 = np.dot(a_2, b_2)
print(multiply_1)

a_3 = np.empty((3,3), dtype="int16")
b_3 = np.empty((3,3), dtype="int16")

multiply_2 = np.dot(a_3, b_3)
print(multiply_2)

# 19. შეავსეთ 10x10 მატრიცა შემთხვევითი რიცხვებით [0, 10] შუალედიდან. წაშალეთ
# კლავიატურიდან შეტანილი რიცხვი. გამოიყენეთ numpy ბიბლიოთეკა.

arr_11 = []

for i in range(0, 100):
    arr_11.append(rd.randint(1,10))

a_11 = np.array(arr_11)
a_11.shape = 10,10

print(a_11)