def ly(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return "It is not a leap year"
        else:
            return "It is a leap year"
    else:
        return "It is not a leap year"
