#!/usr/bin/env python3
def convert_to_24_hour(hour, minute, period):

# Check the period then go on to output the right one
 if period == "pm" and hour != 12:
    hour += 12
 elif period == "am" and hour == 12:
    hour = 0
    # make changes on the output then print
 print( f"{hour:02d}{minute:02d} hrs")

convert_to_24_hour(9,21,'pm')