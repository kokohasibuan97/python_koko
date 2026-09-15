grade = int(input('Enter your current grade:'))
prev_grade = int(input('Enter your previous grade:')
                 )
if grade >= 90 and prev_grade >=65:
    print("awesome")
if grade >= 90 and prev_grade < 65:
    print("awesome, you definitely working hard, right?")
if grade >=65:
    message="passed the exam" if grade >=65 else "bellow the pasiing grade"
    print(message) 
