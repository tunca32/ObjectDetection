
# 🧠 Nesne Tanıma Sistemi (YOLOv8)

Bu Python projesi, **YOLOv8** modeli kullanarak görsellerdeki nesneleri tanır ve tespit edilen nesneleri görsel üzerinde işaretler. Tkinter arayüzü ile kullanıcı dostu bir deneyim sunar.

## 🖼️ Nasıl Çalışır?

Kullanıcı, sistem arayüzünden bir görsel seçer. Ardından, **YOLOv8** modeli kullanılarak görseldeki nesneler tanınır ve üzerinde sınıf ismi ile birlikte görsel olarak işaretlenir.

---

## ✅ Gereksinimler

- Python 3.10 veya üzeri  
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)  
- Aşağıdaki temel kütüphaneler:

```bash
pip install -r requirements.txt
```

Alternatif olarak bu temel kütüphaneleri tek komutla da kurabilirsiniz:

```bash
pip install ultralytics opencv-python pillow
```

---

## 🔽 Model Dosyasını İndirme

GitHub 100MB sınırı nedeniyle `yolov8x.pt` model dosyası repoya dahil edilmemiştir.

Proje çalışmadan önce modeli indirip proje klasörüne koymanız gerekir:

```bash
pip install ultralytics
yolo download model=yolov8x.pt
```

> İndirdikten sonra `yolov8x.pt` dosyasını proje klasörüne (örneğin: `object_detection_app/`) yerleştirin.

---

## 🏷️ Tanıyabildiği Nesne Kategorileri

YOLOv8, aşağıdaki **COCO veri kümesindeki 80 sınıfı** tanıyabilir:

```
person, bicycle, car, motorcycle, airplane, bus, train, truck, boat, traffic light,
fire hydrant, stop sign, parking meter, bench, bird, cat, dog, horse, sheep, cow,
elephant, bear, zebra, giraffe, backpack, umbrella, handbag, tie, suitcase, frisbee,
skis, snowboard, sports ball, kite, baseball bat, baseball glove, skateboard, surfboard,
tennis racket, bottle, wine glass, cup, fork, knife, spoon, bowl, banana, apple,
sandwich, orange, broccoli, carrot, hot dog, pizza, donut, cake, chair, couch,
potted plant, bed, dining table, toilet, tv, laptop, mouse, remote, keyboard,
cell phone, microwave, oven, toaster, sink, refrigerator, book, clock, vase,
scissors, teddy bear, hair drier, toothbrush
```

---

## 🚀 Uygulamayı Başlatma

1. Gerekli kütüphaneleri yükleyin
2. `main.py` dosyasını çalıştırın:

```bash
python main.py
```

Tkinter arayüzü ile uygulama başlayacaktır.

---

## 👨‍💻 Proje Sahibi

Bu proje **Mehmet Yasin Tunca** tarafından hazırlanmıştır.  
