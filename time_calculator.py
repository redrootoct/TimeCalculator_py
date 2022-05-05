def add_time(input1, input2, useWeekdays = False):

    #Process inputs
    ###############

    whole_current_time = input1.split()

    current_time = whole_current_time[0].split(":")

    current_time_of_day = whole_current_time[1]

    if current_time_of_day == "PM":
        if current_time[0] != "12": #if hour is not 12, sum 12 to hour, otherwise leave hour as it is
            int_current_time_hour = int(current_time[0])
            int_current_time_hour += 12
            current_time[0] = str(int_current_time_hour)

    if current_time_of_day == "AM" and current_time[0] == "12": #if it is 12AM, convert it to 0
        current_time[0] = "00"

    time_to_add = input2.split(":")

    #Do calculation
    ###############

    #Calculate minutes

    minutes_sum = int(time_to_add[1]) + int(current_time[1])

    if minutes_sum >= 60:
        minute_diff = minutes_sum - 60
        minutes = minute_diff
        hours_to_add = 1
    else:
        minutes = minutes_sum
        hours_to_add = 0

    #Calculate hour

    hour_sum = int(time_to_add[0]) + int(current_time[0]) + hours_to_add
    if hour_sum >= 24:
        extra_days_int = hour_sum // 24
        hour = hour_sum - 24 * extra_days_int
    else:
        hour = hour_sum
        extra_days_int = 0

    #Calculate weekdays

    if useWeekdays != False:
        useWeekdays = useWeekdays.lower()
        if useWeekdays == "monday":
            start_weekday_number = 1
        elif useWeekdays == "tuesday":
            start_weekday_number = 2
        elif useWeekdays == "wednesday":
            start_weekday_number = 3
        elif useWeekdays == "thursday":
            start_weekday_number = 4
        elif useWeekdays == "friday":
            start_weekday_number = 5
        elif useWeekdays == "saturday":
            start_weekday_number = 6
        elif useWeekdays == "sunday":
            start_weekday_number = 7

        weekday_number = (start_weekday_number + extra_days_int) % 7

        if weekday_number == 1:
            weekday = "Monday"
        elif weekday_number == 2:
            weekday = "Tuesday"
        elif weekday_number == 3:
            weekday = "Wednesday"
        elif weekday_number == 4:
            weekday = "Thursday"
        elif weekday_number == 5:
            weekday = "Friday"
        elif weekday_number == 6:
            weekday = "Saturday"
        elif weekday_number == 0:
            weekday = "Sunday"

    #Formatting time to string

    def timeNumberFormat(n) :
        if n < 10:
            return "0{}".format(n)
        else:
            return "{}".format(n)

    if hour >= 12:
        rest = 24 - hour
        hour = 12 - rest
        time_of_day = "PM"

        if hour == 12: #if time is 24 then it should be 12 AM
            time_of_day = "AM"
        if hour == 0:  #if hour is 12 then it should be 12 PM
            hour = 12

    else:
        time_of_day= "AM"
        if hour == 0: #if hour is 00 then it should be 12 AM
            hour = 12

    formatted_hour = str(hour)
    formatted_minutes = timeNumberFormat(minutes)
    formatted_extra_days = str(extra_days_int)

    #print

    if extra_days_int == 0:
        if useWeekdays == False:
            new_time = formatted_hour+":"+formatted_minutes+" "+time_of_day
        else:
            new_time = formatted_hour + ":" + formatted_minutes + " " + time_of_day+", "+weekday
    else:
        if useWeekdays == False:
          if extra_days_int == 1:
            new_time = formatted_hour+":"+formatted_minutes+" "+time_of_day+" (next day)"
          else:
            new_time = formatted_hour+":"+formatted_minutes+" "+time_of_day+" ("+formatted_extra_days+" days later)"
        else:
          if extra_days_int == 1:
             new_time = formatted_hour + ":" + formatted_minutes + " " + time_of_day + ", " + weekday+ " (next day)"
          else:
             new_time = formatted_hour + ":" + formatted_minutes + " " + time_of_day + ", " + weekday+ " (" +formatted_extra_days + " days later)"

    return new_time
