favoritelanguages = {
    'jen':['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favoritelanguages.items():
	print('\n' + name.title() + "'s favorite languages are: ")
	for language in languages:
		print('\t' + language.title())
		
