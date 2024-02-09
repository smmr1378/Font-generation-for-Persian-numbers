import pygad 
import numpy as np 
import typing as typ 
import matplotlib.pyplot as plt 
from PIL import Image 
import os 


def fitness_func(ga_instance: pygad.GA, solution: np.array, solution_idx: int) -> float:
  
    solution_reshaped = solution.reshape(original_array.shape)
    
    mse = np.mean((original_array - solution_reshaped)**2)
    
    fitness = 1.0 / (mse + 0.00000001)
   
    return fitness




def on_generation(ga_instance: pygad.GA) -> None:
   
    best_solution = ga_instance.best_solution()
  
    best_solution_reshaped = best_solution[0].reshape(original_array.shape)
    
    final_image = Image.fromarray(best_solution_reshaped.astype(np.uint8))
   
    plt.figure()
    plt.plot(ga_instance.best_solutions_fitness)
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title("Fitness Curve")
   
    plt.figure()
    plt.imshow(final_image)
    plt.title("Final Image")
    

num_generations = 100 # تعداد نسل‌ها
num_parents_mating = 10 # تعداد والدین مشارکت کننده در تولید فرزندان
sol_per_pop = 20 # تعداد راه‌حل‌ها در هر جمعیت
mutation_percent_genes = 5 # درصد ژن‌های تغییر یافته در هر راه‌حل
parent_selection_type = "rws" 
crossover_type = "single_point" 
mutation_type = "random" 
keep_parents = 0 

images_path = "output"
output_path = "output2"

# ایجاد پوشه output اگر وجود نداشته باشد
if not os.path.exists(output_path):
    os.mkdir(output_path)

# حلقه برای خواندن تصاویر از پوشه images
for image_name in os.listdir(images_path):
    # تعریف مسیر کامل تصویر
    image_path = os.path.join(images_path, image_name)
    # بارگذاری تصویر با استفاده از کتابخانه PIL
    original_image = Image.open(image_path)
    # تبدیل تصویر به آرایه نامپای
    original_array = np.asarray(original_image)
    # ایجاد نمونه از کلاس GA با پارامترهای تعریف شده
    ga_instance = pygad.GA(num_generations=num_generations,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_func,
                           sol_per_pop=sol_per_pop,
                           num_genes=original_array.size,
                           init_range_low=0,
                           init_range_high=255,
                           mutation_percent_genes=mutation_percent_genes,
                           parent_selection_type=parent_selection_type,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           keep_parents=keep_parents,
                           on_generation=on_generation)
    # شروع فرآیند تکامل
    ga_instance.run()
    # گرفتن نهایی‌ترین راه‌حل
    best_solution = ga_instance.best_solution()
    # تبدیل نهایی‌ترین راه‌حل به آرایه دو بعدی با ابعاد مشابه تصویر اصلی
    best_solution_reshaped = best_solution[0].reshape(original_array.shape)
    # تبدیل آرایه به تصویر
    final_image = Image.fromarray(best_solution_reshaped.astype(np.uint8))
    # تعریف مسیر ذخیره تصویر پردازش شده
    output_image_path = os.path.join(output_path, image_name)
    # ذخیره تصویر پردازش شده
    final_image.save(output_image_path)