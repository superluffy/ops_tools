import os
import time

while True:
    os.system("netstat -n|grep ^tcp|awk '{print $NF}'|sort -nr|uniq -c")
    time.sleep(1)
