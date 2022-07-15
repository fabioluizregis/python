c = 5
while c != 0:
    print(c)
    c -= 1

print("==============")

c = 5
while c:
    print(c)
    c -= 1

print("=======Using break=======")

while True:
    print("Type a number that is divided by 7: ")
    response = input()
    if int(response) % 7 == 0:
        break
