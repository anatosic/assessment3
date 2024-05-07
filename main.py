"""
Blackjack
"""
# Provide your solution here
def calculate_score(int1, int2, int3):
    sum = int1 + int2 + int3
    sum1 = sum - 10

    if sum <= 21:
        return sum
    elif sum > 21 and int1 == 11 or int2 == 11 or int3 == 11:
        print(sum1)
        if sum1 > 21:
            return "BUST"
        else:
            return sum1

print(calculate_score(9, 9, 9))
print(calculate_score(2, 8, 11))
print(calculate_score(3, 8, 11))
print(calculate_score(11, 11, 11))

"""
Even Numbers
"""
#Provide your solution here
def even_positive_numbers(list):
    positive = []

    for number in list:
        if number > 0 and number % 2 == 0:
            positive.append(number)
    return positive


#Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

print(even_positive_numbers([1, 2, 3]))
print(even_positive_numbers([10, 22, 31, 24, 35, 36]))
print(even_positive_numbers([-10, -22, 31, 24, 35, 36]))
print(even_positive_numbers([6, 9, -15, -2, 15, 20]))
