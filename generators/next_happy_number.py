def get_sum_of_squares_of_digits(num):
    sum_of_digit = 0
    
    while num:
        digit = num % 10
        square = digit** 2
        sum_of_digit += square
        num = num//10

    return sum_of_digit

def is_happy_number(num):
    already_visited = set()

    while True:
        if num == 1:
            return True

        elif num in already_visited:
            return False
        
        already_visited.add(num)
        num = get_sum_of_squares_of_digits(num)

def next_happy_number(number):
    while True:
        if is_happy_number(number):
            yield number

        number += 1   

get_the_happy_number = next_happy_number(7)

print(next(get_the_happy_number))
print(next(get_the_happy_number))
print(next(get_the_happy_number))
print(next(get_the_happy_number))
print(next(get_the_happy_number))
    
    