# Port Scanner
# :) Vexvain :)
import sys, socket

argv = sys.argv
argc = len(argv)
if(argc < 3 or argc > 3):
    sys.exit("[\x1b[31m?\x1b[37m] Usage: python "+argv[0]+" <target ipv4> <max port>")
target = argv[1]
least_port = 1;
max_port = int(argv[2])
for x in xrange(max_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = int(x)
    s.settimeout((0.001))
    try:
        s.connect((target, port))
        print "[\x1b[33m+\x1b[37m] Port \x1b[32m%d\x1b[37m is open!" % (port)
    except:
        #print "[\x1b[31m#\x1b[37m] Port Closed \x1b[32m%d\x1b[37m..." % (port)
        continue
print "[\x1b[35m!\x1b[37m] Done scanning \x1b[34m%d\x1b[37m port(s)." % (max_port)
