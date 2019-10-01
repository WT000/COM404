# Asking what activity should be performed
# If "calculate" it will calculate, if not it will give a generic answer
print("Please enter the activity to be performed.")
activity = str(input())
if (activity == "calculate"):
    print("Performing calculations...")
else:
    print("Performing activity...")
print("Activity completed!")