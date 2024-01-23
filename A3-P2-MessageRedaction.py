#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:     w0424837
#Student Name:  Mason Liao


# CODE STARTS HERE 

# Function to convert all letters in a list to lowercase
def lower_case_list(p_list):
    return [letter.lower() for letter in p_list]

def main():
   
    # Continue taking input until the user decides to quit
    while True:
        user_phrase = input("Type a phrase (or quit to exit program): ")
        if user_phrase.lower() == "quit":
            break
        
        # Let the user to enter a comma-separated list of letters to redact
        comma_separated_list = input("\nType a comma-separated list of letters to redact: ").split(",")

        # Convert the list of letters to lowercase using the defined function
        comma_separated_list = lower_case_list(comma_separated_list)

        # Initialize a variable for the number of redacted letters
        num_removed = 0

        # Count and display the number of redacted letters in the phrase
        for letter in comma_separated_list:
            num_removed += user_phrase.lower().count(letter)
        print("Number of letters redacted: {0}".format(num_removed))

        # Redact the specified letters in the user's phrase with underscores
        for letter in comma_separated_list:
        # Replace both uppercase and lowercase
            user_phrase = user_phrase.replace(letter.upper(), "_").replace(letter.lower(), "_")
        print("Redacted phrase: {0}\n".format(user_phrase))


    # Ready for Marking
    
    # YOUR CODE ENDS HERE

main()