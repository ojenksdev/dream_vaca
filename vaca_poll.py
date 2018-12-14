# Dream vacation program
# Polls users to see where they would like to visit in the world (or beyond)


vacation_poll = {}

# Flag to show the poll is active in the While loop
poll_active = True

while poll_active:
    # Prompt users for their name
    name = input("Hello, what is your name?: ")

    # Prompt users for their response
    response = input("\nWhere would you like to go? ")

    # Add this information to the vacation_poll dictionary
    vacation_poll[name] = response

    # See if anyone else would like to take the poll
    more_users = input("Would anyone else like to take the poll? (yes/no)")
    if more_users == 'no':
        poll_active = False

# Print poll results to screen
print("\n=====Poll Results=====")
for name, response in vacation_poll.items():
    print(name.title() + " would like to visit " + response.title() + " someday.")

print("\nThanks for taking the poll!")
