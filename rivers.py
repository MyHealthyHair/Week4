rivers = {
    'nile': 'egypt',
    'long river': 'china',
    'yellow river': 'china',
    }
for river, country in rivers.items():
	print('the '+ river.title()+' runs through '+country.title())
	
for river in rivers.keys():
	print(river.title())
	
for country in rivers.values():
	print(country.title())
