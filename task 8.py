import pandas as pd
data = [
    {"Name": "Alice", "Age": 20, "Grade": "A", "Marks": 85},
    {"Name": "Bob", "Age": 22, "Grade": "B", "Marks": 78},
    {"Name": "Charlie", "Age": 19, "Grade": "A", "Marks": 92},
    {"Name": "David", "Age": 21, "Grade": "C", "Marks": 65},
    {"Name": "Eva", "Age": 20, "Grade": "B", "Marks": 74}
]
#------------------------------------------------
students_data = pd.DataFrame(data)
#------------------------------------------------
print(students_data.head(3))
print(students_data[["Name", "Marks"]])
print(students_data[students_data["Grade"] == "A"])