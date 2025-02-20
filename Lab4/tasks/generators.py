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
    for i in range(n, -1, -1):
        yield i

def main():
    while True:
        print("\nChoose an option:")
        print("1. Generate squares up to N")
        print("2. Print even numbers up to n")
        print("3. Numbers divisible by 3 and 4 up to n")
        print("4. Squares from a to b")
        print("5. Countdown from n to 0")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            N = int(input("Enter N: "))
            print(list(square_generator(N)))
        elif choice == "2":
            n = int(input("Enter n: "))
            print(", ".join(map(str, even_numbers(n))))
        elif choice == "3":
            n = int(input("Enter n: "))
            print(list(divisible_by_3_and_4(n)))
        elif choice == "4":
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            print(list(squares(a, b)))
        elif choice == "5":
            n = int(input("Enter n: "))
            print(list(countdown(n)))
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
