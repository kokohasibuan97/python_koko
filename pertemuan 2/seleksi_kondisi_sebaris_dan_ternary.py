grade = int(input('Enter your current grade:'))
prev_grade = int(input('Enter your previous grade:')
                 )
if grade >= 90 and prev_grade >=65:
    print("awesome")
if grade >= 90 and prev_grade < 65:
    print("awesome, you definitely working hard, right?")
if grade >=65:
    print("passed the exam")
else:
        print("bellow the pasiing grade")

if (grade >=65 and not prev_grade >=65) or (not grade >=65 and prev_grade>=65):
    print("at least you passed one exam. good job!")
        