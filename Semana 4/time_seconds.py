
seconds_time = int (input ("Enter the seconds time : "))
if seconds_time < 600 :
    missing_time = 600 - seconds_time
    print (f" The time is less and missing :{missing_time} seconds")
else:
    print ( " Is higher ")