def make_student(name, score, group=""):
    d = {"name": name, "score": score}
    if group:
        d["group"] = group
    return d
print(make_student("Kamran", 61, "CE-101"))
students = []
while True:
    name = input("Name: ")
    if name == "quit":
        break
    score = int(input("Score: "))
    students.append(make_student(name, score))
for s in students:
    print(s["name"] + ": " + str(s["score"]))
