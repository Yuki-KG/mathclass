# mathclass

mathclass is a math drill program. It offers addition, subtraction and multiplication questions according to difficulty.

## Requirement

Python 3.x is required to run this program. 
It doesn't work in Python 2.x environment.

## Usage

```bash
$ python mathclass.py
```

After you type as shown above, you have prompt message asking you the operation, number of questions, and difficulty level.

### Operation

Addition, subtraction, and multiplication are available. 
When you are asked what kind of operation you'd like, you can answer either [1] Addition, [2] Subtraction or [3] Multiplication. 
If you input other than 1, 2, or 3, you'll have an error message like this:

```
?Input 1, 2 or 3
```

### Number of question

You can select either 10, 20, 50 or 100 questions. 
If you input other than these numbers, you'll have an error message like this:

```
?Input 1, 2, 3 or 4
```

### Difficulty level

A difficulty level determines how many digits of operations.
You can select either 1, 2, 3 or 4 of the difficulty level.
1 is easiest, and 4 most difficult.

|Difficulty Level|Addition|Subtraction|Multiplication|
|:--|:--:|:--:|:--:|
|1|1 digit + 1 digit|2 digits - 1 digit|1 digit * 1 digit|
|2|2 digits + 1 digit|2 digits - 2 digits|2 digits * 1 digit|
|3|2 digits + 2 digits|3 digits - 2 digits|3 digits * 1 digit|
|4|3 digits + 3 digits|3 digits - 3 digits|3 digits * 2 digits|

### Answering questions

After selecting the operation, the number of questions and the difficulty level, your drill will start.

In each question, you give your answer and hit return.
When your answer is correct, "BINGO!" will appear.
Otherwise, "OOPS!" will appear along with the correct answer.

After completing the drill, the result will appear. The result includes the questions and answers you had answered and whether your answers are correct or not.

Your score will be shown below the result.
(0-100 points)
A short comment follows.
