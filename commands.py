#Yazan Yiğit

#Burada komutlar için gerekli bazı fonksiyonler vardır

import os
import config as cf
from termcolor import colored

def gir(konum):
    try:
        os.chdir(konum)
    except:
        print(cf.error1)

def ip_goster():
    os.system("ip addr show")

def konum():
    os.system("pwd")

def geri():
    os.chdir('..')

def hilal():
    info = colored("""
    Sürüm: 1.3
    Hazırlayan : Yiğit
    Lisans : GPL
    paket yöneticileri: apt - dnf
    github: https://github.com/7Yigit7/hilal-konsole
    web sitesi: yigitweb.online
    ""","cyan")
    print(info)

def yetki(komut):
    os.system(f"sudo {komut}")
    if komut == "kapat":
        kap_ = input("Bilgisayar kapatılsın mı? [E,H]₺ ")
        if kap_ == "e" or kap_ == "E":
            os.system("sudo shutdown now")
        else:
            pass

def paket_yonetici(tip="apt",islem="update"):
    os.system(f"sudo {tip} {islem}")

def klos(dosya_adi):
    os.system(f"mkdir {dosya_adi}")

def sil(dosya_adi):
    os.system(f"rm -r {dosya_adi}")

def dosya(dosya_adi):
    os.system(f"touch {dosya_adi}")

def durum():
    print()

def kp(x):
    os.system(f"cp {x}")

def py(start):
    os.system(f"python3 {start}")
def jar(start):
    os.system(f"java -jar {start}")
def c(start,derlenen):
    os.system(f"g++ {start} -o {derlenen} && ./{derlenen}")
def yanki(d):
    print(d)

