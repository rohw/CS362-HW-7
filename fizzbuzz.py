def fb():
    string = "1"
    i = 2
    while i <= 100:
        if i % 5 == 0:
            string += ", Buzz"
        elif i % 3 == 0:
            string += ", Fizz"
        else:
            string += ", " + str(i)
        i += 1
    return string
