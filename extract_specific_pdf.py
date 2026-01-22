import pypdf
import os

pdf_path = r"c:\Users\itg\Documents\ClassCourseDesign\인공지능모델링\2001070304_23v2 인공지능 데이터 전처리.pdf"
output_path = "pdf_extracted_module1.txt"

print(f"Extracting from {pdf_path}...")
try:
    reader = pypdf.PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Extraction complete. Saved to {output_path}")
    print(f"Extracted {len(text)} characters.")
except Exception as e:
    print(f"Error reading PDF: {e}")
