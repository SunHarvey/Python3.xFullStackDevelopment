import subprocess

result = subprocess.call(['ping', 'www.baidu.com', '-c', '5'])
print(result)
