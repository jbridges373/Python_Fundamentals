# def served_order(orders):
#     if len(orders) == 0:
#         print("There are no orders to serve.")
#         return
    
#     item = orders.pop(0)
#     print(f"Now serving: {item}")

# served_order([])

# def filled_order(menu, order):
#     if len(order) == 0:
#         print("Nothing available.")
#         return
    
#     if order not in menu:
#         print(f"{order} is not on the menu.")
#         return

#     menu.remove(order)
#     print(f"Order placed: {order}")

# Challenge: Call the Next Guest
# call_next() seats the first guest on a restaurant's waitlist. But when the waitlist is empty, the
# app crashes.

waitlist = []

def call_next(waitlist):
    """Seat the first guest on the waitlist."""
    # 1. Guard clause: checks if the list is empty and exits early
    if len(waitlist) == 0:
        print("The waitlist is currently empty!")
        return  # Exits the function immediately
        
    name = waitlist[0]
    print(f"Now seating: {name}")

# 2. Test it with an empty waitlist to confirm it no longer crashes.
call_next(waitlist)