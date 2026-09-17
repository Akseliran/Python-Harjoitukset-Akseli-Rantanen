#li = [2,3,2,6,7,3,3]
#li1 = list(set(li))
#print(li1)
#hedelmat = {"Omena", "appelsiini", "vesimeloni"}
#print("Omena" in hedelmat)
students = [
    {"name" : "Ella", "age":14, "grade": "9"},
    {"name" : "Leo", "age":15, "grade": "8"},
    {"name" : "Aino", "age":14, "grade": "10"}
    ]
for i in students:
    dict(i)
    print(f'{i["name"]}:n arvosana on {i["grade"]}')
