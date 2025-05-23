# Nesne Tanıma Sistemi (YOLOv8 ile)

Bu proje, YOLOv8 modelini kullanarak görsellerdeki nesneleri tespit eden bir masaüstü uygulamasıdır. Uygulama, kullanıcıdan bir görsel seçmesini ister ve seçilen görsel üzerinde nesne tespiti gerçekleştirir.

## ✨ Özellikler

- Kullanıcı dostu grafik arayüz (Tkinter ile)
- Görselden nesne tespiti (YOLOv8 - `yolov8n.pt` modeli)
- Tespit edilen nesnelerin görsel üzerinde işaretlenmesi

## 📦 Kurulum

1. Python 3.10 veya üzeri bir sürüm kurulu olmalıdır.
2. Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:

```bash
pip install -r requirements.txt
```

> Alternatif olarak temel bağımlılıkları tek satırda kurmak için:

```bash
pip install ultralytics opencv-python pillow
```

## 🧠 Kullanılan Model

Bu uygulama Ultralytics tarafından geliştirilen [YOLOv8](https://github.com/ultralytics/ultralytics) modelini kullanır. `yolov8n.pt` modeli hafif ve hızlıdır, küçük projeler ve demolar için uygundur.

## 🔍 Tespit Edilebilen Nesne Kategorileri (COCO sınıfları)

Uygulama aşağıdaki 80 kategoride nesne tespiti yapabilir:

person, bicycle, car, motorcycle, airplane, bus, train, truck, boat, traffic light, fire hydrant, stop sign, parking meter, bench, bird, cat, dog, horse, sheep, cow, elephant, bear, zebra, giraffe, backpack, umbrella, handbag, tie, suitcase, frisbee, skis, snowboard, sports ball, kite, baseball bat, baseball glove, skateboard, surfboard, tennis racket, bottle, wine glass, cup, fork, knife, spoon, bowl, banana, apple, sandwich, orange, broccoli, carrot, hot dog, pizza, donut, cake, chair, couch, potted plant, bed, dining table, toilet, tv, laptop, mouse, remote, keyboard, cell phone, microwave, oven, toaster, sink, refrigerator, book, clock, vase, scissors, teddy bear, hair drier, toothbrush

## 👨‍💻 Hazırlayan

**Mehmet Yasin Tunca**

Bu proje eğitim ve sunum amaçlı hazırlanmıştır. YOLOv8 açık kaynaklı bir modeldir ve Ultralytics lisansı altında kullanılabilir.
