# coding:utf-8

from modul import *


M = '\x1b[1;31m'
U = '\x1b[1;36m'
P = '\x1b[1;37m'
H = '\x1b[1;32m'
K = '\x1b[1;33m'
PI = '\x1b[1;35m'

mbwdru=[]

class gadag_user:
	def __init__(self,url,cookie):
		
		self.url=url
		self.cookies=cookie

	def followers(self,link,what=False):
		try:
			if what is True:
				link=req.get(link,cookies=self.cookies).text
			_=re.findall('" \/>\<div\ class\=\".."\>\<a\ href\=\"/(.*?)"\>\<span\>(.*?)</span\>',link)
			for __ in _:
				___=re.search("id=(\d*)" if "profile.php" in __[0] else "(.*?)\?",__[0])
				mbwdru.append(___.group(1)+"(muhamad badru)"+__[1] if ___ is not None else __[0]+"(mbwdru)"+__[1])
				print(f"\r\x1b[1;37m [*] Sedang dump {len(mbwdru)} mohon tunggu!",end="")
			if "Lihat Selengkapnya" in link:
				self.followers(self.url+parser(link,"html.parser").find("a",string="Lihat Selengkapnya")["href"],True)
			return mbwdru
		except: return mbwdru
		
	def fl(self,link,what=False):
		try:
			if what is True:
				link=req.get(link,cookies=self.cookies).text
			_=re.findall('style\=\"vertical-align: middle"\>\<a\ class\=\"..\" href\=\"/(.*?)"\>(.*?)</a\>',link)
			for __ in _:
				mbwdru.append(re.search("id=(\d*)" if "profile.php" in __ [0] else "(.*?)\?",__[0]).group(1)+"(muhamad badru)"+__[1])
				print(f"\r\x1b[1;37m [*] Sedang dump {len(mbwdru)} mohon tunggu!",end="")
			if "Lihat Teman Lain" in link:
				self.fl(self.url+parser(link,"html.parser").find("a",string="Lihat Teman Lain")["href"],True)
			return mbwdru
		except: return mbwdru
		
	def grup(self,link,why,what=False):
	#def grup(self,link,batas,what=False,why=False):
		try:
			if what is True:
				link=req.get(link,cookies=self.cookies).text
			_=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',link)
			for __ in _:
				___=re.search("id=(\d*)" if "profile.php" in __[0] else "Romi XD",__[0])
				mbwdru.append(___.group(1)+"(muhamad badru)"+__[1] if ___ is not None else __[0]+"(muhamad badru)"+__[1])
				print(f"\r\x1b[1;37m [*] Sedang dump {len(mbwdru)} mohon tunggu!",end="")
				#if len(mbwdru)==batas:
					#why=True;break
			#if why is False:
			if "Lihat Selengkapnya" in link:
				self.grup(self.url+parser(link,"html.parser").find("a",string="Lihat Selengkapnya")["href"],why,True)
			else:
				self.get_post(f"{self.url}/groups/{why}")
			return mbwdru
		except: return mbwdru
			
	def get_post(self,link):
		try:
			link=req.get(link,cookies=self.cookies).text
			_=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',link)
			for __ in _:
				if "profile.php" in __[0]:
					___=re.search("profile.php\?id=(\d*)",__[0]).group(1)
					if ___ in mbwdru:
						continue
					else:
						mbwdru.append(___+"(muhamad badru)"+__[1])
				else:
					___=re.search("(.*?)\?refid",__[0]).group(1)
					if ___ in mbwdru:
						continue
					else:
						mbwdru.append(___+"(muhamad badru)"+__[1])
				print(f"\r\x1b[1;37m [*] Sedang dump {len(mbwdru)} mohon tunggu!",end="")
			if "Lihat Postingan Lainnya" in link:
				self.get_post(self.url+parser(link,"html.parser").find("a",string="Lihat Postingan Lainnya")["href"])
		except: pass
			
	def cari(self,link,jumlah,what=False,why=False):
		try:
			if what is True:
				link=req.get(link,cookies=self.cookies).text
			_=re.findall('picture" \/>\<\/a\>\<\/td\>\<td\ class\=\".*?"\>\<a\ href\=\"\/(.*?)"\>\<div\ class\=\"..\"\>\<div\ class\=\"..\"\>(.*?)<\/div>',link)
			for __ in _:
				mbwdru.append(re.search("id=(\d*)" if "profile.php" in __[0] else "(.*?)\?refid=",__[0]).group(1)+"(muhamad badru)"+__[1])
				print(f"\r\x1b[1;37m [*] sedang dump {len(mbwdru)} mohon tunggu !",end="")
				if len(mbwdru)==jumlah:
					why=True;break
			if why is False:
				if "Lihat Hasil Selanjutnya" in link:
					self.cari(parser(link,"html.parser").find("a",string="Lihat Hasil Selanjutnya")["href"],jumlah,True)
			return mbwdru
		except: return mbwdru
					
	def request(self,link,what=False):
		try:
			if what is True:
				link=req.get(link,cookies=self.cookies).text
			_=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',link)
			for __ in _:
				mbwdru.append(re.search("uid=(\d*)" if "?uid" in __[0] else "\/(.*?)\?fref",__[0]).group(1)+"(muhamad badru)"+__[1])
				print(f"\r\x1b[1;37m [*] Sedang dump {len(mbwdru)} mohon tunggu!",end="")
			if "Lihat selengkapnya" in link:
				self.request(self.url+parser(link,"html.parser").find("a",string="Lihat selengkapnya")["href"],True)
			return mbwdru
		except: return mbwdru
	
	def like_post(self,link,jumlah,what=False,why=False):
		try:
			if what is True:
				link=req.get(link,cookies=self.cookies).text
			_=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"/(.*?)"\>(.*?)<\/a\>',link)
			for __ in _:
				mbwdru.append(re.search("id=(\d*)",__[0]).group(1)+"(muhamad badru)"+__[1] if "profile.php" in __[0] else __[0]+"(muhamad badru)"+__[1])
				print(f"\r\x1b[1;37m [*] Sedang dump {len(mbwdru)} mohon tunggu!",end="")
				if len(mbwdru)==jumlah:
					why=True;break
			if why is False:
				if "Lihat Selengkapnya" in link:
					self.like_post(self.url+parser(link,"html.parser").find("a",string="Lihat Selengkapnya")["href"],jumlah,True)
			return mbwdru
		except: return mbwdru
				
				