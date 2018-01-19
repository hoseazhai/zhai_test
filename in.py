NUM = 12
count = 0

while(count < 3):
    number = input('Please input number ')
    n = int(number)
    if n == NUM:
        print('you are win')
        break
    elif n < NUM:
        print('less')
    else:
        n > NUM
        print('more')
    count += 1
else:
    print('you are fired')
