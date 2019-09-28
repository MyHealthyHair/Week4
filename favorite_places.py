favorite_places = {
    'abby': ['mountain', 'valley', 'paris'],
    'ellen': ['hawaii', 'iceland'],
    'caroline': ['new york', 'the playground', 'south carolina']
                  }

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())
