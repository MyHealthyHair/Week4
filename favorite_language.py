#1
favorite_language = {
    'gen':'python',
    'sarah':'c',
    'phill':'ruby',
    'gin':'python',
    }

for name, language in favorite_language.items():
	print(name.title()+"'s favorite language is " + 
	    language.title() + ' .')

#2
print('\n')

favorite_language = {
    'gen':'python',
    'sarah':'c',
    'phill':'ruby',
    'gin':'python',
    }

for name in favorite_language.keys():
	print(name.title())

#3
print('\n')

favorite_language = {
    'gen':'python',
    'sarah':'c',
    'phill':'ruby',
    'gin':'python',
    }

friends=['phill','sarah']
for name in favorite_language.keys():
	print(name.title())
	
	if name in friends:
		print('hi '+name.title()+
		    ', I see your favorite language is '+
		    favorite_language[name].title()+'!')
		    
#4
print('\n')

favorite_language = {
    'gen':'python',
    'sarah':'c',
    'phill':'ruby',
    'gin':'python',
    }

if 'erin' not in favorite_language.keys():
	print('erin, please take our roll!')
	
#5
print('\n')

favorite_language = {
    'gen':'python',
    'sarah':'c',
    'phill':'ruby',
    'gin':'python',
    }
    
for name in sorted(favorite_language.keys()):
	print(name.title()+ ', thank you for taking the poll.')
	
#6
print('\n')

favorite_language = {
    'gen':'python',
    'sarah':'c',
    'phill':'ruby',
    'gin':'python',
    }
    
print('the following languages have been mentioned: ')
for language in favorite_language.values():
	print(language.title())
	
#7
print('\n')

favorite_language = {
    'gen':'python',
    'sarah':'c',
    'phill':'ruby',
    'gin':'python',
    }
    
print('the following languages have been mentioned: ')
for language in set(favorite_language.values()):
	print(language.title())
