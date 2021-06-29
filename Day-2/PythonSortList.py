employees = [
    {'Name': 'Sankalp Swarup', 'age': 21, 'salary': 10000},
    {'Name': 'Ayush Vaidya', 'age': 19, 'salary': 8000},
    {'Name': 'Khushi Sharma', 'age': 18, 'salary': 1000},
    {'Name': 'Siddharth Maratha', 'age': 30, 'salary': 15000},
]


employees.sort(key=lambda x: x.get('Name'))
print(employees, end='\n\n')


employees.sort(key=lambda x: x.get('age'))
print(employees, end='\n\n')


employees.sort(key=lambda x: x.get('salary'), reverse=True)
print(employees, end='\n\n')