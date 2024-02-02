import easyocr
from PIL import Image, ImageDraw, ImageFont
# ایجاد یک شیء خواننده با زبان‌های مورد نظر
reader = easyocr.Reader(['fa','en'])

# تعریف یک تابع برای نمایش برچسب‌های واقعی و پیش‌بینی شده
def show_labels(image_path, true_labels):
  # خواندن تصویر و انجام OCR
  result = reader.readtext(image_path)
  # نمایش تصویر
  print(f"تصویر: {image_path}")
  # نمایش برچسب‌های واقعی
  print(f"برچسب‌های واقعی: {true_labels}")
  # نمایش برچسب‌های پیش‌بینی شده
  print("برچسب‌های پیش‌بینی شده:")
  for item in result:
    # استخراج متن و اطمینان از هر مورد
    text, confidence = item[1], item[2]
    # نمایش متن و اطمینان
    print(f"{text} ({confidence:.2f})")

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
# تعریف نام فونت
FONT_NAME = 'W_tahoma.ttf'
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
                font = ImageFont.truetype('fonts/W_tahoma.ttf', int(font_size / (res_y_old / res_y)))
                # محاسبه مختصات متن به پیکسل
                x, y = (int(x_cm / f * res_x), int(y_cm / f * res_y))
                # رسم متن روی تصویر
                draw.text((x, y), digit, font=font, fill=0, anchor='mm', align='center')
            # رسم متن با مختصات و اندازه فونت مشخص
            draw_text(w_cm / 2, h_cm / 2, 20)
            # ذخیره تصویر با رزولوشن مشخص
            img.save(digit + '_tahoma_' + str(w) + 'x' + str(h) + '.png', dpi=(res_x, res_y))
            # نمایش برچسب‌های واقعی و پیش‌بینی شده برای تصویر
            show_labels(digit + '_tahoma_' + str(w) + 'x' + str(h) + '.png', digit)
