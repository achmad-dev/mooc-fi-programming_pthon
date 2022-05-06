# Write your solution here
students = int(input("How many students on the course?"))
group_size = int(input("Desired group size?"))
if students % group_size > 0:
    print(f"Number of groups formed: {students // group_size + 1}")
elif students % group_size == 0:
    print(f"Number of groups formed: {students // group_size}")
