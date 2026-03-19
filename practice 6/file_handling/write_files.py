with open('/Users/algida/pp2/practice 6/file_handling/plants.txt', 'w') as t:
    t.write('Nowadays we have a big amount of plants')

with open('/Users/algida/pp2/practice 6/file_handling/grades.txt', 'w') as grade:
    grade.write('Student : Hermione Ghauri')
    grade.write('\nYear : 2')
    grade.write('\nScores in disciplineds for the attestation period :')
    grade.write('\nComputer Science : 58.00')
    grade.write('\nCalculus III : 60.00')
    grade.write('\nDifferential equations : 57.00')
    grade.write('\nPhilosophy : 59.00')
    grade.write('\nPhysics II : 60.00')
    grade.write('\nHistory : 58.00')

with open('/Users/algida/pp2/practice 6/file_handling/grades.txt', 'a') as grade:
    grade.write('\nShe did a great job!!!!!!!!!!')

