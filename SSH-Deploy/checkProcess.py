import pxssh
import sys

listArgs = ' / '.join(sys.argv)
print "Arguments : "+listArgs
tocheck = sys.argv[1]

s = pxssh.pxssh()
if not s.login (tocheck, 'sr-readonly', 'unsecure'):
    print "SSH session failed on login."
    print str(s)
else:
    print "SSH session login successful"
    s.sendline ('jps | grep DFSZKFailoverController | wc -l')
    s.prompt()         # match the prompt
    var = s.before     # print everything befere the prompt.
    tab = var.splitlines(True)
    if(tab[1].strip()=="1"):
        print 'DFSZKFailoverController Is Running'
    else:
        print 'DFSZKFailoverController Is NOT Running ['+tab[1].strip()+']'	
    s.logout()
