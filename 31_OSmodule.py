import os

curDir = os.getcwd()

print(curDir)

os.mkdir('newDIr')

import time

time.sleep(4)

os.rename('newDIr','newDirTwo')

time.sleep(3)

os.rmdir('newDirTwo')
