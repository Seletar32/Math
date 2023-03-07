#getting equations
print('When entering your equation, please use standard form (ax+by=c). Use spaces to seperate numbers from operators.')
eq1 = input('Enter equation 1 here: ')
eq2 = input('Enter equation 2 here: ')

#creating equations
list1 = list(eq1)
list2 = list(eq2)
len1 = len(list1)
len2 = len(list2)

#getting co-efficients
i = 0
while i == 0:
    if ' ' in list1:
        list1.remove(' ')
    elif '+' in list1:
        list1.remove('+')
    elif '-' in list1:
        list1.remove('-') 
    elif '=' in list1:
        list1.remove('=')
    elif 'x' in list1:
        xl1 = list1.index('x')
        list1[xl1] = '  '
    elif 'y' in list1:
        yl1 = list1.index('y')
        list1[yl1] = '  '
    else:
        break
while i == 0:
    if ' ' in list2:
        list2.remove(' ')
    elif '+' in list2:
        list2.remove('+')
    elif '-' in list2:
        list2.remove('-')
    elif '=' in list2:
        list2.remove('=')
    elif 'x' in list2:
        xl2 = list2.index('x')
        list2[xl2] = '  '
    elif 'y' in list2:
        yl2 = list2.index('y')
        list2[yl2] = '  '
    else:
        break
    
#saving co-efficients
a1 = list1.index('  ')
a = list1[0:a1]
del list1[0:a1 + 1]

b1 = list1.index('  ')
b = list1[0:b1]
del list1[0:b1 + 1]

x = list1[:]
list1.clear()


d1 = list2.index('  ')
d = list2[0:d1]
del list2[0:d1 + 1]

e1 = list2.index('  ')
e = list2[0:e1]
del list2[0:e1 + 1]

y = list2[:]
list2.clear()


a = int(''.join(a))
b = int(''.join(b))
x = int(''.join(x))
d = int(''.join(d))
e = int(''.join(e))
y = int(''.join(y))

#solving systems
matrix1 = (((e/(a*e - b*d)) * x) + ((-b/(a*e - b*d)) * y))
matrix2 = (((-d/(a*e - b*d)) * x) + ((a/(a*e - b*d)) * y))

#outputting answer
print('x = ', matrix1)
print('y = ', matrix2)
