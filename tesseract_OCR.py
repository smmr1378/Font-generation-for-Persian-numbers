import os
import re
from PIL import Image
from unidecode import unidecode
import easyocr


def ocr_accuracy(true_text, ocr_text):
    true_text = re.sub(r'\W+', '', true_text)
    ocr_text = re.sub(r'\W+', '', ocr_text)

    distance = levenshtein_distance(true_text, ocr_text)

    accuracy = (1 - distance / max(len(true_text), len(ocr_text))) * 100
    return accuracy


def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]


output_path = "output"
reader = easyocr.Reader(['fa'])

accuracy_scores = []

for filename in os.listdir(output_path):
    true_text = filename.split("_")[0]
    image = Image.open(os.path.join(output_path, filename))
    image_path = os.path.join(output_path, filename)
    ocr_text = reader.readtext(image_path)[0][1]
    ocr_text_english = unidecode(ocr_text)

    print(f"True text: {true_text}")
    print(f"OCR text: {ocr_text}")
    print(f"English OCR text: {ocr_text_english}")

    accuracy = ocr_accuracy(true_text, ocr_text_english)
    print(f"Accuracy: {accuracy:.2f}%")
    print("-" * 20)

    accuracy_scores.append(accuracy)

average_accuracy = sum(accuracy_scores) / len(accuracy_scores)
print(f"Average accuracy: {average_accuracy:.2f}%")
