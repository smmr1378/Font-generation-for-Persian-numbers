import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import pytesseract 
import matplotlib.pyplot as plt

def create_image(digits_list, width, height, resolution, font):
    text = ' '.join(digits_list)
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((500, 100), text, font=font, fill=0, anchor='mm', align='center') # از font به عنوان یک پارامتر ورودی استفاده کنید
    img = img.resize((width // resolution, height //
                     resolution), Image.Resampling.LANCZOS)
    img = img.resize((width, height), Image.Resampling.LANCZOS)

    label = ''.join(digits_list)
    # به جای ذخیره تصویر، آن را برگردانید
    return img, label

if __name__ == '__main__':
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    width = 1000
    height = 200
    font = ImageFont.truetype('fonts/W_tahoma.ttf', 128) # از یک فونت با اندازه 128 استفاده کنید
    # تعداد تصاویر را مشخص کنید
    num_images = 100
    # تصاویر، برچسب‌های واقعی و پیش‌بینی شده را بارگذاری کنید
    images = [] # لیستی از تصاویر به صورت شیء Image
    true_labels = [] # لیستی از برچسب‌های واقعی به صورت رشته
    pred_labels = [] # لیستی از برچسب‌های پیش‌بینی شده به صورت رشته

    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    for i in range(num_images):
        digits_list = digits.copy()
        np.random.shuffle(digits_list)
        resolution = np.random.randint(1, 11)
        # ایجاد تصویر با استفاده از تابع create_image
        img, label = create_image(digits_list, width, height, resolution, font)
        # استخراج جدول داده با استفاده از pytesseract
        data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT, lang='fas')
        # چاپ ستون‌های مهم جدول
        print(data['level'])
        print(data['text'])
        print(data['conf'])
        print(data['left'])
        print(data['top'])
        print(data['width'])
        print(data['height'])
        # اضافه کردن تصویر، برچسب واقعی و پیش‌بینی شده به لیست‌های مربوطه
        images.append(img)
        true_labels.append(label)
        # انتخاب متن با بیشترین اطمینان به عنوان برچسب پیش‌بینی شده
        max_conf = 0
        max_text = ''
        for j, conf in enumerate(data['conf']):
            if conf > max_conf:
                max_conf = conf
                max_text = data['text'][j]
        pred_labels.append(max_text)

    # یک شکل با اندازه 20 در 20 ایجاد کنید
plt.figure(figsize=(20, 20))

# برای هر تصویر یک زیرشکل ایجاد کنید
for i in range(num_images):
    # انتخاب یک زیرشکل در سطر i // 10 و ستون i % 10
    plt.subplot(10, 10, i + 1)
    # نمایش تصویر با استفاده از matplotlib
    plt.imshow(images[i])
    # حذف مقیاس رنگ، برچسب‌های محورها و اعداد روی تصویر
    plt.axis('off')
    # اگر برچسب واقعی و پیش‌بینی شده برابر بودند، رنگ متن را سبز کنید، در غیر این صورت قرمز
    color = "green" if true_labels[i] == pred_labels[i] else "red"
    # نمایش برچسب واقعی و پیش‌بینی شده در زیر تصویر
    plt.xlabel(f"{true_labels[i]} ({pred_labels[i]})", color=color)

# نمایش شکل
plt.show()
