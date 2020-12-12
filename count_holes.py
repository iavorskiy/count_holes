
b = input("Enter the number to count the holes: \n")
def count_holes(b):

    if type(b) != int and type(b) != str:
        return("ERROR")
        try:
            int(b)
        except ValueError:
            return "ERROR"
    c = str(b)
    counter = 0
    for x in c:
        if x in "0469":
            counter += 1
        elif x == "8":
            counter += 2

    return counter

print(count_holes(b))

