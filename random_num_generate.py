import random

number_a = int(input("Enter first number:"))
number_b = int(input("Enter second number:"))


def generate_random_numbers(count):
	random_numbers = []
	for _ in range(count):
		number = random.randint(number_a, number_b)
		random_numbers.append(number)
	return random_numbers	

random_numbers = generate_random_numbers(5)
print(random_numbers)