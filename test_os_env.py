import os
import time
import json
from attrdict import AttrDict

print(os.environ.keys())
print(os.environ.get('TESTER'))

a = {
    'a': 1,
    'b': 'c'
}
a = AttrDict(a)

os.environ['TESTER'] = "lpt"*3000
os.environ['TESTER'] = json.dumps(a)

for i in range(3):
    a_recv = json.loads(os.environ.get('TESTER'))
    a_recv = AttrDict(a_recv)
    print("===== 2: ", a_recv)
    print("==== a: ", a_recv.b)
    time.sleep(30)
