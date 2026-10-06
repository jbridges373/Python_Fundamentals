## Challenge: Move a Singer to the Top of the Queue
 
Moving a singer to the top is two steps:
1) take them out of their current position, and
2) insert them at the beginning of the queue.
 
1. Write move_to_top(queue):
    - Ask the host which position they want to move, and convert their answer to a number
    - Take that singer out of the queue with .pop(). Watch for an off-by-one error: the queue starts
    at 1 for the host, but Python starts counting at 0, so position 1 is
    index 0. Pass the host's number minus one as the argument to .pop()
    - Put the singer back at the front of the queue with .insert()
    - Print a message announcing who moved to the top
 
2. Call move_to_top in the app loop so the host can run the command, and add "top" to the Options menu.
 
Here's what your output should look like:
 
Current Queue:
 
1. Annie - Dancing Queen
2. Allen - Country Roads
 
Options: add / next / top / remove / quit
> top
 
Who do you want to move to the top? Enter a number: 2
 
Moved Allen to the top of the queue!
 
Current Queue:
