# وارد کردن کتابخانه‌های مورد نیاز
from PIL import Image, ImageDraw, ImageFont
from skimage import io, util
import matplotlib.pyplot as plt
import numpy as np 
# ایجاد یک لیست از ارقام
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# حلقه برای هر رقم
for digit in digits:
    # ایجاد یک تصویر خالی با پس‌زمینه سفید و اندازه 28 در 28 پیکسل
    img = Image.new('L', (28, 28), 255)

    # ایجاد یک شیء رسم را ایجاد کند که بتواند متن را روی تصویر بنویسد
    draw = ImageDraw.Draw(img)

    # بارگذاری فونت مورد نظر
    font = ImageFont.truetype('calibri.ttf', 20)

    # رسم متن رقم با فونت انتخابی و رنگ سیاه روی تصویر
    # استفاده از پارامتر anchor برای قرار دادن مرکز متن در وسط تصویر
    # استفاده از پارامتر align برای قرار دادن متن در هر خط به صورت افقی وسط
    draw.text((14, 14), digit, font=font, fill=0, anchor='mm', align='center')

    # ذخیره تصویر با نام رقم
    img.save(digit + '_calibri.png')

# باز کردن تصویر 9
img = Image.open('9_calibri.png')
# تبدیل تصویر به آرایه نامپای
img = np.array(img)
# نمایش تصویر
plt.figure()
plt.imshow(img)
plt.show()