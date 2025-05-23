import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
from ultralytics import YOLO


model = YOLO('yolov8x.pt')




pencere = tk.Tk()
pencere.title("Nesne Tanıma Sistemi")
pencere.geometry("800x600")


resim_alani = tk.Label(pencere)
resim_alani.pack(pady=10)

def resim_sec_ve_tanima():
    dosya_yolu = filedialog.askopenfilename(filetypes=[("Görüntü Dosyaları", "*.jpg *.jpeg *.png")])
    if not dosya_yolu:
        return


    img = cv2.imread(dosya_yolu)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    results = model(img_rgb)


    img_detected = results[0].plot()


    img_pil = Image.fromarray(cv2.cvtColor(img_detected, cv2.COLOR_BGR2RGB))
    img_pil.thumbnail((700, 500))


    img_tk = ImageTk.PhotoImage(img_pil)
    resim_alani.configure(image=img_tk)
    resim_alani.image = img_tk


buton = tk.Button(pencere, text="Resim Seç ve Nesne Tanı", command=resim_sec_ve_tanima, font=("Arial", 14))
buton.pack(pady=20)


pencere.mainloop()
