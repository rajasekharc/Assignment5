from datetime import datetime

print("""Enter Timestamp in this format: Day dd Mon yyyy hh:mm:ss +xxxx \n
    Day is Weekday as abbreviated name
    dd is Day of the month as a zero-padded decimal number
    Mon is Month as abbreviated name
    yyyy is Year with century as a decimal number
    hh is Hour (24-hour clock) as a zero-padded decimal number
    mm is Minute as a zero-padded decimal number
    ss is Second as a zero-padded decimal number
    +xxxx is UTC offset in the form +HHMM or -HHMM)""")

try:
    t1=datetime.strptime(input("Enter Timestamp1: "),"%a %d %b %Y %H:%M:%S %z")
    t2=datetime.strptime(input("Enter Timestamp2: "),"%a %d %b %Y %H:%M:%S %z")
    print(abs((t2-t1).total_seconds()))

except ValueError:
    print("Provide Timestamp in the fixed way as shown above")
