pets = []

pet = {
    'animal type': 'cat',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'meats',
      }
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
       }
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'eggs',
      }
pets.append(pet)

for pet in pets:
    print("\nHere's the information about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
