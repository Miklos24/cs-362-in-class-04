def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False
            
if __name__ == "__main__":
    print("Please enter a year:")
    year = int(input())
    if isLeapYear(year):
        print(year, "is a leap year!")
    else:
        print(year, "is not a leap year.")
