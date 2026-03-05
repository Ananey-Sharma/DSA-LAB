class Ticket:
    def __init__(self, customer_name, issue, priority=False):
        self.customer_name = customer_name
        self.issue = issue
        self.priority = priority


class TicketingSystem:
    def __init__(self):
        self.ticket_queue = []

    def submit_ticket(self, ticket):
        if ticket.priority:
            self.ticket_queue.insert(0, ticket)
        else:
            self.ticket_queue.append(ticket)

    def process_ticket(self):
        if self.ticket_queue:
           return self.ticket_queue.pop(0)
        else:
            return None

    def display_tickets(self):
        if self.ticket_queue:
            print("Current Tickets:")
            for i in range(len(self.ticket_queue)):
                ticket = self.ticket_queue[i]
                print(f"{i+1}. Customer: {ticket.customer_name}, Issue: {ticket.issue}, Priority: {ticket.priority}")
        else:
            print("No tickets currently in the queue.")

ticketing_system = TicketingSystem()

while True:
    print("\n1. Submit Ticket")
    print("2. Process Ticket")
    print("3. Display Tickets")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        customer_name = input("Enter customer name: ")
        issue = input("Enter issue: ")
        priority = input("Is this a priority ticket? (yes/no): ").lower() == 'yes'
        ticket = Ticket(customer_name, issue, priority)
        ticketing_system.submit_ticket(ticket)
        print("Ticket submitted successfully!")

    elif choice == '2':
        processed_ticket = ticketing_system.process_ticket()
        if processed_ticket:
            print(f"Processed Ticket - Customer: {processed_ticket.customer_name}, Issue: {processed_ticket.issue}, Priority: {processed_ticket.priority}")
        else:
            print("No tickets to process.")
    
    elif choice == '3':
        ticketing_system.display_tickets()

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")

