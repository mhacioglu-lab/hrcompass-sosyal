"""Lansman serisi gönderi metinleri ve Metricool verisi (31.10–12.11.2026)."""
import json

B = 'https://raw.githubusercontent.com/mhacioglu-lab/hrcompass-sosyal/main/2026-10-31-lansman/'
UTM = '?utm_source=sosyal&utm_medium=organik&utm_campaign=lansman_2026_11'

G = [
    ('2026-10-31T10:00:00', '00-genel-4x5.jpg', 'HRCompass: İK\'nın tüm dijital çözümleri tek çatıda', 'https://hrcompass.com.tr/', True,
     """İK'nın tüm dijital çözümleri artık tek çatı altında. 🧭

HRCompass yayında! İK profesyonelleri için hazırladığımız tüm uygulamalar ücretsiz:

📰 HRNews: Günlük İK haberleri, iki kaynakla doğrulanmış
📊 HRSurvey: 38 hazır şablonla anket, QR ile katılım
🎯 HRQuiz: Eğitim ve etkinlikler için canlı quiz
🏆 HR Arena: İK bilgi yarışması, düello ve haftalık lig
🧮 Araçlar ve Soru-Cevap: Kıdem, ihbar, brütten nete hesaplama; uzman editör yanıtları
🔎 İK Çözümleri Rehberi: Yazılım, danışmanlık ve eğitim firmalarını karşılaştırın, tek tıkla teklif isteyin

Ücret yok. Üye olun, hemen kullanmaya başlayın.
👉 hrcompass.com.tr

Önümüzdeki günlerde her uygulamayı tek tek tanıtacağız. Takipte kalın, İK'cı arkadaşlarınızı etiketleyin! 👇

#HRCompass #İnsanKaynakları #İK #İKProfesyonelleri #HRTech #İKTeknolojileri #ÇalışanDeneyimi #İşeAlım"""),
    ('2026-11-02T10:00:00', '01-hrnews.jpg', 'Günlük İK Haberleri', 'https://hrcompass.com.tr/haberler/', False,
     """Sabah kahvenizi içerken İK gündeminin neresindesiniz? ☕

HRNews ile Türkiye'nin İK gündemi her gün tek yerde:
✔ Atamalar, mevzuat, ücret, eğitim ve İK teknolojileri
✔ İki ayrı kaynakla doğrulanan haberler
✔ Haftalık bülten ve piyasa bandı

Okumak ücretsiz, üyelik bile gerekmez.
👉 hrcompass.com.tr/haberler

Siz İK haberlerini nereden takip ediyorsunuz? Yorumlarda buluşalım. 👇

#HRNews #İKHaberleri #İnsanKaynakları #ÇalışmaHayatı #Mevzuat #İKGündemi #HRCompass"""),
    ('2026-11-03T10:00:00', '02-hrsurvey.jpg', 'Ücretsiz Anket Oluşturun', 'https://hrsurvey.tr/', False,
     """Çalışanlarınız gerçekten ne düşünüyor? Sormadan bilemezsiniz.

HRSurvey ile dakikalar içinde anket kurun:
✔ 7 kategoride 38 hazır şablon: bağlılık, eNPS, işe uyum, eğitim, ücret algısı ve daha fazlası
✔ QR ya da kodla katılım
✔ Sonuçlar anında, anlaşılır raporla

Tamamen ücretsiz.
👉 hrsurvey.tr

Bu ay ekibinize hangi soruyu sormak isterdiniz? 👇

#HRSurvey #ÇalışanBağlılığı #eNPS #ÇalışanDeneyimi #Anket #GeriBildirim #İnsanKaynakları #HRCompass"""),
    ('2026-11-05T10:00:00', '03-hrquiz.jpg', 'Canlı İK Quizleri', 'https://hrquiz.tr/', False,
     """Eğitimde herkes telefonuna bakıyorsa, telefonu eğitime katın. 📱

HRQuiz ile eğitimi, toplantıyı, etkinliği yarışmaya çevirin:
✔ Katılımcılar PIN ile telefondan bağlanır
✔ Liderlik tablosu anında güncellenir
✔ Hazır İK quizleriyle hemen başlayın

Katılım ücretsiz. Eğitiminiz ya da etkinliğiniz için quiz hazırlatmak isterseniz bize yazın.
👉 hrquiz.tr

#HRQuiz #Eğitim #ÖğrenmeVeGelişim #Oyunlaştırma #EğitimTeknolojileri #İnsanKaynakları #HRCompass"""),
    ('2026-11-06T10:00:00', '04-hrarena.jpg', 'HR Arena Bilgi Yarışması', 'https://hrarena.tr/', False,
     """İK bilginize ne kadar güveniyorsunuz? Kanıtlama zamanı. 🏆

HR Arena'da:
✔ Arkadaşınla düello yap
✔ Haftalık ligde sıralamaya gir
✔ Yetkinlik pusulasıyla güçlü yanlarını ve gelişim alanlarını gör

Web'de hemen oyna, Android uygulaması yakında. Ücretsiz.
👉 hrarena.tr

Ekip arkadaşınızı etiketleyin, ilk düelloyu başlatın! 👇

#HRArena #BilgiYarışması #İKBilgisi #Oyunlaştırma #Yetkinlik #İnsanKaynakları #HRCompass"""),
    ('2026-11-09T10:00:00', '05-araclar.jpg', 'Araçlar ve Soru-Cevap', 'https://hrcompass.com.tr/araclar/', False,
     """Kıdem tazminatı ne kadar tutar? Yıllık izin bölünebilir mi? Yanıtlar artık bir tık uzakta.

✔ Kıdem, ihbar, brütten nete maaş, yıllık izin ve fazla mesai hesaplama araçları
✔ Soru-Cevap'ta sorunuzu sorun, uzman editörlerimiz kaynak göstererek yanıtlasın; isterseniz adınız gizli kalır
✔ Katkılarınızla rozet kazanın, ayın liderleri arasına girin

Hepsi ücretsiz.
👉 hrcompass.com.tr/araclar

Kaydedin, ihtiyacınız olduğunda elinizin altında olsun. 🔖

#KıdemTazminatı #YıllıkİzinHesaplama #BrüttenNete #İşHukuku #Bordro #İnsanKaynakları #HRCompass"""),
    ('2026-11-11T10:00:00', '06-ik-cozumleri.jpg', 'İK Çözüm Ortağınızı Bulun', 'https://hrcompass.com.tr/ik-cozumleri/', False,
     """Bordro yazılımı, eğitim firması, danışman… Doğru çözüm ortağını bulmak neden bu kadar zor olsun?

İK Çözümleri Rehberi'nde:
✔ Firmaları alanına göre arayın, karşılaştırın
✔ Tek tıkla teklif ya da demo isteyin
✔ İK firmasıysanız profilinizi ücretsiz oluşturun, QR dijital kartvizitinizi indirin

👉 hrcompass.com.tr/ik-cozumleri

Firmanız rehberde mi? Kontrol edin, profilinizi sahiplenin.

#İKÇözümleri #HRTech #İKYazılımı #İKDanışmanlığı #EğitimFirmaları #İnsanKaynakları #HRCompass"""),
    ('2026-11-12T10:00:00', '07-markalar.jpg', 'Markanızı İK Dünyasına Taşıyın', 'https://hrcompass.com.tr/', False,
     """Ürününüzü İK profesyonellerine anlatmanın en kısa yolu: onların her gün baktığı yerde olmak.

HRCompass ve HRNews'te reklam ve sponsorluk:
✔ Haber okurken, çözüm ararken, etkinlik seçerken görünün
✔ Gösterim, tıklama ve gelen teklifler ölçülür
✔ Reklamınızdan gelen ziyaretçi, üye olmadan size teklif gönderebilir

Uygun alan ve tarih için: info@hrcompass.com.tr

#Reklam #B2BPazarlama #İKPazarlaması #Sponsorluk #HRTech #İnsanKaynakları #HRCompass"""),
]


def info(tarih, dosya, baslik, adres, yz, metin):
    return {
        'autoPublish': True, 'draft': True, 'descendants': [], 'hasNotReadNotes': False, 'shortener': False,
        'smartLinkData': {'ids': []}, 'text': metin, 'media': [B + dosya], 'mediaAltText': [baslik],
        'firstCommentText': f'🔗 {adres}{UTM}',
        'providers': [{'network': n} for n in ('instagram', 'facebook', 'linkedin', 'tiktok')],
        'publicationDate': {'dateTime': tarih, 'timezone': 'Europe/Istanbul'},
        'instagramData': {'type': 'POST', 'isAiGenerated': yz}, 'facebookData': {'type': 'POST'},
        'linkedinData': {'type': 'post', 'previewIncluded': True},
        'tiktokData': {'title': baslik[:90], 'privacyOption': 'PUBLIC_TO_EVERYONE', 'autoAddMusic': False, 'photoCoverIndex': 0},
    }


if __name__ == '__main__':
    import sys
    i = int(sys.argv[1])
    print(json.dumps(info(*G[i]), ensure_ascii=False))
