def get_fizzbuzz(my_input):
    my_fizzbuzz_result = ''
    if my_input % 3 == 0 and my_input % 5 == 0: # No curly braces
        my_fizzbuzz_result = 'Fizzbuzz'
    elif my_input % 3 == 0 and not (my_input % 5 == 0):
        my_fizzbuzz_result = 'Fizz'
    elif not (my_input % 3 == 0) and my_input % 5 == 0:
        my_fizzbuzz_result = 'Buzz'
    else:
        my_fizzbuzz_result = 'Try again!'
    print(my_fizzbuzz_result)

get_fizzbuzz(45)
get_fizzbuzz(5)


def calc_exp(num, power=2):
    return num**power

print(calc_exp(3))
print(calc_exp(3,3))
