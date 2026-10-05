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


# 1. Stub add_singer and remove_singer with one-sentence docstrings
def add_singer(queue):
    """Add a new singer to the back of the queue."""
    print("\n[add a singer]")


def remove_singer(queue):
    """Remove the next singer from the front of the queue."""
    print("\n[remove a singer]")


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
