name = "Elizabeth"

subjects = ["English","Latin","History","Math","Science"]

print("Hello " + name)

print(subjects)

for i in subjects:
    print("One of my classes is " + i)

cities = ["London","Paris","Athens","New York City","Rome"]

for i in cities:
    if i == "Paris":
        print("Some of the most exquisite food is found in " + i)
    elif i == "New York City":
        print("One of the most exciting and busiest cities is " + i)
    elif i == "London": 
        print("I love traveling to " + i + " and seeing the double-decker buses ")
    else:
        print("I love traveling to " + i)

place = []

while True:
    print("What is a city you love? Type 'end' to quit.")
    answer = input().title()
    if answer == "End":
        break
    else:
        place.append(answer)

for i in place:
   if i in ["Italy","Europe","England","China","France","New York","Spain"]:
       print(i + " is not a city!")
   else:
       print("A city you love is " + i)
