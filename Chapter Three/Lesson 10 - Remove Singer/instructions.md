Challenge: Remove a Singer
Find the singer in the queue and remove them.

In the remove_singer() function:

1. Prompt the host for who to remove. Clean the input: title-cased, no extra spaces.
2. Loop through the queue looking for a matching singer name. Each singer is a (name, song) tuple,
so compare against the name inside the tuple rather than the tuple itself. Check hints.md
if you need help!
3. If you find a match, remove the whole tuple with .remove(), print a confirmation and return.
4. If the loop finishes without a match, print a message telling the host no match was found.

Example output:

remove

Who do you want to remove? allen

Removed Allen from the queue.

remove

Who do you want to remove? sarah

There's no one named Sarah in the queue.