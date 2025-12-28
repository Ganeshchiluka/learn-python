input_number = int(input("Enter number: "))

def is_armstrong(input_number):
    total_sum = 0
    num = input_number
    length = len(str(input_number))
    while num > 0 :
        digit = num % 10
        total_sum = total_sum + (digit**length)
        num //= 10
    return total_sum==input_number

if is_armstrong(input_number):
    print(str(input_number) +" is an Armstrong number.")
else:
    print(str(input_number)+" is not an Armstrong number.")