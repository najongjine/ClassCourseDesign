import pypdf
import os

pdf_path = r"c:\Users\najon\OneDrive\Documents\ClassCourseDesign\인공지능학습데이터구축\인공지능학습데이터구축.pdf"

try:
    reader = pypdf.PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    with open("pdf_content.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Extraction complete. check pdf_content.txt")
except Exception as e:
    print(f"Error reading PDF: {e}")
