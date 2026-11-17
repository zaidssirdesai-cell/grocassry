def calculate_gross_salary():
    basic_salary = 50000
    hra = basic_salary * 0.20
    da = basic_salary * 0.10
    gross_salary = basic_salary + hra + da

    print("Basic Salary:", basic_salary)
    print("HRA:", hra)
    print("DA:", da)
    print("Gross Salary:", gross_salary)

calculate_gross_salary()