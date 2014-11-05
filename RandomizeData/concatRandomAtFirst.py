import sys
import os
import random 
if len(sys.argv) < 3 :
	print "ERROR wrong number of arguments : "+str((len(sys.argv)-1))
	print "arg : (1) path of input file"
	print "arg : (2) path of output file"
	print "arg : (3) [optional] erasure if output have to be deleted if exists"

	sys.exit()

fileIn=sys.argv[1]
fileOut=sys.argv[2]
erasure=None

if len(sys.argv) > 3 :
	erasure=sys.argv[3]

print "Erasure ?"+ str(erasure)	
exists = os.path.exists(fileIn)

if( not exists):
	print "ERROR : file "+fileIn+" does not exists..."
	sys.exit()

exists = os.path.exists(fileOut)

if(exists):
	if(erasure=="erase"):
		print "File "+fileOut+" exists. Removing..."
		os.remove(fileOut)
		
	else : 
        	print "ERROR : file "+fileIn+" already exists..."
        	sys.exit()


print "Input :"+fileIn+", output : "+fileOut 

fin = open(fileIn,'r')
fout = open(fileOut,'w')

#nb of parsed lines 
count=0

for line in fin :
	newline = str(random.randint(1,10000000))+'#'+line
	fout.write(newline)
	count=count+1
	
print "Done for "+str(count)+" lines."
fin.close()
fout.close()

