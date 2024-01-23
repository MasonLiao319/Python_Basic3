#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:     w0424837
#Student Name:  Mason Liao


# CODE STARTS HERE

# Function to print a line with a specified character and length
def printALine(p_char,p_length):
    print(p_char * p_length)

# Function to calculate the average number of hours worked per day
def averageHour(p_hoursWorked,p_workDays):
    total = sum(p_hoursWorked)
    days = len(p_workDays)
    return total / days

# Main function to gather and analyze work hours data
def main():
    # Define work days
    work_days = [1,2,3,4,5]

    # Collect hours worked data for each day
    hours_worked = []
    for counter in work_days:
        hours = float(input("Enter hours worked on Days #{0}: ".format(counter)))
        hours_worked.append(hours)

    # Print a line to separate sections in the output     
    printALine("-",70)

    # Determine the day(s) with the most hours worked and make the value(s) a list
    current_max = max(hours_worked)
    max_hour_day = []
    max_hour_value = []
    print("The most hours worked was on:")
    for counter in range(len(hours_worked)):
        if current_max == hours_worked[counter]:
            max_hour_day.append(counter + 1)
            max_hour_value.append(hours_worked[counter])

    # Display the day(s) with the most hours worked
    for counter in range(len(max_hour_day)):
        print("Day#{0} when you worked {1} hours".format(max_hour_day[counter],max_hour_value[counter]))
   
    # Print a line
    printALine("-",70)

    # Calculate and display total and average hours worked
    average_hours = averageHour(hours_worked,work_days) 
    print("The total number of hours worked was: {0}\nThe average number of hours worked each day was: {1}".format(sum(hours_worked),average_hours))

    # Print a line
    printALine("-",70)

    # Identify and display days with less than 7 hours worked
    print("Days you slack off (i.e. worked less than 7 hours):")
    slacked_of_hours = []
    slacked_of_day = []
    sufficient_hour_standard = 7

    for counter in range(len(work_days)):
        if hours_worked[counter] < sufficient_hour_standard:
            slacked_of_hours.append(hours_worked[counter])
            slacked_of_day.append(work_days[counter])

    # Display the results
    for counter in range(len(slacked_of_day)):
        print("Day #{0}: {1} hours".format(slacked_of_day[counter],slacked_of_hours[counter]))
    

    
    # Ready for Marking

    # YOUR CODE ENDS HERE

main()