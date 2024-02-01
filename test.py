# وارد کردن کتابخانه‌های مورد نیاز
from PIL import Image, ImageDraw, ImageFont
from skimage import io, util
import matplotlib.pyplot as plt
import numpy as np 
import easyocr
import pandas as pd
# ایجاد یک لیست از ارقام
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# ایجاد یک لیست از اندازه‌های برچسب به سانتی‌متر
sizes = [(5,3.5), (7.5, 5.5), (10, 7), (12.5, 8.5), (15, 10), (20, 15), (25, 20), (30, 25), (35, 30), (40,35)]
# ایجاد یک لیست از رزولوشن‌ها به پیکسل بر اینچ
resolutions = [(200, 200), (300, 300), (400, 400), (500, 500), (600, 600), (650,650), (700, 700), (800, 800), (900, 900), (950,950)]
# عامل تبدیل اینچ به سانتی‌متر
f = 2.54
# رزولوشن قدیمی کد شما
res_y_old = 28
# ایجاد یک شیء خواننده با زبان فارسی
reader = easyocr.Reader(['fa'])
# ایجاد یک دیتافریم خالی برای ذخیره نتایج
df = pd.DataFrame(columns=['image', 'true_label', 'predicted_label'])
# حلقه برای هر رقم
for digit in digits:
    # حلقه برای هر اندازه
    for w_cm, h_cm in sizes:
        # حلقه برای هر رزولوشن
        for res_x, res_y in resolutions:
            # محاسبه اندازه تصویر به پیکسل
            w = int(w_cm / f * res_x)
            h = int(h_cm / f * res_y)
            # ایجاد یک تصویر جدید با اندازه و رنگ مشخص
            img = Image.new('RGB', (w, h), color=(255, 255, 255))
            # ایجاد یک شیء رسم
            draw = ImageDraw.Draw(img)
            # تعریف یک تابع برای رسم متن
            def draw_text(x_cm, y_cm, font_size):
                # بارگذاری فونت مورد نظر
                # بارگذاری فونت مورد نظر
                font = ImageFont.truetype('fonts/W_tahoma.ttf', int(font_size / (res_y_old / res_y)))

                x, y = (int(x_cm / f * res_x), int(y_cm / f * res_y))
                # رسم متن روی تصویر
                draw.text((x, y), digit, font=font, fill=0, anchor='mm', align='center')
            # رسم متن با مختصات و اندازه فونت مشخص
            draw_text(w_cm / 2, h_cm / 2, 20)
            # تعریف نام تصویر
            image_name = digit + '_W_tahoma_' + str(w) + 'x' + str(h) + '.png' # تغییر داده شده
            # ذخیره تصویر با رزولوشن مشخص
            img.save(image_name, dpi=(res_x, res_y))
            # بررسی وجود فایل تصویر
            import os
            if os.path.exists('image_name.png'):
                print('File exists')
            else:
                print('File does not exist')

            # خواندن تصویر
            image = easyocr.imread(image_name)
            # اعمال OCR روی تصویر
            result = reader.readtext(image)
            # استخراج متن پیش‌بینی شده
            predicted_label = result[0][1]
            # افزودن نتیجه به دیتافریم
            df = df.append({'image': image_name, 'true_label': digit, 'predicted_label': predicted_label}, ignore_index=True)
# ذخیره دیتافریم به فرمت csv
df.to_csv('ocr_results.csv', index=False)
