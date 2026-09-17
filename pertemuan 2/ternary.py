grade = int(input('Enter your current grade:'))
prev_grade = int(input('Enter your previous grade:')
                 )
if grade >= 90 and prev_grade >=65:
    print("awesome")
if grade >= 90 and prev_grade < 65:
    print("awesome, you definitely working hard, right?")
print("passed the exam") if grade >=65 else print("below the passing grade")
    

        