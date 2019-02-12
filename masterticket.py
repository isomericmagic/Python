"""
Let us pretend that all of the remaining cast members of the comedy group,  Monty Python, are going to get together and do a question and answer session.  
They're gonna be discussing what it's like for them as a comedy group, to have jokes that they made over three decades ago still referenced in Python tutorials 
and code examples. Now, let's also imagine, since they're funny like this, that they want to have the only way that you can buy tickets, is through a single python script. 
No website, no app. Just a single console app. You can only buy tickets using a command line program where no one would expect it. Spain, in a cheese shop. 
You've been tasked with writing that program. Sound fun? There are some very specific instructions and I've gone and captured them for us in Trello.  

Let's walk through the product requirements:

As a user, I should be shown the number of tickets left remaining, so I can understand the importance of buying now. (That makes sense...gotta give them a little bit of FOMO.)

As a user, I should have a personalized experience so that I feel welcome by the brand. (Cool, I'll have to get to know what their name is right?)

As a user, I should have errors reported in a user friendly manner.

As a user, I should be able to request a certain amount of tickets and be told the total cost.

As a user, I should be able to confirm my order so that I do not accidentally purchase more tickets than intended.

As a user I should not be offered tickets if they're aren't any available, that would be horrible.

And finally, as an owner, I should receive a service charge for each transaction so I can pay others to maintain the software.
"""
TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100  

#function to calculate total ticket price (num tickets * price + service fee)
def calculate_price(number_of_tickets):
  return (int(requested_tickets) * TICKET_PRICE) + SERVICE_CHARGE

#run this code continuously while there are tickets remaining
while tickets_remaining > 0:  
  #output how many tickets are remaining using the tickets_remaining variable
  print("There are currently {} tickets available.".format(tickets_remaining))  
  #gather the user's name and assign it to a new variable
  user_name = input("Please enter your name:  ")  
  #prompt the user by name and ask them how many tickets they want to buy, and handle value error
  try:
    requested_tickets = int(input("Hi {}, how many tickets would you like to purchase today?".format(user_name)))
    # Raise a value error if the number of tickets requested is greater than the number available or less than one
    if requested_tickets > tickets_remaining:
      raise ValueError("There aren't that many tickets remaining, we only have {} left.".format(tickets_remaining))
    if requested_tickets < 1:
      raise ValueError("You must request at least 1 ticket.")  
  except ValueError as err:
    print("Invalid number of tickets requested ({}). Please try again.".format(err))
  else:
    #calculate the total price and assign it to a variable
    total_price = calculate_price(requested_tickets)  
    #output price to screen
    print("Thanks, {} your total is ${}.".format(user_name, total_price))  
    #prompt user if they want to proceed (Y/N)?
    purchase_confirmation = input("Please confirm you would like to make this purchase now (Y/N): ")
    
    #if user confirms they want to proceed
    if purchase_confirmation.upper() == "Y":    
        #print out SOLD! to confirm their purchase
        print("SOLD!")      
        #decrementthe tickets remaining by the number they purchased
        tickets_remaining -= requested_tickets      
    #otherwise thank them by name
    else:
        print("Perhaps another time then...Thanks, {}!".format(user_name))
      
#notify user tickets are sold out
print("Sorry there are no more tickets available.")