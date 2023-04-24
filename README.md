# Lewis-Carroll-Word-Ladder

This program solves the Lewis Carroll word ladder puzzle. An example of the puzzle is going from the word head to tail --> {head, heal, teal, tell, tall, tail}
The program utilizes the priority queue class, a custom word class, a wordset and a Breadth-first search to solve the puzzle. 
Utilizing the breadth first search I add all permutations of the starting word that is given based on user input that are valid(in the wordset) to the priority queue.
I overloaded the < and == operators in the word class so that the next word popped from the priority queue is most similar to the second user inputted word which is the
target word the program tries to get to. I created this program after taking a data structures and algorithms course to reinforce what I learned.
