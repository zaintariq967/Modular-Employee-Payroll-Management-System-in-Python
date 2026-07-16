def calculate_bonus(salary):
    return salary * 0.10      # 10% Bonus


def calculate_allowance(salary):
    return salary * 0.15      # 15% Allowance


def gross_salary(salary, bonus, allowance):
    return salary + bonus + allowance


def net_salary(gross):
    tax = gross * 0.05        # 5% Tax
    return gross - tax