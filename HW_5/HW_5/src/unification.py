def unify(x, y, s):
    if s == None:
        return None
    elif x == y:
        return s  
    elif isinstance(x, str) and x.startswith('?'):
        return unify_var(x, y, s)
    elif isinstance(y, str) and y.startswith('?'):
        return unify_var(y, x, s)
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        return unify(x[1:], y[1:], unify(x[0], y[0], s))
    else:
        return None  

def unify_var(var, x, s):
    if var in s:
        return unify(s[var], x, s)
    elif occur_check(var, x):
        return None
    else:
        s[var] = x
        return s

def occur_check(var, x):
    if var == x:
        return True
    elif not isinstance(x, str) and isinstance(x, list):
        return var in x
    return False

num1 = '1. human(?x) U human(?y)'
res = unify(['human', '?x'], ['human', '?y'], {})
print(num1)
print(str(res))
print

num2 = '2. likes(?x,?y) U likes(pat0, chris2)'
res = unify(['likes', '?x', '?y'], ['likes', 'pat0', 'chris2'], {})
print(num2)
print(str(res))
print

num3 = '3. likes(?x,?x) U likes(pat0, chris2)'
res = unify(['likes', '?x', '?x'], ['likes', 'pat0', 'chris2'], {})
print(num3)
print(str(res))
print

num4 = '4. likes(?x,?x) U likes(?y, pat0)'      #{'?y': 'pat0', '?x': '?y'}
res = unify(['likes', '?x', '?x'], ['likes', '?y', 'pat0'], {}) 
print(num4)
print(str(res))
print

num5 = '5. likes(pat0,?x) U likes(?y, pat0)'
res = unify(['likes', 'pat0', '?x'], ['likes', '?y', 'pat0'], {})
print(num5)
print(str(res))
print

num6 = '6. likes(?x,?y) U likes(friend(pat0),pat0)'
res = unify(['likes', '?x', '?y'], ['likes', ['friend', 'pat0'], 'pat0'], {})
print(num6)
print(str(res))
print

num7 = '7. likes(friend(?x),?x) U likes(friend(?y),?y)'
res = unify(['likes', ['friend', '?x'], '?x'], ['likes', ['friend', '?y'], '?y'], {})
print(num7)
print(str(res))
print

num8 = '8. suburb(sk1(?x),?x) U suburb(?y,Naperville)'
res = unify(['suburb', ['sk1', '?x'], '?x'], ['suburb', '?y', 'Naperville'], {})
print(num8)
print(str(res))
print

num9 = '9. suburb(sk2(?x),?x) U suburb(sk3(?y),Naperville)'
res = unify(['suburb', ['sk2', '?x'], '?x'], ['suburb', ['sk3', '?y'], 'Naperville'], {})
print(num9)
print(str(res))
print

num10 = '10. suburb(sk3(?x),?x) U suburb(sk3(?y),Napervilile)'  #{'?y': 'Naperville', '?x': '?y'}
res = unify(['suburb', ['sk3', '?x'], '?x'], ['suburb', ['sk3', '?y'], 'Naperville'], {}) 
print(num10)
print(str(res))
print



