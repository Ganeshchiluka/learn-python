input_number = int(input("Enter number: "))

def is_palindrome(input_number):
    actual = input_number
    inverse = 0
    while input_number > 0 :
        digit = input_number % 10
        inverse = inverse * 10 + digit
        input_number //= 10
    return inverse==actual

if is_palindrome(input_number):
    print(str(input_number) +" is a Palindrome number.")
else:
    print(str(input_number)+" is not a Panlindrome number.")