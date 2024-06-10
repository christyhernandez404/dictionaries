import os
import time


service_tickets = {
    1: {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    2: {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}


def next_id():  
    last_id = 0
    for id in service_tickets.keys():
        if id > last_id:
            last_id = id
    return last_id + 1

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def open_ticket():
    new_id = next_id()
    while True:
        customer = input("Whats your name? ")
        issue = input("Describe the issue: ")
        status = 'open'
        print(f"Customer:{customer}, Issue:{issue}, Status:{status}")
        correct = input("Is this information accurate? y/n")
        if correct == 'y':
            service_tickets[new_id] = {
                "Customer": customer, 'Issue': issue, 'Status': status}
            print(f"Your ticket has been created: ID: {new_id}, Customer: {service_tickets[new_id]['Customer']}, Issue: {service_tickets[new_id]['Issue']}, Status: {service_tickets[new_id]['Status']}")
            break
        else:
            continue


def update_ticket():
    print("\nPlease view tickets first to see which ticket number you'd like to update")
    ticket_id = int(input("Enter the ticket number you'd like to update:"))
    if ticket_id not in service_tickets:
        print("Invalid ticket ID")
        return
    what_to_update = input(
        "Would you like to update the customer or the issue? customer/issue: ")
    if what_to_update == 'customer':
        new_customer = input("What should the customer name be?")
        service_tickets[ticket_id]['Customer'] = new_customer
        print(f"The ticket has been updated: ID: {ticket_id}, Customer: {service_tickets[ticket_id]['Customer']}, Issue: {service_tickets[ticket_id]['Issue']}, Status: {service_tickets[ticket_id]['Status']}")
    elif what_to_update == 'issue':
        new_issue = input("What should the issue be?")
        service_tickets[ticket_id]['Issue'] = new_issue
        print(f"The ticket has been updated: ID: {ticket_id}, Customer: {service_tickets[ticket_id]['Customer']}, Issue: {service_tickets[ticket_id]['Issue']}, Status: {service_tickets[ticket_id]['Status']}")
    else:
        print("Invalid option")


def view_tickets():
    print("These are the tickets:")
    for ticket_id, ticket_info in service_tickets.items():
        print(f"ID: {ticket_id}, Customer: {ticket_info['Customer']}, Issue: {
              ticket_info['Issue']}, Status: {ticket_info['Status']}")

        # why to reference the items it's curly braces and then a square brackets inside


def main():  # Hold the main functionality of my app
    while True:
        ans = input('''
Welcome to IT Support! What would you like to do?
                    
1 - Open a new service ticket
2 - Update the status of an existing ticket to "closed"
3 - Display all tickets
4 - Quit

Enter the corresponding number for the action you'd like to take here:''')
        if ans == '1':
            open_ticket()
            time.sleep(5)
            clear()
        elif ans == '2':
            update_ticket()
            time.sleep(5)
            clear()
        elif ans == '3':
            view_tickets() 
            time.sleep(5)
            clear()
        elif ans == '4':
            print("Thanks for using our app!")
            break
        else:
            print("Invalid data entry")


main()
