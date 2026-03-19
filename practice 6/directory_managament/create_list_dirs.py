#CREATE NESTED DIRECTORIES
import os
from pathlib import Path

os.makedirs('2026/03/19/daily_musthaves')

Path('2026/03/19/goals').mkdir(parents=True, exist_ok=True)

#LIST FILES AND FOLDERS

os.listdir('/Users/algida/pp2/practice 6/file_handling/')

os.listdir('/Users/algida/')

#FIND FILES BY EXTENSION

for x in Path('.').glob('*.py'):
    print(f"{x} is found!")

