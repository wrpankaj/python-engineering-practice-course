# GitHub Setup Guide

## Step 1: Create GitHub Account
Go to GitHub and sign in using your account.

## Step 2: Create New Repository
1. Click **New Repository**
2. Repository name:
   `python-engineering-practice-course`
3. Select **Public** or **Private**
4. Tick **Add a README file**
5. Click **Create Repository**

## Step 3: Upload Course Files
1. Open the repository.
2. Click **Add file**.
3. Click **Upload files**.
4. Drag and drop all course folders and files.
5. Click **Commit changes**.

## Step 4: Enable GitHub Pages for HTML Quizzes
1. Go to repository **Settings**.
2. Click **Pages**.
3. Under **Build and deployment**, choose:
   - Source: Deploy from branch
   - Branch: main
   - Folder: /root
4. Save.
5. GitHub will generate a website link.

## Step 5: Share Link with Students
Share repository link or GitHub Pages link.

## Suggested Repository Structure

python-engineering-practice-course/
│
├── README.md
├── 01_Optimization_SciPy/
│   ├── README.md
│   └── optimization_practice.py
│
├── 02_Efficiency_Problems/
│   ├── README.md
│   └── efficiency_practice.py
│
├── 03_Control_Systems/
│   ├── README.md
│   └── control_practice.py
│
├── 04_Spreadsheet_Processing/
│   ├── README.md
│   └── spreadsheet_practice.py
│
├── quizzes/
│   └── quiz_bank.md
│
└── student_submissions_template/

## Student Submission Instructions

Each student should submit:
- Python code file
- Screenshot of output
- Generated Excel file if applicable
- Short explanation of logic
