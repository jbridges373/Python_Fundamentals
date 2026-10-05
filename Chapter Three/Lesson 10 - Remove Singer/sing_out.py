queue = [
    ("Annie", "Dancing Queen"), 
    ("Bob", "Bohemian Rhapsody"), 
    ("Cathy", "Rolling in the Deep")
]


def show_queue(queue):
    """Display the current list of singers."""
    print("\nCurrent Queue:\n")    
    for singer, song in queue:
        print(f"{singer} - {song}")    
    print("\nOptions: add / remove / quit")  

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

# 1. Stub add_singer and remove_singer with one-sentence docstrings
def add_singer(queue):
    """Add a new singer to the back of the queue."""
    # Call prompt_for_singer(), unpack what comes back, and save to variables
    name, song = prompt_for_singer()

    # Add the singer and their song as a tuple to the end of the queue
    queue.append((name, song))

    # Print a message confirming the singer was added
    print(f"\nAdded {name} to the queue.")

def remove_singer(queue):
    """Find a specific singer by name in the queue and remove them."""
    # 1. Prompt the host and clean the input
    target_name = input("Who do you want to remove? ").strip().title()
    
    # 2. Loop through the queue and unpack the (name, song) tuples
    for item in queue:
        singer_name, song_title = item  # Unpack the tuple
        
        # Compare against the name inside the tuple
        if singer_name == target_name:
            # 3. If found, remove the whole tuple item, confirm, and exit the function
            queue.remove(item)
            print(f"\nRemoved {target_name} from the queue.")
            return

    # 4. If the loop finishes without hitting 'return', no match was found
    print(f"\nThere's no one named {target_name} in the queue.")


def run_app(queue):
    print("============================================")
    print("Welcome to Sing Out: A Karaoke Queue Manager")
    print("============================================")
    
    while True:
        show_queue(queue)        
        command = input("> ").strip().lower()
        
        # 2. Finish the if/elif/else chain to call matching functions
        if command == "quit":
            print("\nGoodbye!")
            break
        elif command == "add":
            add_singer(queue)
        elif command == "remove":
            remove_singer(queue)
        # 3. Add an else to handle unrecognized commands without crashing
        else:
            print(f"\nSorry, I don't know the command '{command}'.")


# Initialize an empty queue list
# queue = []

# 4. Call run_app(queue) to test the application
run_app(queue)
