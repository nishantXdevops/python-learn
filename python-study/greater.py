a=10
b=200
c=50
d=30

if a<b:
    print("a bada h")
else:
    print("b bda h")

# # if a>b:
# #     if a>c:
# #         print("a is greater among three")
# #     else:
# #         print("c is greater among three")
# # else:
# #     if b>c:
# #         print("b is greater ")
# #     else:
# #         print("c is greater")

# if (a>=b) and (a>=c):
#     print("a is greater")
# elif (b>=c):
#      print("b is greater")
# else:
#      print("c is greater")    


# # if a>b:
# #     if b>c:
# #         if c>d:
# #             print("c bada h") 
# #         else:
# #             print("b is greater") 
# #     else:
# #         print("c is greater") 
# # else:
# #     print("d is greater")    



from PIL import Image
import pytesseract
from pdf2image import convert_from_path

# Corrected file path with forward slashes (Linux-style)
pdf_path = "/mnt/c/Users/pk226/Downloads/4003_23.pdf"

# Convert PDF pages to images
images = convert_from_path(pdf_path)

# Use OCR to extract text from each image (English + Hindi)
text_pages = [pytesseract.image_to_string(img, lang='eng+hin') for img in images]

# Combine all extracted text into one string
full_text = "\n\n".join(text_pages)

# Preview the first 3000 characters (optional for debugging)
print(full_text[:3000])














