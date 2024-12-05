immutable_var = 1,"2",3.0,True,[1,2,3]
print(f'Кортеж: {immutable_var}')
# immutable_var[1] = 2 кортеж является неизменяемым типом данных
# и данная команда приведёт к ошибке TypeError
mutable_list = [1,2,3,4,"0",False,(1,2,3)]
print(f'Список: {mutable_list}')