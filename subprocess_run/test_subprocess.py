import os
import subprocess
os.environ["TEST"] = "lpt"

s = subprocess.run("/data/luopengting/workspace/test/subprocess_run/test.sh", stderr=subprocess.PIPE)
print(s)

code, out, err = s.returncode, s.stdout, s.stderr
print(code, out)
print(err.decode('utf-8'))


print("=============")
s = subprocess.Popen("python /data/luopengting/workspace/test/subprocess_run/print_msg.py", shell=True)
print("*" * 10)
print(s.returncode)
print(s.stderr)
print("*" * 10)
s.wait()
print(s.returncode)
print(s.stderr)

print("*******************")
s = subprocess.Popen("sh /data/luopengting/workspace/test/subprocess_run/test.sh", shell=True)
s.wait()
print(s.returncode)

if s.returncode != 0:
    print("There is error.")

