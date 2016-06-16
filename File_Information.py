#import the required modules
import os
import stat
import time
def file():
	file_name=raw_input('Enter the file name:')
	(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)=os.stat(file_name)
	# create a dictionary to hold file info
	file_info = {
	'fname': file_name,
	'fsize': size,
	'f_lm': time.strftime("%d/%m/%Y %I:%M:%S %p",time.localtime(mtime)),
	'f_la': time.strftime("%d/%m/%Y %I:%M:%S %p",time.localtime(atime)),
	'f_ct': time.strftime("%d/%m/%Y %I:%M:%S %p",time.localtime(ctime))
	}
	print
	print "file name = %(fname)s" % file_info
	print "file size = %(fsize)s bytes" % file_info
	print "last modified = %(f_lm)s" % file_info
	print "last accessed = %(f_la)s" % file_info
	print "creation time = %(f_ct)s" % file_info
	print
	if stat.S_ISDIR(mode):
	  print "This a directory"
	  file()
	  
	else:
	  print "This is not a directory"
	  print
	  print "A closer look at the os.stat(%s) tuple:" % file_name
	  print 'Mode',mode,'\nIno',ino,'\nDev',dev,'\nnlink',nlink,'\nuid',uid,'\ngid',gid,'\nSize %s bytes'%size
				
	  file()
	
file()
