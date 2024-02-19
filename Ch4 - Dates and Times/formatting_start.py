#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime

def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes 
    now = datetime.now()

    
    #### Date Formatting ####
    
    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    # a versão minúscula é encurtada e a maiúscula é completa
    print(now.strftime("the current year is: %Y"))
    print(now.strftime("the current year is: %Y"))
    print(now.strftime("hoje é %d de %B de %Y, dia da semana: %A" ))

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("Locale date and time: %c, locale date %x, locale time %X"))

    #### Time Formatting ####
    
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("24h time: %H:%M"))


if __name__ == "__main__":
    main()
