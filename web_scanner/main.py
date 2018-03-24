#!/usr/bin/python
import os, sys

from domain_name import *
from nmap import *
from whois import *
#from general import *
from robots_txt import *
from ip_address import *


ROOT_DIR = 'companies'
if not os.path.exists(ROOT_DIR):
    os.makedirs(ROOT_DIR)

def save_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()

def web_scan(name, url):
	domain_name = get_domain(url)
	ip_addr = get_ip_address(domain_name)
	nmap = get_nmap('-F', ip_addr)
	robots_txt = get_robots_txt(url)
	whois = get_whois(domain_name)
	create_report(name, url, domain_name, ip_addr, nmap, robots_txt, whois)

def create_report(name, full_url, domain_name, ip_addr, nmap, robots_txt, whois):
	project_dir = ROOT_DIR + "/" + name
	#create_dir(project_dir)
	result = str("Full_URL:  \n"+ full_url + "\n********************************\n" + 
		"DOMAIN_NAME: \n" + domain_name + "\n********************************\n" + 
		"IP_ADDR: \n" + ip_addr + "\n********************************\n" +
		"NMAP_RESULTS: \n" + nmap + "\n********************************\n" +
		"ROBOTS_TXT: \n" + robots_txt + "\n********************************\n" +
		"WHOIS_RESULT: \n" + str(whois) + "\n********************************\n")
	save_file(project_dir + "_web-scan.txt", result)
		


	#write_file(project_dir + "/full_url.txt", full_url)
	#write_file(project_dir + "/domain_name.txt", domain_name)
	#write_file(project_dir + "/nmap.txt", nmap)
	#write_file(project_dir + "/ip_addr.txt", ip_addr)
	#write_file(project_dir + "/robots_txt.txt", robots_txt)
	#write_file(project_dir + "/whois.txt", whois)

def main(): 
	name = sys.argv[1]
	url = sys.argv[2]
	#print url
	web_scan(name, url)
	#web_scan('4hathacker', "http://www.4hathacker.in")
	#web_scan('wikipedia', 'https://en.wikipedia.org/wiki/Main_Page')

if __name__ ==  "__main__":
	main()
