#coding utf-8
answer = ""
numbers = []
result = 0
while True:
    answer = input("Пиши цифру... иле не цифру: ")
    try:
        answer = float(answer)
        numbers.append(answer)
        print(numbers)
    except ValueError or TypeError:
        print(numbers)
        for i in numbers:
            result += i
        print ("Сумма: {0:.2f}".format(result))
        break



