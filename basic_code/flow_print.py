import time
import sys 

test = "A simple sentence."

for char in test:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.2)