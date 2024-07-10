#Yazan Yiğit

#Merhaba bu py sayfasında sizlere neler yaptığımı anlatacağım
#hemde ayrıntılı bir şekilde

#Gerekli modüller bunlar
import os
#OS modülü işletim sistemi işlemlerini yapar
#Yani klasör aç kapa, dosya sil, dosya gez gibi işler
#Bir işletim sistemi yazmak için iyi bir modül
#En sevdiğim fonsiyonu systen() bu fonksiyon bilgisayarınızda yüklü olan işletim sisteminin
#komutlarını çalıştırır.

from termcolor import colored
#Bu ise print çıktılarını renkli yapmaya yarıyor
#Bu modülü GPT'den öğrendim bu modül hakkında pek bilgim yok

import commands as komut
#Bu benim oluşturduğum bir modül
#Komutlar bu modülde olacak

import config as cf

import history

kürdistan = "" # Sadece bir şaka :)

cf.start()# Başlangıç kodları
#Aşağıda bir while dongüsü var, bu döngü sayesinde program kapanmıyor ve her zaman bir komut bekler
#kapat komudunu kullanana kadar.

history.setup_input_history()

while_key = True
#Ben bu değişkene while anahtarı diyorum
#Bunun görevi ise while döngüsünü True yani aktif halede çalışmasını ve zamanı gelince False yani kapanmasını sağlamak
#1 ve 0 gibi, kapalı veya açık.
while while_key:
    konum = os.getcwd()
    #Bu konum değişkenidir
    #While döngüsü sayesinde güncel konumu yani bulunduğumuz diziyi gösterir.
    Kullanici_adi = os.getlogin()

    makine_adi = os.uname().nodename

    #Temalar
    #sizlerde istediğiniz temayı oluşturabilirsiniz
    tema1 = colored(cf.title,cf.hk1_color) + f"> {colored(Kullanici_adi,cf.ka3_color)}" + f" > {colored(konum,cf.kd2_color)}{cf.terminal_ucu} "
    tema2 = colored(f"{Kullanici_adi}@{makine_adi}:{konum}",cf.tm4_2_color) + "₺ "
    tema3 = colored(f"C:{konum}> ",cf.tm5_3_color)

    #Tema değiştir
    #1: Hilal tarzı
    #2: GNU linux tarzı
    #3: Windows cmd tarzı
    tema = tema1 #<---  Aktif olan tema

    main = history.get_input(tema)
    #bu input komut girmemizi sağlar

    #Aşağıda bir if bloğu daha doğrusu bir if ağı var
    #bu if ağı komutları gireceğimiz girdiye göre çalıştırır.
    if main == "kapat":#While anahtarını hatırladınız mı? işte bu komut while döngüsünü bozar ve bu sayede program kapanır.
        while_key = False

    elif main == "tmz":# linıx komudunu kullanarak terminali temizler
        os.system("clear")

    elif main == kürdistan:#Hiç bir komut yazmadan sadece enter tuşuna basınca hiç birşey olmazya işte bu ona yarıyor.
        pass

    #Bundan sonrası sizde
    #Kodumu inceleyin ve keşifedin
    #Yaptığım herşeyi anlatmak zor olur.

    elif main[0:4] == "gir ":
        komut.gir(main[4::])

    elif main == "ip göster":
        komut.ip_goster()

    elif main == "geri":
        komut.geri()

    elif main == "konum":
        komut.konum()

    elif main == "hilal":
        komut.hilal()

    elif main[0:6] == "yetki ":
        komut.yetki(main[6::])

    elif main[0:4] == "apt kur": # APT kapet yöneticisi DEBİAN
        komut.paket_yonetici(tip=main[0:4],islem="install "+main[8::])
    elif main[0:4] == "apt " or main[0:4] == "apt ":
        if main[4::] == "paket -g" or main[4::] == "paket güncelle":
            komut.paket_yonetici(tip=main[0:4],islem="update")
        elif main[4::] == "sistem -g" or main[4::] == "sistem güncelle":
            komut.paket_yonetici(tip=main[0:4],islem="upgrade")
        else:
            print(cf.error2)

    elif main[0:8] == "dnf kur ": # DNF paket yöneticisi FEDORA
        komut.paket_yonetici(tip=main[0:4],islem="install "+main[8::])
    elif main[0:4] == "dnf " or main[0:4] == "dnf ":
        if main[4::] == "paket -g" or main[4::] == "paket güncelle":
            komut.paket_yonetici(tip=main[0:4],islem="update")
        elif main[4::] == "sistem -g" or main[4::] == "sistem güncelle":
            komut.paket_yonetici(tip=main[0:4],islem="upgrade")
        else:
            print(cf.error2)

    elif main[0:5] == "klos ":
        komut.klos(main[5::])   # Dosya işlemleri bölümü
    elif main[0:4] == "sil ":
        komut.sil(main[4::])
    elif main[0:4] == "yaz ":
        os.system(f"nano {main[4::]}")
    elif main[0:6] == "dosya ":
        komut.dosya(main[6::])

    elif main == "tema1":
        os.system("hilal")#Tema geçiş sistemi

    elif main == "tema2":#Kurulum sırasında bu paketlerde kurulur
        os.system("tema-gnu")

    elif main == "tema3":
        os.system("tema-cmd")

    else:
        os.system(main)


