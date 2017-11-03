# Problem : File Permissions (passwd, shadow and group) Are Not Properly Set
# Note:
# 1. The user running the script must have administrative(root) privileges.
# 2. The script is written in python2
# 3. A backup file for file permissions is created at the location '/tmp/file_name.acl' 

# {
# modifying the file permissions for owner, groups, others  
  
import os, datetime, sys, time
odat = (time.strftime("%d-%m-%Y"))
dat = datetime.datetime.now()

ipv4 = os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0]
file_log = '/tmp/test1_' + str(ipv4) + '_' + str(odat) + '.log'
f = open(file_log,'a+')
saveout = sys.stdout
sys.stdout = f

print "***************Log Started for test1*******************"

print '\nOn Date: ' + str(dat) + '\n' + 'In System with ip: ' + ipv4 + '\n'
os.system("getfacl -p /etc/group > /tmp/group.acl")
os.system("getfacl -p /etc/passwd > /tmp/passwd.acl")
os.system("getfacl -p /etc/shadow > /tmp/shadow.acl")

print "Backup permissions files are created as '/tmp/group.acl','/tmp/passwd.acl','/tmp/shadow.acl' "

os.system("sudo chmod 644 /etc/passwd")
os.system("sudo chmod 600 /etc/shadow")
os.system("sudo chmod 644 /etc/group")

print 'Updated access permissions:\n'
p1 = os.popen("ls -l /etc/passwd")
print p1.readline()
p2 = os.popen("ls -l /etc/shadow")
print p2.readline()
p3 = os.popen("ls -l /etc/group")
print p3.readline()

print "***************Log Ended for test1*******************"
sys.stdout = saveout
f.close()
# }
