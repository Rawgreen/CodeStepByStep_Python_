
def enough_time_for_lunch(hour1, minute1, hour2, minute2):

    if (hour2 - hour1) < 0:
        return False

    elif (hour2 - hour1) > 1:
        return True

    elif (hour2 - hour1) == 1:

        if (minute2 + 60 - minute1) < 45:
            return False

        else:
            return True

    else:
        if (minute2 - minute1) < 45:
            return False

        else: return True
            
    