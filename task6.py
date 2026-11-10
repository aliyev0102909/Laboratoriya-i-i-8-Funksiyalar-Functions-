def average(*numbers):
    return sum(numbers) / len(numbers) if numbers else 0
def make_course(code, **details):
    details["code"] = code
    return details
print(average(70, 80, 90))
print(average(100))
print(average())
print(make_course("CE101", title="Fundamentals of Programming", credits=6))
