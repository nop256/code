from cisc108 import assert_equal

def get_front_of_weekdays(day):
    day.lower().replace("day", "")
    if day in ["mon", "tues", "wed", "thurs", "fri"]:
        return day
    else:
        return "weekend"

assert_equal(get_front_of_weekdays("Monday"), "Mon")
assert_equal(get_front_of_weekdays("sunday"), "weekend")
assert_equal(get_front_of_weekdays("friday"), "fri")
