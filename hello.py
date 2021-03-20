#print('Hello world!!!')
#name = input('What is your name?')
#print('Hello {0} !!! {1} !!!'.format(name,name))

name = 'Dima;Vova;Petya'

#print(dir(name))
userlist = name.split(';')
d = '========='.join(userlist)
print(d.swapcase())

'''
userlist = name.split(';')
print(userlist)
for item in userlist:
	print(len(item))
	print('hello')
print('End')
'''



