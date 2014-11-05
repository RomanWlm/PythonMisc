import pxssh
import sys

## Args : hostname, user, passwd, Java ProcessName, expected count (optional) 
if( len(sys.argv) < 5) :
	print "Wring number of arguments : expect at least 4"
	print " - Expected Arguments : host, user, passwd, Java ProcessName, expected count (optional)"
	sys.exit(-1)  

host = sys.argv[1]
user = sys.argv[2]
passwd = sys.argv[3]
processName = sys.argv[4]

##TODO check arg
 
if(len(sys.argv)>5) :
	if(str(sys.argv[5]).isdigit()):
		count = str(sys.argv[5])
	else : 
		print "ERROR : Given expected count process argument(5) is not a digit : "+str(sys.argv[5])+" check for 1 process " 
		count = "1"
else :
	count = "1"

print "Checking on "+str(user)+"@"+str(host)+" Java process '"+str(processName)+"'"

s = pxssh.pxssh()

if not s.login (host, user, passwd):
    	print "SSH session failed on login."
    	print str(s)
	sys.exit(-1)
else:
    	print "SSH session login successful"
    	s.sendline ('jps | grep -i '+str(processName)+' | wc -l')
    	s.prompt()         # match the prompt
    	var = s.before     # print everything befere the prompt.
    	tab = var.splitlines(True)
    	if(tab[1].strip()==str(count)):
		print str(processName)+' Is Running'
	else:
		print 'There is '+tab[1].strip()+' running process(es) of '+str(processName)	
s.logout()
sys.stdout.write(tab[1].strip())
sys.stdout.flush()
sys.exit(0)
