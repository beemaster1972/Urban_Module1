grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
avrg_grades = [sum(el)/len(el) for el in grades]
average_grades = dict(zip(students,avrg_grades))
print(average_grades)