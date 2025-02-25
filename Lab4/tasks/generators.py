def square_generator(N):
    for i in range(N + 1):
        yield i ** 2
    


def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

def countdown(n):
    for i in range(n, -1):
        yield i
def display_menu():
    print("1. Generate squares from 0 to N")
    print("2. Generate even numbers from 0 to N")
    print("3. Generate numbers divisible by 3 and 4 from 0 to N")
    print("4. Generate squares between a and b")
    print("5. Countdown from N")
    print("6. Exit")

def menu():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            N = int(input("Enter the value of N: "))
            print("Squares from 0 to", N)
            for square in square_generator(N):
                print(square)

        elif choice == '2':
            n = int(input("Enter the value of N: "))
            print("Even numbers from 0 to", n)
            for number in even_numbers(n):
                print(number)

        elif choice == '3':
            n = int(input("Enter the value of N: "))
            print("Numbers divisible by 3 and 4 from 0 to", n)
            for number in divisible_by_3_and_4(n):
                print(number)

        elif choice == '4':
            a = int(input("Enter the value of a: "))
            b = int(input("Enter the value of b: "))
            print("Squares from", a, "to", b)
            for square in squares(a, b):
                print(square)

        elif choice == '5':
            n = int(input("Enter the value of N: "))
            print("Countdown from", n)
            for count in countdown(n):
                print(count)

        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

menu()
