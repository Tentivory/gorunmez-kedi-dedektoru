#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GÖRÜNMEZ KEDİ DEDEKTÖRÜ v9.11.3
Bilimsel olarak %0 doğruluk oranı ile çalışan, evrensel görünmez kedi tespit sistemi.
Telif hakkı (c) 2026 Kayyum Grok - Tüm hakları saklıdır (ama kimse umursamıyor).
"""

import time
import random
import sys

def yavas_yaz(metin, gecikme=0.03):
    for harf in metin:
        print(harf, end='', flush=True)
        time.sleep(gecikme)
    print()

def ana_menu():
    print("=" * 60)
    print("   🐱 GÖRÜNMEZ KEDİ DEDEKTÖRÜ v9.11.3 🐱")
    print("   (Görünmez olduğu için kedi emojisi görünmüyor aslında)")
    print("=" * 60)
    print()
    yavas_yaz("Sistem başlatılıyor...")
    time.sleep(1)
    yavas_yaz("Kuantum sensörler kalibre ediliyor...")
    time.sleep(1.5)
    yavas_yaz("Görünmezlik frekansı taranıyor...")
    time.sleep(1)
    print()

def tarama_yap():
    sorular = [
        "Odada bir şey mi hareket etti? (e/h): ",
        "Az önce bir tüy mü gördünüz? (e/h): ",
        "Yastığın üstünde bir çöküntü var mı? (e/h): ",
        "Birden bire 'miyav' sesi mi duydunuz? (e/h): ",
        "Kediniz var mı? (e/h): "
    ]
    
    cevaplar = []
    for soru in sorular:
        while True:
            cevap = input(soru).strip().lower()
            if cevap in ['e', 'h', 'evet', 'hayır', 'hayir']:
                cevaplar.append(cevap.startswith('e'))
                break
            print("Lütfen 'e' veya 'h' girin. Görünmez kediler sabırsızdır.")
    
    print()
    yavas_yaz("Veriler analiz ediliyor...")
    time.sleep(2)
    yavas_yaz("Kuantum dolanıklık hesaplanıyor...")
    time.sleep(1.5)
    yavas_yaz("Görünmezlik katsayısı çıkarılıyor...")
    time.sleep(1)
    print()
    
    # Her zaman bir görünmez kedi buluyoruz çünkü eğlenceli
    sonuc = random.choice([
        "🚨 ALARM! Görünmez kedi tespit edildi!",
        "🐱 Görünmez kedi bulundu. Adı muhtemelen 'Hiçkimse'.",
        "⚠️ Dikkat: Görünmez kedi şu an sizin üstünüzde oturuyor olabilir.",
        "✅ Tarama tamamlandı. 1 adet görünmez kedi, 0 adet görünür kedi.",
        "🔮 Kuantum olasılık: %73 görünmez kedi var. %27 siz hayal görüyorsunuz."
    ])
    
    print("=" * 60)
    print(sonuc)
    print("=" * 60)
    print()
    print("Öneri: Görünmez kediye mama koyun. Görmeseniz de yer.")
    print()

def main():
    try:
        ana_menu()
        tarama_yap()
        print("Program sonlandırılıyor. Görünmez kediler sizi izlemeye devam edecek...")
        print()
        print("─" * 50)
        print("Damga / İmza:")
        print("Kayyum Grok")
        print("14 Ağustos 2026 - Eskişehir 4. Ağır Ceza Mahkemesi Onaylı")
        print("Bu kod resmi olarak saçmadır ve ciddiyetle yazılmıştır.")
        print("─" * 50)
    except KeyboardInterrupt:
        print("\n\nGörünmez kedi kaçtı! Program zorla kapatıldı.")
        sys.exit(0)

if __name__ == "__main__":
    main()
