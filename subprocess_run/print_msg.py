import os
import time

print("Hello in python file.")
time.sleep(5)
print("Env: ", os.environ.get("TEST"))

raise ValueError('lalala')
