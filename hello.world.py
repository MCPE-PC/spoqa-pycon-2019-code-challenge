import sys
import random

colors = range(1, 8)
esc = '\x1b['

while True:
	sys.stdout.write(f'{esc}0;{str(random.choice(colors) + 30)};{str(random.choice(colors) + 40)}mCONNECT THE PYTHONISTAS\n{esc}0m')
