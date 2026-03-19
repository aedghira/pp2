#DELETE FILE METHODS
import os
os.remove('/Users/algida/pp2/practice 6/file_handling/plants.txt')

if os.path.exists('GPA_results.txt'):
    os.remove('GPA_results.txt')
else:
    print('Oops(This file does not exist in your folder')

#COPY FILE METHODS
import shutil

shutil.copy('/Users/algida/pp2/practice 6/file_handling/grades.txt','/Users/algida/pp2/practice 6/file_handling/hermione_score.txt') 
