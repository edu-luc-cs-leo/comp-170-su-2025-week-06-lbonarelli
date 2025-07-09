
def load_to_list(filepath: str) -> list[float]:
    values = []
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                values.append(float(line))
    return values

def descriptive_statistics(source_data: list[float]) -> None:
    total = 0
    count = 0
    minimum = source_data[0]
    maximum = source_data[0]

    for temp in source_data:
        total += temp
        count += 1
        if temp < minimum:
            minimum = temp
        if temp > maximum:
            maximum = temp

    average = round(total / count, 2)

    print(f"There are {count} values in the data source.")
    print(f"The average value is {average}")
    print(f"The highest value is {maximum} and the smallest value is {minimum}")

def apply_markup(filepath: str) -> None:
    with open(filepath, "r") as file:
        for line in file:
            words = line.strip().split()
            output = []

            for word in words:
                if word.startswith("."):
                    output.append(word[1:].upper())
                elif word.startswith("_"):
                    output.append(" ".join(word[1:]))
                else:
                    output.append(word)

            print(" ".join(output))

#Reflection
# I was able to use clean structure and made sure that each function has a single return where needed.
# I tried to avoid complicating things and maintaing the the logic simple, especially in the formatting part where the markup was. 
# My stats function prints all values in a proper way and doesn’t use more than what is really needed.
# This HW compared to the other submissions I’ve done in the past weeks, I believe this code is easier to understand even though it took me some time as well.
# I can say now that with the class material I can better understand how to work with files, loops, and formatting text in Python.

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 

