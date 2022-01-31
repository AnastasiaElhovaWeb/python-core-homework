from data import EMPLOYEES
from data import DEPARTMENTS

def cross_join(employees, departments):
    """
    Реализует декартово произведение списков employees и departments

    :param employees: Список LastName сотрудников таблицы Employee
    :param departments: Список DepartmentName таблицы Department
    :return: Генератор пар (LastName, DepartmentName)
    """
    indexEmployer = 0
    indexDepartment = 0
    while indexEmployer < len(employees):
        while indexDepartment < len(departments):
            yield (employees[indexEmployer], departments[indexDepartment])
            indexDepartment += 1
        indexEmployer += 1
        indexDepartment = 0

cr = cross_join(EMPLOYEES, DEPARTMENTS)
print(next(cr))
print(next(cr))