import numpy as np
import pandas as pd
import string

ALPHABET = np.array(list(string.ascii_lowercase + string.ascii_uppercase))

dt = {
    'rand_string': [''.join(np.random.choice(ALPHABET, size=10)) for _ in range(100)],
    'rand_1_10': np.random.randint(0, 11, size=100),
    'rand_1_7': np.random.randint(1, 8, size=100),
    'rand_unique': np.random.choice(100, size=100, replace=False)
}

data = pd.DataFrame(data=dt)
data.to_excel('datasets/data.xlsx', sheet_name="sheetOne", index=False)
fn = np.array(["vinme", "sadme", "asd", "qwe", "asd", "sdq"])
ln = np.array(["lroe", "fasd", "asd", "sada", "asdas", "asdq"])

dt = {
    'rand_unique': np.random.choice(100, size=50, replace=False),
    'first_name': np.random.choice(fn, size=50),
    'last_name': np.random.choice(ln, size=50),
    'rand_2000_5000': np.random.randint(2000, 5000+1, size=50),
}

data = pd.DataFrame(data=dt)
with pd.ExcelWriter("datasets/data.xlsx", engine="openpyxl", mode="a") as writer:
    data.to_excel(writer, sheet_name="sheetTwo", index=False)

sheet1 = pd.read_excel("datasets/data.xlsx", sheet_name="sheetOne")
sheet2 = pd.read_excel("datasets/data.xlsx", sheet_name="sheetTwo")

datanew = pd.concat([sheet1, sheet2], axis=1)
datanew.to_excel("datasets/datanew.xlsx", index=False)

sheet1 = pd.read_excel("datasets/data.xlsx", sheet_name="sheetOne")

sheet3 = sheet1[sheet1.rand_string.str.contains('a')]
with pd.ExcelWriter("datasets/datanew.xlsx", engine="openpyxl", mode="a") as writer:
    sheet3.to_excel(writer, sheet_name="sheet3", index=False)

sheet2 = pd.read_excel("datasets/data.xlsx", sheet_name="sheetTwo")
sheet2[sheet2[sheet2.columns[3]] == sheet2[sheet2.columns[3]].max()]

df = pd.read_excel("datasets/file_example_XLSX_1000.xlsx", index_col=0)
df.sort_values(by=['Id'], ascending=False)
print(f"Age mean: {df['Age'].mean()}")
print(f"Age mode: {', '.join(str(m) for m in df['Age'].mode())}")
print(f"Age median: {df['Age'].median()}")
print("Oldest users: ")
print(df[df['Age'] == df['Age'].max()])
print("Youngest users: ")
print(df[df['Age'] == df['Age'].min()])

staff = pd.read_excel("datasets/staff_1000.xlsx", index_col=0)
staff_age = staff[(30 <= staff['Age']) | (staff['Age'] < 40)]
staff_age.to_excel("datasets/staff_age.xlsx")

