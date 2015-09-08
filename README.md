## 100 Doors

http://rosettacode.org/wiki/100_doors

Problem: You have 100 doors in a row that are all initially closed. You make 100 passes by the doors. The first time through, you visit every door and toggle the door (if the door is closed, you open it; if it is open, you close it). The second time you only visit every 2nd door (door #2, #4, #6, ...). The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.
Question: What state are the doors in after the last pass? Which are open, which are closed?

## 24 Game

http://rosettacode.org/wiki/24_game

The 24 Game tests one's mental arithmetic.
Write a program that randomly chooses and displays four digits, each from one to nine, with repetitions allowed. The program should prompt for the player to enter an arithmetic expression using just those, and all of those four digits, used exactly once each. The program should check then evaluate the expression. The goal is for the player to enter an expression that evaluates to 24.
Only multiplication, division, addition, and subtraction operators/functions are allowed.
Division should use floating point or rational arithmetic, etc, to preserve remainders.
Brackets are allowed, if using an infix expression evaluator.
Forming multiple digit numbers from the supplied digits is disallowed. (So an answer of 12+12 when given 1, 2, 2, and 1 is wrong).
The order of the digits when given does not have to be preserved.
Note:
The type of expression evaluator used is not mandated. An RPN evaluator is equally acceptable for example.
The task is not for the program to generate the expression, or test whether an expression is even possible.
