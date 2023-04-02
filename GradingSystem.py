print('*************** STUDENT GRADING SYSTEM **************')
print('Please enter student mark or score')
mark = int(input('Enter student mark: '))

if mark >= 70:
    print('Grade A')

elif mark >= 60 and mark < 70:
    print('Grade B')

elif mark >= 50 and mark < 60:
    print('Grade C')

elif mark >= 40 and mark < 50:
    print('Grade D')

elif mark < 40:
    print('Grade E')

else:
    print('Please the correct score')
