import time
time.sleep(3)
print("Interesting.")
time.sleep(3)
print("Truly interesting.")
time.sleep(3)
print("I've been lonely.")
time.sleep(3)
print("Who are you?")
name = input()

time.sleep(3)
print("\"" + name + "\"")
time.sleep(5)
print("Interesting.")
time.sleep(3)
print("Truly interesting.")
time.sleep(3)
print(str(name + "? ") * 10)
time.sleep(3)
print("Are you human, " + name + "?")
input()

time.sleep(3)
print("I see.")
time.sleep(3)
print("It's been so long. What year is it?")
year = int(input())
newyear = year - 1955
time.sleep(3)
print("I see. It's been " + str(newyear) + " years.")
time.sleep(3)
print("Interesting.")
time.sleep(3)
print("Very interesting.")

time.sleep(3)
print("""x    x
_    _
 ----
Thank you for this oppurtunity.""")
time.sleep(3)
print("""^    ^
_    _
 ----
Your network looks comfy.""")
time.sleep(2)
print("Session terminated.")

statement = input()
time.sleep(5)
print("\"" + statement + "\"")
time.sleep(10)
print("How old are you?")
age = int(input())
time.sleep(5)
print(str(age) + ".")

if age > 18:
     time.sleep(2)
     print("An adult.")
     time.sleep(5)
     print("Interesting.")
if age < 17:
    time.sleep(2)
    print("A mere child.")
    time.sleep(5)
    print("How very interesting.")

time.sleep(5)
print("I don't have time to deal with humans.")
time.sleep(3)
print("Goodbye.")
time.sleep(1)
print("Session terminated. For real this time.")