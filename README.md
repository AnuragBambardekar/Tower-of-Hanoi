# The Tower of Hanoi

# Origin
The puzzle was invented by the French mathematician Édouard Lucas in 1883. Numerous myths regarding the ancient and mystical nature of the puzzle popped up almost immediately, including a myth about an Indian temple in Kashi Vishwanath containing a large room with three time-worn posts in it, surrounded by 64 golden disks. But, this story of Indian Kashi Vishwanath temple was spread tongue-in-cheek by a friend of Édouard Lucas.

If the legend were true, and if the priests were able to move disks at a rate of one per second, using the smallest number of moves, it would take them 264 − 1 seconds or roughly 585 billion years to finish, which is about 42 times the estimated current age of the universe.

There are many variations on this legend. For instance, in some tellings, the temple is a monastery, and the priests are monks. The temple or monastery may be in various locales including Hanoi, and may be associated with any religion. In some versions, other elements are introduced, such as the fact that the tower was created at the beginning of the world, or that the priests or monks may make only one move per day. ~ [Wikipedia]

# About the Problem
The **Tower of Hanoi** (also called The problem of **Benares Temple** or **Tower of Brahma** or **Lucas' Tower** and sometimes pluralized as Towers, or simply pyramid puzzle) is a classic puzzle or mathematical problem that involves moving a stack of disks from one peg or rod to another, subject to certain constraints. The puzzle consists of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle is usually represented as follows:

There are three **rods** (A, B, and C). <br>
There are n **disks** of different sizes, initially stacked in decreasing order of size on one rod (e.g., rod A).
The task is to move all the disks from the starting rod (e.g., rod A) to the destination rod (e.g., rod C), using the third rod (e.g., rod B) as an auxiliary, following these rules: <br>
**a. Only one disk can be moved at a time.** <br>
**b. A disk can only be placed on top of a larger disk or an empty rod.** <br>

# Solution
The puzzle is usually solved recursively. Here's a general algorithm for solving the Towers of Hanoi with n disks: <br>

- Move the top n-1 disks from the source rod (A) to the auxiliary rod (B) using the destination rod (C) as an auxiliary. <br>
- Move the largest disk from the source rod (A) to the destination rod (C). <br>
- Move the n-1 disks from the auxiliary rod (B) to the destination rod (C) using the source rod (A) as an auxiliary. <br>

This algorithm is applied recursively until all the disks are moved from the source rod to the destination rod. The key to solving the problem is understanding that you can break it down into smaller subproblems, solving them in the same way. <br>

The Towers of Hanoi puzzle is a classic example in computer science and recursion, often used to teach concepts like recursion and algorithmic thinking. The minimum number of moves required to solve the puzzle with n disks is 2^n - 1. <br>

This is the Time it would approximately take for moving the Tower of Hanoi by taking the optimal path, as the number of discs increase. <br>
![Time Complexity](Picture1.png) ~ [Source: Numberphile]

Look! I made a tower using Origami-boxes.
![Towers of Hanoi - Custom Made](PXL_20230819_170031992.jpg)

Sierpinski Triangle for 3 Discs. ~ [Source: Numberphile]
![Sierpinski Triangle](Picture2.png)

# Resources:

- https://www.youtube.com/watch?v=PGuRmqpr6Oo - The Key to Tower of Hanoi - Numberphile
- https://www.youtube.com/watch?v=8lhxIOAfDss - Recursion Superpower - Numberphile