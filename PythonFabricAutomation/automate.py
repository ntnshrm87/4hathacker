from fabric.api import env, sudo, put, get
import os
import time

def main():
	odat = (time.strftime("%d-%m-%Y"))
	os.system('mkdir /test1-Related')
	host_list = ["10.0.0.218", "10.0.0.222", "10.0.0.227", "10.0.0.228"]
	for item in host_list:
        	env.host_string = item
        	env.user = "root"
        	env.password = "redhat123"

		# make a directory as /tmp/test1 in remote server
		sudo("mkdir /tmp/test1")

		# put the codes in /tmp/test1
		put("/root/Desktop/test1.py", "/tmp/test1/test1.py")

		# run the script on remote machine
		sudo("python /tmp/test1/test1.py")

		# get the log files and save all the logs in /test1-Related
		log_remote_path = '/tmp/test1_' + str(item) + '_' + str(odat) + '.log'
		log_local_path = '/test1-Related' 
		get(log_remote_path, log_local_path)

if __name__ == "__main__":
	main()
