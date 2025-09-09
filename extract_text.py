import boto3
import fitz
import os
import re


def pdf_to_images(pdf_path, output_dir="temp_images"):
    # Check if the PDF file exists
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open the PDF
    doc = fitz.open(pdf_path)
    image_paths = []

    # Get base name without extension
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]

    # Convert each page to image
    for i in range(len(doc)):
        pix = doc[i].get_pixmap(dpi=300)
        img_path = os.path.join(output_dir, f"{base_name}_page{i + 1}.jpg")
        pix.save(img_path)
        image_paths.append(img_path)

    return image_paths




def extract_text_from_image(image_path):
    textract = boto3.client('textract')
    with open(image_path, 'rb') as f:
        image_bytes = f.read()
    response = textract.detect_document_text(Document={'Bytes': image_bytes})
    return "\n".join([b['Text'] for b in response['Blocks'] if b['BlockType'] == 'LINE'])




def extract_student_answers(pdf_path):
    images = pdf_to_images(pdf_path)
    full_text = ""
    for img in images:
        full_text += extract_text_from_image(img) + "\n"
        os.remove(img)

    print("\nOCR EXTRACTED TEXT:\n")
    print(full_text[:2000])

    # Step 1: Clean up consecutive lines and normalize
    lines = full_text.splitlines()
    cleaned_lines = [line.strip() for line in lines if line.strip()]

    # Step 2: Find lines where a question starts
    q_indices = []
    for idx, line in enumerate(cleaned_lines):
        if re.match(r'^\d$', line):  # line is just 1, 2, 3, 4, 5
            if idx + 1 < len(cleaned_lines) and len(cleaned_lines[idx + 1].split()) > 4:
                q_indices.append(idx)

    # Step 3: Extract answer blocks using those indices
    answers = []
    for i in range(len(q_indices)):
        start = q_indices[i]
        end = q_indices[i + 1] if i + 1 < len(q_indices) else len(cleaned_lines)
        answer_block = "\n".join(cleaned_lines[start:end])
        answers.append(answer_block.strip())
    print("Student Answers :")
    for i in answers:
        print(i)
        print()
    print(f"\nExtracted {len(answers)} answers from PDF")
    return answers


pdf_to_images(r"data\students\qna[1].pdf")