grade = int(input('Enter your current grade:'))
prev_grade = int(input('Enter your previous grade:')
                 )
if grade >= 90 and prev_grade >=65:
    print("awesome")
elif grade >= 90 and prev_grade < 65:
    print("awesome, you definitely working hard, right?")
else:
    message="passed the exam" if grade >=65 else "below the passing grade"
    print(message) 

