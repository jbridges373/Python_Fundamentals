queue = [
    ("Annie", "Dancing Queen"), 
    ("Bob", "Bohemian Rhapsody"), 
    ("Cathy", "Rolling in the Deep")
]


def show_queue(queue):
    """Display the current list of singers with sequential numbering."""
    print("\nCurrent Queue:\n")
    
    # enumerate() gives you a loop counter starting at 1 automatically
    for number, (singer, song) in enumerate(queue, start=1):
        print(f"{number}. {singer} - {song}")
        
    print("\nOptions: add / next / top / remove / quit")
  

# prompt for singer
def prompt_for_singer():
    """Prompt the user for a singer's name and song title."""
    singer_input = input("Enter the singer's name: ")
    song_input = input("Enter the song title: ")    

    # Strip spaces and fix casing (.title() capitalizes first letters)
    singer = singer_input.strip().title()
    song = song_input.strip().title()
    
    # Return two values at once
    return singer, song

# Stub add_singer and remove_singer with one-sentence docstrings
def add_singer(queue):
    """Add a new singer to the back of the queue."""
    # Call prompt_for_singer(), unpack what comes back, and save to variables
    name, song = prompt_for_singer()

    # Add the singer and their song as a tuple to the end of the queue
    queue.append((name, song))

    # Print a message confirming the singer was added
    print(f"\nAdded {name} to the queue.")

# Write next_singer(queue)
def next_singer(queue):
    """Take the singer off the front of the queue and announce them."""
    # Check if the queue is empty first to prevent crashing
    if not queue:
        print("\nThe queue is empty! No one is up next.")
        return

    # Take the singer off the front of the queue using .pop(0) and save it
    # Note: .pop() defaults to the end, .pop(0) removes from the front (index 0)
    current_act = queue.pop(0)
    
    # Unpack that singer tuple into name and song variables
    name, song = current_act
    
    # Announce that they're next
    print(f"\nNOW UP: {name} - {song}")

# Write move_to_top(queue)
def move_to_top(queue):
    """Move a singer from their current position to the front of the queue."""
    # Check if the queue is empty first
    if not queue:
        print("\nThe queue is empty! No one to move.")
        return

    # Ask the host which position to move and convert it to a number
    position_input = input("Who do you want to move to the top? Enter a number: ")
    
    # Simple check to make sure the input is a valid number inside our queue range
    if not position_input.isdigit():
        print("Please enter a valid number.")
        return
        
    position = int(position_input)
    
    if position < 1 or position > len(queue):
        print(f"Invalid position. Please pick a number between 1 and {len(queue)}.")
        return

    # Convert host position (1-indexed) to Python index (0-indexed) by subtracting 1
    python_index = position - 1
    
    # Take that singer out of the queue with .pop()
    moved_singer = queue.pop(python_index)
    
    # Put the singer back at the front of the queue (index 0) with .insert()
    queue.insert(0, moved_singer)
    
    # Unpack the name from the tuple just for the confirmation message
    singer_name, _ = moved_singer
    print(f"\nMoved {singer_name} to the top of the queue!")

def remove_singer(queue):
    """Find a specific singer by name in the queue and remove them."""
    # Prompt the host and clean the input
    target_name = input("Who do you want to remove? ").strip().title()
    
    # Loop through the queue and unpack the (name, song) tuples
    for number, (singer_name, song_title) in enumerate(queue, start=1):
        # Compare against the name inside the tuple
        if singer_name == target_name:
            # 3. If found, remove the whole tuple item, confirm, and exit the function
            queue.pop(number - 1)
            print(f"\nRemoved {target_name} from the queue.")
            return

    # If the loop finishes without hitting 'return', no match was found
    print(f"\nThere's no one named {target_name} in the queue.")



def run_app(queue):
    print("============================================")
    print("Welcome to Sing Out: A Karaoke Queue Manager")
    print("============================================")
    
    while True:
        show_queue(queue)        
        command = input("> ").strip().lower()
        
        # Finish the if/elif/else chain to call matching functions
        if command == "quit":
            print("\nGoodbye!")
            break
        elif command == "add":
            add_singer(queue)
        elif command == "next":
            next_singer(queue)
        elif command == "top":
            move_to_top(queue)    
        elif command == "remove":
            remove_singer(queue)
        
        # Add an else to handle unrecognized commands without crashing
        else:
            print(f"\nSorry, I don't know the command '{command}'.")


# Initialize an empty queue list
# queue = []

# Call run_app(queue) to test the application
run_app(queue)
