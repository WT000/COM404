# Asking if the book cover is hard or soft.
print("Does the book have a soft or hard cover?")
book_cover = input()

if (book_cover == "soft"):
    print("Is the book perfect-bound?")
    perfect_bound = input()
    if (perfect_bound == "yes"):
        print("Soft cover, perfect bound books are very popular!")
    elif (perfect_bound == "no"):
        print("Soft covers with coils or stiches are great for short books.")
elif (book_cover == "hard"):
    print("Books with hard covers can be more expensive!")
else:
    print("You didn't answer my question!")