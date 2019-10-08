print("How far are we from the cave?")
distance = int(input())

for count in range (distance, 0, -1):
    print(distance, "steps remaining")
    distance = distance - 1

print("We have reached the cave!")