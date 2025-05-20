# if문
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0;
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# for 문
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# range() 함수
for i in range(5):
    print(i)

# 함수+인자 기본
def describe_number(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(describe_number(7))

# 리스트+append()
squares = []
for i in range(5):
    squares.append(i ** 2)

print(squares)

# 딕셔너리 반복
person = {"name": "Alice", "age": 28}
for key, value in person.items():
    print(f"{key} → {value}")



