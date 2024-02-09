# Designing a system for producing Persian numbers font

In this project, we are going to design a system for producing Persian numerals font to minimize the misrecognition of numerals in the space of changing resolution and geometric distortion, and here we used B Nazanin font.

![font](Img\B_nazanin.jpg)
---
### Usage
First install requirements packages:
```
pip install -r requirements.txt 
```
---
### OCR
With the font we chose, we generate the dataset in different resolutions, then we read the numbers inside the images with an OCR and labeled them and calculated the accuracy for each image, here we used easyocr [Easyocr](https://github.com/JaidedAI/EasyOCR)

---
### Genetic algoritm
In the next part of the project, we changed the pixels using the genetic algorithm to change the font and shape of the numbers and put the result in a folder.