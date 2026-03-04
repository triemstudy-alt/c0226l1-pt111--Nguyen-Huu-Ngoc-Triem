import converter as cv

print(f"Chuyển đổi sang km: {cv.km_to_miles(10)}")
print(f"Chuyển đổi sang độ f: {cv.celsius_to_fahrenheit(40)}")
print(f"Chuyển đổi sang m: {cv.miles_to_km(cv.km_to_miles(10))}")
print(f"Chuyển đổi sang độ c: {cv.fahrenheit_to_celsius(cv.celsius_to_fahrenheit(40))}")