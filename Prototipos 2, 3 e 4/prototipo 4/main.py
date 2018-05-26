import subprocess
from subprocess import PIPE

def main():
    process = subprocess.call('python prediction.py', shell=True)
    process = subprocess.call('python gerajson.py', shell=True)
    
if __name__ == '__main__':
    main()
