import os
print(os.popen('ls -l').read())
print(os.popen('uptime').read())