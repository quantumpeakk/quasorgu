import requests
import json
import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system("clear")

def banner():
    print(Fore.CYAN + """
╔════════════════════════════════════╗
║   🔐 SORGU TOOL                    ║
║   👤 Yapımcı: @quantumpeak         ║
╚════════════════════════════════════╝
""")

def ad_soyad_il_sorgu():
    print(Fore.YELLOW + "\n🔍 Ad Soyad İl Sorgusu")
    ad = input(Fore.CYAN + "Ad: ").strip()
    soyad = input(Fore.CYAN + "Soyad: ").strip()
    il = input(Fore.CYAN + "İl: ").strip()

    url = "https://api.hexnox.pro/sowixapi/adsoyadilce.php"
    params = {
        "ad": ad,
        "soyad": soyad,
        "il": il
    }

    try:
        r = requests.get(url, params=params)
        data = r.json()
        print(Fore.GREEN + "\n🧾 Sonuç:")
        for k, v in data.items():
            print(Fore.GREEN + f"{k.capitalize()}: {v}")
    except Exception as e:
        print(Fore.RED + f"Hata: {e}")

def gsm_sorgu():
    print(Fore.YELLOW + "\n📞 GSM Numarası Sorgusu")
    gsm = input(Fore.CYAN + "GSM (05XXXXXXXXX): ").strip()

    url = "https://api.hexnox.pro/sowixapi/gsm.php"
    params = {"gsm": gsm}

    try:
        r = requests.get(url, params=params)
        data = r.json()
        print(Fore.GREEN + "\n🧾 Sonuç:")
        for k, v in data.items():
            print(Fore.GREEN + f"{k.capitalize()}: {v}")
    except Exception as e:
        print(Fore.RED + f"Hata: {e}")

def tc_to_gsm():
    print(Fore.YELLOW + "\n🆔 TC → GSM Sorgusu")
    tc = input(Fore.CYAN + "TC Kimlik No: ").strip()

    url = "https://api.hexnox.pro/sowixapi/tcgsm.php"
    params = {"tc": tc}

    try:
        r = requests.get(url, params=params)
        data = r.json()
        print(Fore.GREEN + "\n🧾 Sonuç:")
        for k, v in data.items():
            print(Fore.GREEN + f"{k.capitalize()}: {v}")
    except Exception as e:
        print(Fore.RED + f"Hata: {e}")

def sifre_kontrol():
    clear()
    print(Fore.MAGENTA + "🔐 Bu araca erişmek için şifre gerekli.")
    sifre = input(Fore.CYAN + "Şifre: ").strip()
    if sifre != "lyrica":
        print(Fore.RED + "❌ Hatalı şifre. Çıkılıyor...")
        exit()

def main():
    sifre_kontrol()
    while True:
        clear()
        banner()
        print(Fore.YELLOW + "1. Ad Soyad Sorgu")
        print("2. GSM → TC Sorgu")
        print("3. TC → GSM Sorgu")
        print("0. Çıkış\n")

        secim = input(Fore.CYAN + "Seçiminiz: ").strip()

        if secim == "1":
            ad_soyad_il_sorgu()
        elif secim == "2":
            gsm_sorgu()
        elif secim == "3":
            tc_to_gsm()
        elif secim == "0":
            print(Fore.MAGENTA + "\n👋 Güle güle!")
            break
        else:
            print(Fore.RED + "❗ Geçersiz seçim!")

        input(Fore.CYAN + "\n⏎ Devam etmek için Enter'a bas...")

if __name__ == "__main__":
    main()
