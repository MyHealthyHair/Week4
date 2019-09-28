favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    } 
    
survey = ['jen','sarah','ellen','phil']
for person in favorite_languages:
    if person in survey:
        print('Thank you for accepting my survey, '+person.title()+'!')
    else:
        print('Would you like to take my survey, '+ person.title()+'?')
