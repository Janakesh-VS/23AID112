employees = [
    ("Arjun",   "FullTime", 85000),
    ("Meena",   "PartTime", 32000),
    ("Ravi",    "FullTime", 60000),
    ("Priya",   "FullTime", 72000),
    ("Karthik", "PartTime", 28000),
    ("Ananya",  "FullTime", 95000),
    ("Vikram",  "FullTime", 78000),
    ("Divya",   "PartTime", 35000),
    ("Suresh",  "FullTime", 54000),
    ("Neha",    "PartTime", 30000),
    ("Rahul",   "FullTime", 68000),
    ("Pooja",   "FullTime", 73000),
    ("Amit",    "PartTime", 26000),
    ("Kavya",   "FullTime", 88000),
    ("Nitin",   "FullTime", 62000),
    ("Sneha",   "PartTime", 34000),
    ("Rohit",   "FullTime", 77000),
    ("Isha",    "PartTime", 31000),
    ("Manoj",   "FullTime", 56000),
    ("Tanvi",   "PartTime", 29000),
]

FullTime_salary=0
Parttime_salary=0
n_fulltime=0
n_parttime=0

for i in employees:
    name, emp_type, salary = i
    if emp_type == "FullTime":
        n_fulltime += 1
        FullTime_salary += salary
    else:
        n_parttime += 1
        Parttime_salary += salary

avg_fulltime_salary = FullTime_salary / n_fulltime
avg_parttime_salary = Parttime_salary / n_parttime
d={"FullTime": avg_fulltime_salary, "PartTime": avg_parttime_salary}
print(d)