import numpy as np

m1 = np.random.randint(0, 101, size=36)
m2 = np.random.randint(0, 101, size=(6, 6))
m3 = np.random.randint(0, 101, size=(6, 3, 2))

print(m1)
print(m2)
print(m3)

def find_factors(n: int) -> np.ndarray:
    divisors = np.array([], dtype=int)
    i = 2
    while i <= np.sqrt(n):
        if (n % i == 0):
            if (n / i == i):
                divisors = np.append(divisors,i)
            else :
                divisors = np.append(divisors, i)
                divisors = np.append(divisors, int(n/i))
        i+=1
    return divisors

m = np.random.randint(0, 101, size=36)

d2 = {}
for d in find_factors(len(m)):
    c = m.reshape(d, int(len(m)/d))
    d2[f"{d}x{int(len(m)/d)}"] = c


d3 = {}

n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))

print(f"{n1}+{n2} = {np.add(n1, n2)}")
print(f"{n1}-{n2} = {np.subtract(n1, n2)}")
print(f"{n1}x{n2} = {np.multiply(n1, n2)}")
print(f"{n1}/{n2} = {np.divide(n1, n2)}")


a = np.random.randint(0, 101, size=36)
n = int(input("Enter number: "))
print(a/n)
print()
print(a//n)

m1 = np.random.randint(0, 101, size=(5, 3))
m2 = np.random.randint(0, 101, size=(3, 2))

print(m1.dot(m2))

n = np.concatenate((
    np.random.randint(0, 101, size=6),
    np.random.randint(0, 101, size=9),
    np.random.randint(0, 101, size=12)
))

print(n)

a1 = np.random.randint(0, 100, size=12)
a2 = np.random.randint(0, 100, size=12)

print(a1)
print(a2)
print()
print(np.inner(a1, a2))
print(np.outer(a1, a2))

print(np.roots([1, 4, -5]))
print(np.roots([1, -2, 1, -4, -5]))

coeff = []
equation = input("Enter equation: ").replace(" ", "")
equation = equation.replace("+", " +").replace("-", " -")
print(equation)

for p in equation.split():
    n = p.split('x')[0]
    if n == '':
        coeff.append(1)
    elif n[0] == '-':
        if len(n[0]) == 1:
            coeff.append(-1)
        else:
            coeff.append(int(n.removeprefix("-"))*-1)
    elif n[0] == '+':
        coeff.append(int(n.removeprefix("+")))
    else:
        coeff.append(int(n))

print(coeff)
print(np.roots(coeff))


x = [3, 9, 4]
p1 = np.poly1d([1, 4, -5])
p2 = np.poly1d([1, -2, 1, -4, -5])

for xi in x:
    print(f"x={xi}:")
    print(f"\tx^2 + 4x - 5 = {p1(xi)}")
    print(f"\tx^4 - 2x^3 + x^2 - 4x - 5 = {p2(xi)}")

def get_coeff(equation: str) -> list:
    coeff = []
    for p in equation.split():
        n = p.split('x')[0]
        if n == '':
            coeff.append(1)
        elif n[0] == '-':
            if len(n) == 1:
                coeff.append(-1)
            else:
                coeff.append(int(n.removeprefix("-"))*-1)
        elif n[0] == '+':
            coeff.append(int(n.removeprefix("+")))
        else:
            coeff.append(int(n))
    return coeff


equation = input("Enter equation: ").replace(" ", "").strip()
equation = equation.replace("+", " +").replace("-", " -")

coeff = get_coeff(equation)
x = np.array(input("Enter points seperated by comma (ex. 1, 2, 3): ").split(', '), dtype=int)
p = np.poly1d(coeff)

for xi in x:
    print(f"x={xi}:")
    print(f"\t{equation}={p(xi)}")


d = [2, 3, 4, 5]
for di in d:
    m = np.random.randint(0, 20, size=(di, di))
    print("Matrix: ")
    print(m)
    print(f"Determinant: {np.linalg.det(m)}")


def minor_matrix(arr, i, j):
    return np.delete(np.delete(arr,i,axis=0), j, axis=1)


m = np.array([
    [8, 2, 1, 2],
    [4, 1, 3, 9],
    [9, 4, 7, 1],
    [5, 8, 4, 6]
])

for i in range(len(m)):
    for j in range(len(m[0])):
        print(i, j)
        print(minor_matrix(m, i, j))
        print()

