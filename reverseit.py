def reverse_it(val):
    if val.isdigit():
        number = int(val)
        reverse = 0
        while number > 0:
            digit = number % 10
            reverse = reverse * 10 + digit
            number //= 10
        return reverse
    else:
        return val[::-1]

your_input = input("Enter any string or number: ")
print("After Reverse:", reverse_it(your_input))