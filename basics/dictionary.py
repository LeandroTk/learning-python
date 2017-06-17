tk = {
    'first_name': 'Leandro',
    'last_name': 'Kinoshita',
    'nicknames': ['TK', 'Dinho'],
    'age': 24
}

print(tk['first_name'])
print(tk['last_name'])
print(tk['nicknames'])
print(tk['age'])

tk['marriage'] = False
print(tk['marriage'])

del tk['marriage']
print('-----------')
print(tk)
