def calculate_sqrt(number, precision) -> float:
    if number < 0:
        return None

    a = number
    p = number

    while True:
        b = (a + p) / 2

        if abs(b * b - number) < 10**(-2 * precision):
            break

        a = b
        p = number / a

    return round(b, precision)

def get_user_input():
    number = int(input("Enter the number to calculate the square root of: "))
    precision = int(input("Enter the number of decimal places for precision: "))
    return number, precision

def display_result(result, precision):
    formatted_result = "{:.{}f}".format(result, precision)
    print("Result:", formatted_result)

def main():
    number, precision = get_user_input()
    result = calculate_sqrt(number, precision)
    display_result(result, precision)

if __name__ == "__main__":
    main()

