# Automated Evaluation of Subjective Exam Answers (Prototype)

## 📌 Overview
This is a **prototype project** that automatically evaluates student answers from PDFs using **OCR + Machine Learning**.  

The system combines:
- **OCR with AWS Textract** → Extracts text from scanned answer sheets.
- **Semantic similarity scoring** → Uses Sentence Transformers (MiniLM/BERT) to compare student answers with the answer key.
- **Rubric-based scoring** → Checks for presence of key points defined by the teacher.

This is intended as a **prototype for educational AI applications**.

---

## 📂 Project Structure

# Automated Evaluation of Subjective Exam Answers (Prototype)

## Overview
This is a **prototype project** that automatically evaluates student answers from PDFs using OCR and ML. The system combines:

- **OCR** using AWS Textract to extract text from PDF answer sheets.
- **Semantic similarity scoring** using Sentence Transformers (BERT) to compare answers with the answer key.
- **Rubric-based scoring** for checking key points in student answers.

This project is ideal as a **prototype for educational AI applications**.

## Project Structure
Automated Evaluation Subjective Exam Answers ML Project
```
├── data
│ ├── students
│ │ └── answer_sheet_1.pdf
│ ├── outputs
│ │ └── qna_scores.json
│ ├── answer_key.txt
│ └── rubric.json
├── extract_text.py
├── main.py
├── scoring.py
├── util.py
└── requirements.txt
```

## ⚡ How It Works
1. **Convert PDF → Images** using PyMuPDF.  
2. **Extract Text** using **AWS Textract**.  
3. **Clean & Split Answers** into question blocks.  
4. **Evaluate** each answer using:
   - Semantic similarity with reference answer (BERT embeddings).
   - Rubric-based keyword matching.  
5. **Score & Save Results** into `data/outputs/qna_scores.json`.

## 🔑 AWS Textract Setup

This project requires **AWS Textract** for OCR.  
Make sure you have an **AWS account** and valid credentials set up.

### Steps:
1. Install AWS CLI:
   `pip install awscli boto3`
   
2. Configure AWS credentials (use your access keys):
     `aws configure`
   
   ## Enter The Following:
   - AWS Access Key ID
   - AWS Secret Access Key
   - Default region (e.g., us-east-1)
   - Output format (json)
   - Verify Textract works:
  
4. Verify Textract works:
   ```
   import boto3
   client = boto3.client('textract')
   print(client)
   ```


## ▶️ How to Run

1. **Install dependencies:**
   
     `pip install -r requirements.txt`
2. **Place student PDFs in:**
   
     `data/students/`
3. **Run the evaluation:**
   
    `python main.py `
4. **Output will be saved in:**
   
   `data/outputs/qna_scores.json`

 
## ✅ Example Output

**Extracted OCR (sample):**

```
State the properties of Eigen Vect
Ans:
* Linearly independent for distinct eigen values.
* Scalar multiples of an eigen vect are also Eigen Vectors.
* Eigen Vectors can be normalized
```
**Evaluation Results (sample):**
  ```
    Q1: 3.5/5
    Q2: 4/5
    Q3: 3.5/5
    Q4: 5/5
    Q5: 4/5
    Total Score: 20/25
  ```

