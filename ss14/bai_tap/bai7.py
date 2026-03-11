students = (
    ("An", 8.5),
    ("Bình", 7.0),
    ("Chi", 9.2)
)
for i in students:
    print(i)
    
for name, point in students:
    print(name, point)

max = 0
for name, point in students:
    if point >= max:
        max = point
print(max)