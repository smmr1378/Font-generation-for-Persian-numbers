import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import pytesseract # از pytesseract به جای easyocr استفاده کنید
import cv2
import matplotlib.pyplot as plt
import seaborn as sns # از seaborn به جای matplotlib استفاده کنید

def create_image(digits_list, width, height, resolution, font):
    text = ' '.join(digits_list)
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((500, 100), text, font=font, fill=0, anchor='mm', align='center') # از font به عنوان یک پارامتر ورودی استفاده کنید
    img = img.resize((width // resolution, height //
                     resolution), Image.Resampling.LANCZOS)
    img = img.resize((width, height), Image.Resampling.LANCZOS)

    label = ''.join(digits_list)
    img.save(f"output/{label}_{resolution}.png")

if __name__ == '__main__':
    os.makedirs('output', exist_ok=True)
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    width = 1000
    height = 200
    font = ImageFont.truetype('fonts/W_tahoma.ttf', 128) # از یک فونت با اندازه 128 استفاده کنید
    for i in range(10):
        digits_list = digits.copy()
        np.random.shuffle(digits_list)
        for resolution in range(1, 11):
            create_image(digits_list, width, height, resolution, font)

    # تعداد تصاویر را مشخص کنید
    num_images = 100

    # تصاویر، برچسب‌های واقعی و پیش‌بینی شده را بارگذاری کنید
    images = [] # لیستی از تصاویر به صورت آرایه‌های نامپای
    true_labels = [] # لیستی از برچسب‌های واقعی به صورت رشته
    pred_labels = [] # لیستی از برچسب‌های پیش‌بینی شده به صورت رشته

    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    image_path = 'D:\Python\produce-font\output'
    os.chdir(image_path)
    for file in os.listdir():
        if file.endswith(".png"):
            file_path = os.path.join(image_path,file)
            img = cv2.imread(file_path)
            text = pytesseract.image_to_string(img, lang='fas') # از pytesseract به جای easyocr استفاده کنید
            print(f"{file} - {text}")
            # اضافه کردن تصویر، برچسب واقعی و پیش‌بینی شده به لیست‌های مربوطه
            images.append(img)
            true_labels.append(file.split('_')[0])
            pred_labels.append(text)

    # یک شکل با اندازه 10 در 10 ایجاد کنید
    plt.figure(figsize=(10, 10))

    # برای هر تصویر یک زیرشکل ایجاد کنید
    for i in range(num_images):
        # انتخاب یک زیرشکل در سطر i // 5 و ستون i % 5
        plt.subplot(5, 5, i + 1)
        # نمایش تصویر با استفاده از seaborn
        sns.heatmap(images[i], cmap='gray', cbar=False, xticklabels=False, yticklabels=False, annot=True, fmt='')
        # اگر برچسب واقعی و پیش‌بینی شده برابر بودند، رنگ متن را سبز کنید، در غیر این صورت قرمز
        color = "green" if true_labels[i] == pred_labels[i] else "red"
        # نمایش برچسب واقعی و پیش‌بینی شده در زیر تصویر
        plt.xlabel(f"{true_labels[i]} ({pred_labels[i]})", color=color)

    # نمایش شکل
    plt.show()
