# coding=utf-8
#1
alien_0 = {'color': 'green', 'points':5}
alien_1 = {'color': 'yellow', 'points':10}
alien_2 = {'color': 'red', 'points':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

#2
print('\n')
#����һ�����ڴ��������˵Ŀ��б�
aliens = []

#����30����ɫ��������
for alien_number in range(30):
	new_alien = {'color': 'green','points':5, 'speed': 'slow'}
	aliens.append(new_alien)
	
#��ʾǰ���������
for alien in aliens[:5]:
	print(alien)
print('...')

#��ʾ�����˶��ٸ�������

#3
print('\n')
#����һ�����ڴ��������˵Ŀ��б�
aliens = []

#����30����ɫ��������
for alien_number in range(30):
	new_alien = {'color': 'green','points':5, 'speed': 'slow'}
	aliens.append(new_alien)
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15
		
#��ʾǰ���������
for alien in aliens[:5]:
	print(alien)
print('...')
