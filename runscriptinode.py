# !/usr/bin/python
import os,sys
print 'Enter file name and list inode metadata'
name=raw_input()
fd=os.open(name,os.O_RDWR)
info=os.fstat(fd)
print "File Information is as follows:"
print "File inode number:",info.st_ino
print "Device number:",info.st_dev
print "Number of link:",info.st_nlink
print "UID of the file:%d" %info.st_uid
print "GID of the file:%d" %info.st_gid
print "Size:",info.st_size
print "Access time:",info.st_atime
print "Modify time:",info.st_mtime
print "Change time:",info.st_ctime
print "Protection:",info.st_mode
print "Number of blocks allocated:",info.st_blocks
print "Size of blocks:",info.st_blksize
 
os.close(fd)
