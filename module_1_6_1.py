my_dict = {"Dmitry":1972,"Denis":2005}
print(f'Dict: {my_dict}')
print(f'Existing val: {my_dict["Denis"]}')
print(f'Not existing val: {my_dict.get('Vika')}')
tmp = {'Vika':1973,'Andrey':1960}
my_dict.update(tmp)
print(f'Modified dict: {my_dict}')
vika = my_dict.pop('Vika')
print(f'Deleted val: {vika}', f'Modified dict: {my_dict}', sep='\n')
my_set = {1,1,'2','2',False,False}
print(f'Set: {my_set}')
my_set.add(4.0)
my_set.add((1,2,3))
print(f'Modified set: {my_set}')