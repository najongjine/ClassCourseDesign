import fitz
import sys

pdf_path = r"c:\Users\najon\OneDrive\Documents\ClassCourseDesign\Books\AI윤리및보안준수\[KISDI] 일반 인공지능 윤리교육 교재(단면).pdf"
out_path = r"c:\Users\najon\OneDrive\Documents\ClassCourseDesign\Books\AI윤리및보안준수\extracted.txt"

doc = fitz.open(pdf_path)
with open(out_path, "w", encoding="utf-8") as f:
    for i in range(min(10, len(doc))):
        f.write(f"--- Page {i} ---\n")
        f.write(doc[i].get_text() + "\n")
    if len(doc) > 10:
        f.write("--- Second Last Page ---\n")
        f.write(doc[-2].get_text() + "\n")
        f.write("--- Last Page ---\n")
        f.write(doc[-1].get_text() + "\n")
