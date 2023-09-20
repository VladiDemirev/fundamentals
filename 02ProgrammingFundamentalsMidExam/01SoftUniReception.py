employee_one_efficiency = int(input())
employee_two_efficiency = int(input())
employee_three_efficiency = int(input())
students_count = int(input())

students_serverd_per_hour = employee_one_efficiency + employee_two_efficiency + employee_three_efficiency

hours_needed = 0

while students_count > 0:
  students_count -= students_serverd_per_hour
  hours_needed += 1

  if hours_needed % 4 == 0:
    hours_needed += 1

print(f"Time needed: {hours_needed}h.")
