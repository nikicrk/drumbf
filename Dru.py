import sys,shutil

runtah=["saya_gans/__pycache__","modul/__pycache__","ajg/__pycache__","saya_gans/ngewe/__pycache__"]

if sys.version[0]!="3":
	exit(" [!] gunakan versy python3")

from saya_gans import awokawokawok
try: [shutil.rmtree(x) for x in runtah]
except: pass
awokawokawok()
