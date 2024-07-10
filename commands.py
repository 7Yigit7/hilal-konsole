#Yazan Yiğit

import os
import config as cf

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
    info = """
    Sürüm: 1.0
    Hazırlayan : Yiğit
    Lisans : GPL
    paket yöneticileri: apt - dnf
    github:
    """
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

