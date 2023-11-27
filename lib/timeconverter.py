def time_convert():
    # The user is asked to provide the time using this format 'hh:mm am/pm'
    timeStr = input("Enter the time in the format 'hh:mm am/pm': ")
    
    # The time is split into two parts
    splitTime = timeStr.split(" ")
    
    # The time is split into hours and minutes
    splitRealTime = splitTime[0].split(":")
    
    # The hour is converted to an integer 
    toInt = int(splitRealTime[0])
    
    # Case examples to convert the time
    if splitTime[1] == "am" and toInt == 12:
        # Convert 12:00 am to 00:00 hrs
        formatted_time = "00" + ":" + splitRealTime[1]
    elif splitTime[1] == "pm" and toInt < 12:
        # Convert afternoon time by adding 12 hours
        toInt += 12
        formatted_time = str(toInt).zfill(2) + ":" + splitRealTime[1]
    else:
        # Keep times in 24-hour format unchanged
        formatted_time = str(toInt).zfill(2) + ":" + splitRealTime[1]
        
    # Display the formatted time
    print(f"Converted time: {formatted_time}")
    return formatted_time

# Call the time_convert function to initiate the time conversion
time_convert()