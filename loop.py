for number in range(1,100):
    if number % 3 == 0:
        print(f"{number} Fizz")
        if number % 5 == 0:
            print(f"{number} Buzz")

        if number % 3 == 0 and number % 5 == 0:
            print(f"{number} FizzBuzz")