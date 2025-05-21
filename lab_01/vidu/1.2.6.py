#câu lệnh điều lệnh
x = 10
if x > 5:
    print("x lớn hơn 5")
elif x == 5:
    print("x bằng 5")
else:
    print("x nhỏ hơn 5")

#vòng lặp for
fruits = ["apple", "banana", "chery"]
for fruit in fruits:
    print(fruit)

#vòng lặp while
count = 0
while count < 5:
    print(count)
    count += 1

#câu lệnh nhảy break
for i in range(1, 101):
    if i % 5 == 0:
        print("Số chia hết cho 5 đầu tiên là: ",i)
        break

#câu lệnh nhảy continue
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)

#câu lệnh nhảy pass
x = 5
if x > 10:
    print("x lớn hơn 10")
else:
    pass