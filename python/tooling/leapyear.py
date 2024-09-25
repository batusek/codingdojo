def isLeapYear(year):
    # After start
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

    return False
    # After end
    # Uncomment:    return True