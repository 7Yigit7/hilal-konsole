#Yazan Yiğit

from os import getlogin
from os import chdir
from os import system

#input ayarları:

# Renk ayarları
#tema1
hk1_color = "green" # Başlık yazısı rengi
kd2_color = "blue" # Konum göstergesi rengi
ka3_color = "yellow" # Kullanıcı adı rengi
#tema2
tm4_2_color = "green" # tema 2 rengi
#tema3
tm5_3_color = "white" # tema3 rengi
# Mavi      : blue
# Sarı      : yellow
# kırmızı   : red
# Siyah     : black
# Yeşil     : green
#Başlık String veri tipi
title = "Hilal Konsol" # Başlık yazar

terminal_ucu = "₺" # Terminal ucu

#Hata mesajları:
error1 = "Hata01 >Klasör bulunamadı" # geri komutunun yanlış klasör hatası
error2 = "Hata02 >Yanlış girdi" # Paket yöneticisi hatası

#Başlangıç fonksiyonu
def start():# Program çalıştığı zaman devreye girecek kodlar:
    system("clear")# Program çalıştığı zaman terminali temizler

    Kullanici_adi = getlogin()
    chdir(f"/home/{Kullanici_adi}")# Program çalıştığı zaman kullanıcı dizisine gider

    #Sizlerde istediğiniz kodları ekleyebilirsiniz veya düzenleyebilirsiniz





