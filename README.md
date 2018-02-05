# CleanRobotCoverage
this is a online coverage problem solver, the framework is very simple:
1. choose a direction to start, then go straight forward, until hits something, and save all the free blocks and with its unexplored direction
2. revisit the last free block with its unexplored direct, run A star search, find a way from current block back to the last free block
3. repeat until the block saver has no free blocks
done!

matrix.txt, matix_1.txt, matrix_2.txt are txt files used to edit the space where the robot is in
use "python ReadMatrix.py", to run the project



hope someone can use the code and implement it into a real robot

Issues with real bot:
	real robot does not make perfect turn...for its way
