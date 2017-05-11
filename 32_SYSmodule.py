import sys

sys.stderr.write('This is stderr text. Should be in RED\n')
sys.stderr.flush()

sys.stdout.write('This is stdout. A blue text\n')


print(sys.argv)

#we can pass arguments into this python from command line using argv

if len(sys.argv) > 1:
    print(sys.argv[1])
