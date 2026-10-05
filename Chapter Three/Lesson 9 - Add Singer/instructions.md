Challenge: Add a Singer
Adding a singer is two separate tasks: 1) prompt the host for a name and a song, and 2) append that singer to the queue. Write a function for each:

1. Write prompt_for_singer():
	• Ask the host for a name and a song
	• The function should return the name and the song title cased and stripped of any extra spaces
	• A function can return two values at once if you separate them with a comma:
    return name, song. You unpack them the same way you would a tuple.

2. Fill in the add_singer() function:
	• Call prompt_for_singer(), unpack what comes back, and save to variables
	• Add the singer and their song to the end of the queue
	• Print a message confirming the singer was added

Example output:

Current Queue:

Annie - Dancing Queen
Allen - Country Roads

Options: add / remove / quit
> add

Name: mike reed
Song: LET IT BE

Added Mike Reed to the queue.

Current Queue:

Annie - Dancing Queen