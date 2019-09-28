favorite_numbers = {
    'ann': [2, 4],
    'belle': [2, 3, 5],
    'carl': [71, 1],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))
