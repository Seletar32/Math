import math

print('Enter quadratic in standard form (ax + bx + c) Do not include the ^2. It is automatically assummed. A cannot be negative.')
eq = input('Enter the equation here: ')
quad = eq.replace(' ', '')
q = list(quad)
i = 0
while i == 0:
    if 'x' in q:
        q.remove('x')
    elif '+' in q:
        p = q.index('+')
        q[p] = ' '
    elif '-' in q:
        m = q.index('-')
        q.insert(m, ' ')
        q[m + 1] = 'minus'
    else:
        break
while i == 0:
    if 'minus' in q:
        minus = q.index('minus')
        q[minus] = '-'
    else:
        break
a = []
while i == 0:
    if q[0] != ' ':
        qa = q[0]
        a.append(qa)
        del q[0]
    elif q[0] == ' ':
        del q[0]
        break
b = []
while i == 0:
    if q[0] != ' ':
        qb = q[0]
        b.append(qb)
        del q[0]
    elif q[0] == ' ':
        del q[0]
        break
c = []
while i == 0:
    if q == []:
        break
    elif q[0] != ' ':
        qc = q[0]
        c.append(qc)
        del q[0]
    elif q[0] == ' ':
        del q[0]
        break
a = int(''.join(a))
b = int(''.join(b))
c = int(''.join(c))

d = math.sqrt(b*b - 4*a*c)
x1 = (-b + d)/2*a
x2 = (-b - d)/2*a
print('x =', x1)
print('x =', x2)

