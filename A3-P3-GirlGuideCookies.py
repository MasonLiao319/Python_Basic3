#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:     w0424837
#Student Name:  Mason Liao

 #  CODE STARTS HERE

# Function to calculate the average number of boxes sold per guide
def averageBox(p_number_of_box,p_number_of_guides):
    total_boxes = sum(p_number_of_box)
    guides = len(p_number_of_guides)
    return total_boxes / guides


# Function to print a line with a specified character and length
def printALine(p_char,p_length):
    print(p_char * p_length)


# Main function to gather and analyze data on boxes sold by guides
def main():
    # Let the user to enter the number of guides selling cookies
    guide_sell_cookie = int(input("Enter the number of guides selling cookies: "))

    # Initialize lists to store names of guides and the number of boxes sold
    name_of_guides = []
    number_of_boxes = []

    # Collect information on each guide, including name and number of boxes sold
    for counter in range(1,guide_sell_cookie + 1):
        name_of_guides.append(input("\nEnter the name of guide: #{0}: ".format(counter)))
        number_of_boxes.append(int(input("Enter the number of boxes sold by {0}: ".format(name_of_guides[counter - 1]))))

    # Call the averageBox function to calculate and display the average number of boxes sold    
    avarage_boxes_sold = averageBox(number_of_boxes,name_of_guides)
    print("\nThe average number of boxes slod by each guide was {0:.1f} ".format(avarage_boxes_sold))

    # Determine and display the prize won by each guide based on their sales performance
    prizes_won = []
    for counter in range(len(name_of_guides)):
        if number_of_boxes[counter] == max(number_of_boxes):
            prize = "Trip to Girl Guide Jamboree in Aruba!"
        elif averageBox(number_of_boxes,name_of_guides) <= number_of_boxes[counter] < max(number_of_boxes):
            prize = "Supe Seller Badge"
        elif 1 < number_of_boxes[counter] < averageBox(number_of_boxes,name_of_guides):
            prize = "Left over cookies"
        elif number_of_boxes[counter] == 0:
            prize = " "
        prizes_won.append(prize)

    # Display a table showing each guide and the prize they won
    print("\nGuide","\t\t","Prize won:")
    printALine("-",60)
    for counter in range(len(name_of_guides)):
        print(name_of_guides[counter],"\t\t-" ,prizes_won[counter])
            

    # Ready for Marking
    
    # YOUR CODE ENDS HERE

main()