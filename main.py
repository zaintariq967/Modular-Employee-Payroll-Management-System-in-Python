from employee import *
from payroll import calculate_bonus, calculate_allowance, gross_salary
from payroll import net_salary as ns

# Employee Details
name = get_employee_name()
emp_id = get_employee_id()
salary = get_employee_salary()

# Payroll Calculations
bonus = calculate_bonus(salary)
allowance = calculate_allowance(salary)

gross = gross_salary(salary, bonus, allowance)
net = ns(gross)

# Salary Slip
print("=" * 35)
print(f"{'SALARY SLIP':^35}")
print("=" * 35)

print(f"{'Employee Name':<18}: {name}")
print(f"{'Employee ID':<18}: {emp_id}")
print(f"{'Basic Salary':<18}: {salary:.2f}")

print("-" * 35)

print(f"{'Bonus (10%)':<18}: {bonus:.2f}")
print(f"{'Allowance (15%)':<18}: {allowance:.2f}")
print(f"{'Gross Salary':<18}: {gross:.2f}")
print(f"{'Net Salary':<18}: {net:.2f}")

print("=" * 35)