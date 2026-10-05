Hints: Remove a Singer

Each singer in the queue is a `(name, song)` tuple rather than a plain string:

queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]

Comparing `singer == name` will never match because `singer` represents the entire tuple.

You can access the name in the tuple directly with indexing, where `singer[0]` is the name and `singer[1]` is the song. You can use indexing when you only need to get one element out of the tuple, like to search for a matching name:

    if singer[0] == name:
    
Unpack the tuple when you need to use both elements:

    singer_name, song = singer
    if singer_name == name:
        print(f"{singer_name} is here to sing {song}")

Once you find the matching singer, pass the entire tuple to `.remove()`:

    queue.remove(singer)
