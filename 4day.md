students = [
("Alice", 85),
("Bob", 92),
("Charlie", 78),
("Diana", 88)
]
print("Student Grades:")
for name, grade in students:
 print(f"{name}: {grade}")
total = sum(grade for _, grade in students)
average = total / len(students)
print(f"\nAverage Grade: {average:.2f}")
highest = max(students, key=lambda x: x[1])
lowest = min(students, key=lambda x: x[1])
print(f"Highest Grade: {highest[0]} ({highest[1]})")
print(f"Lowest Grade: {lowest[0]} ({lowest[1]})")

