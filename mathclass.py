import numpy as np

# main part begins here
q1 = ''
q2 = ''
q3 = ''
operation = ''
questions = 0
difficultyLevel = 0

print('***************************************')
print('')
print('          M A T H   C L A S S')
print('')
print('***************************************')
print('')

while q1 == '':
    print('Choose an operation: ')
    print('[1] Addition; [2] Subtraction; [3] Multiplication', end=' > ')
    q1 = input()
    if q1 == '1':
        operation = "+"
    elif q1 =='2':
        operation = '-'
    elif q1 == '3':
        operation = 'x'
    else:
        print('?Input 1, 2 or 3')
        q1 = ''

while q2 == '':
    print('How many questions are you taking? ')
    print('[1] 10  [2] 20  [3] 50  [4] 100', end=' > ')
    q2 = input()
    if q2 == '1':
        questions = 10
    elif q2 == '2':
        questions = 20
    elif q2 == '3':
        questions = 50
    elif q2 == '4':
        questions = 100
    else:
        print('?Input 1, 2, 3 or 4')
        q2 = ''

while q3 == '':
    print('Choose difficulty level.')
    if operation == '+':
        print('[1]: X + X')
        print('[2]: XX + X')
        print('[3]: XX + XX')
        print('[4]: XXX + XXX')
        print('> ', end='')
    elif operation == '-':
        print('[1]: XX - X')
        print('[2]: XX - XX')
        print('[3]: XXX - XX')
        print('[4]: XXX - XXX')
        print('> ', end='')
    elif operation == 'x':
        print('[1]: X x X')
        print('[2]: XX x X')
        print('[3]: XXX x X')
        print('[4]: XXX x XX')
        print('> ', end='')
    q3 = input()
    if q3 == '1':
        difficultyLevel = 1
    elif q3 == '2':
        difficultyLevel = 2
    elif q3 == '3':
        difficultyLevel = 3
    elif q3 == '4':
        difficultyLevel = 4
    else:
        print('?Input 1, 2, 3 or 4')
        q3 = ''

a = [[0, 0, 0, 0, False]]
for i in range(1, questions+1):
    if operation == '+':
        if difficultyLevel == 1:
            x1 = np.random.randint(0, 9)
            x2 = np.random.randint(0, 9)
        elif difficultyLevel == 2:
            x1 = np.random.randint(10, 99)
            x2 = np.random.randint(0, 9)
        elif difficultyLevel == 3:
            x1 = np.random.randint(10, 99)
            x2 = np.random.randint(10, 99)
        else:
            x1 = np.random.randint(100, 999)
            x2 = np.random.randint(100, 999)
        correctAnswer = x1 + x2
    elif operation == '-':
        if difficultyLevel == 1:
            x1 = np.random.randint(10, 99)
            x2 = np.random.randint(0, 9)
        elif difficultyLevel == 2:
            while x1 <= x2:
                x1 = np.random.randint(10, 99)
                x2 = np.random.randint(10, 99)
        elif difficultyLevel == 3:
            x1 = np.random.randint(100, 999)
            x2 = np.random.randint(10, 99)
        else:
            while x1 <= x2:
                x1 = np.random.randint(100, 999)
                x2 = np.random.randint(100, 999)
        correctAnswer = x1 - x2
    else:
        if difficultyLevel == 1:
            x1 = np.random.randint(0, 9)
            x2 = np.random.randint(0, 9)
        elif difficultyLevel == 2:
            x1 = np.random.randint(10, 99)
            x2 = np.random.randint(0, 9)
        elif difficultyLevel == 3:
            x1 = np.random.randint(100, 999)
            x2 = np.random.randint(0, 9)
        else:
            x1 = np.random.randint(100, 999)
            x2 = np.random.randint(10, 99)
        correctAnswer = x1 * x2
    a.append([x1, x2, correctAnswer, 0, False])
    print('Question {0}:    '.format(i), end='')
    print('{0} {1} {2} = '.format(a[i][0], operation, a[i][1]), end='')
    a[i][3] = int(input())
    if a[i][3] == a[i][2]:
        a[i][4] = True
        print('BINGO!')
        print('')
    else:
        print('OOPS!')
        print('Correct answer is {0}'.format(a[i][2]))
        print('')

bingos = 0
for i in range(1, questions+1):
    print('')
    print('-------------------------------')
    print('     R E S U L T')
    print('-------------------------------')
    print('Question {0}: {1} {2} {3} = {4} : '.format(i, a[i][0], operation, a[i][1], a[i][3]), end='')
    if a[i][4] == True:
        bingos += 1
        print('Correct')
    elif a[i][4] == False:
        print('Incorrect (Correct answer={0})'.format(a[i][2]))

print('')
print('')
score: int = 100 * bingos // questions
print('Your score: {0} points'.format(score))
print('')
if score >= 80:
    print('Excellent!')
elif score >= 60:
    print('Good.')
elif score >= 50:
    print('Fair.')
else:
    print('Crap!')
print('')
