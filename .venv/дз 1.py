def main():
    name = input("введіть своє ім'я: ")
    age = input("введіть свій вік: ")
    print(f"Привіт {name}, тобі {age}!")
if __name__ == "__main__":
    main()


def main():
    age = int(input("введіть свій вік: "))
    if age > 18:
        print("вхід дозволено!")
    else:
        print("вхід заборонено!")
if __name__ == "__main__":
    main()

import random
def guess_the_number():
    secret_number = random.randint(1, 10)
    attempts = 3
    print("я загадав число від 1 до 10. У вас є три спроби вгадати його")
    for attempt in range(1, attempts + 1):
        guess = int(input(f"спроба {attempt}, ваше число: "))
        if guess == secret_number:
            print("ви вгадали!")
            break
        elif guess > secret_number:
            print("менше")
        else:
            print("більше")
        if attempt == attempts:
            print(f"ви програли! Загадане число було {secret_number}")
if __name__ == "__main__":
    guess_the_number()


def print_range():
    start = int(input("з: "))
    end = int(input("по: "))
    print("числа у вибраному діапазоні:")
    for number in range(start, end + 1):
        print(number, end=" ")
if __name__ == "__main__":
    print_range()


def print_even_reverse():
    n = int(input("введіть число n: "))
    print("парні числа у зворотному порядку:")
    for number in range(n, 0, -1):
        if number % 2 == 0:
            print(number, end=" ")
if __name__ == "__main__":
    print_even_reverse()


def determine_grade():
    score = int(input("введіть кількість балів від 0 до 100: "))
    if 0 <= score <= 49:
        print("незадовільно")
    elif 50 <= score <= 69:
        print("задовільно")
    elif 70 <= score <= 89:
        print("добре")
    elif 90 <= score <= 100:
        print("відмінно")
if __name__ == "__main__":
    determine_grade()


def calculator():
    a = float(input("введіть перше число: "))
    b = float(input("введіть друге число: "))
    operation = input("виберіть дію із цих пропозицій: +, -, *, /: ")
    if operation == '+':
        print(f"відповідь: {a + b}")
    elif operation == '-':
        print(f"відповідь: {a - b}")
    elif operation == '*':
        print(f"відповідь: {a * b}")
    elif operation == '/':
        if b == 0:
            print("Помилка: ділення на нуль!")
        else:
            print(f"відповідь: {a / b}")
if __name__ == "__main__":
    calculator()