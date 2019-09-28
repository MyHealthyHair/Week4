# -*- coding: UTF-8 -*-
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
#¸ÅÊöËùµãµÄÅûÈø
print('you orded a ' + pizza['crust'] + '-crust pizza '+
    'with the following toppings:')
   
for topping in pizza['toppings']:
	print('\t' + topping) 
