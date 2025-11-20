# CRUD Project for Candidate Recruitment

This project is a simple **CRUD (Create, Read, Update, Delete)** application for managing candidate recruitment data.  
It is built using **pure Python** without any frameworks, and stores data in a local text file (`data.txt`).  
This project is perfect for learning basic Python file handling, data processing, and building console-based applications.

---

## 📌 Features

- **Create Candidate Data**  
  Add new candidate information such as name, birthdate, gender, position applied, psikotest scores.

- **Read Candidate Data**  
  Display all stored candidates in a clean and formatted console table.

- **Update Candidate Data**  
  Modify specific fields (name, birthdate, gender, scores, etc.) for any candidate.

- **Delete Candidate Data**  
  Remove candidate information based on PK (primary key) or called order "No" using a safe temporary file method.

- **Data Storage**  
  Uses a simple text file `data.txt` with comma-separated values.

---

## 📁 Project Structure

📁 CRUD Project for Candidate Recruitment/
│
├── main.py
├── data.txt
├── README.md
│
└── CRUD/
    ├── __init__.py
    ├── Database.py
    ├── Input.py
    └── View.py
---

## 🚀 How to Run

1. Make sure you have Python installed (version 3.9+ recommended).
2. Navigate to the project folder:
3. Run the main script : main.py (python main.py in terminal)


---

## 🛠 Requirements

This project does not require external packages.  
Everything is built using **standard Python libraries**.

---

## 📌 Example Data Format

`data.txt` stores values in this structure:
pk/ID, date_created, name, birthdate, age, gender, position, score_psikotes, score_teknikal, score_wawancara, kecocokan

Example entry:
158573,2025-11-18,DUDIH,1995-11-10,30,L,HRD,100.0,100.0,100.0,100%


---

## 💡 Learning Outcomes

By exploring this project, you will learn:

- File handling in Python (`open`, read/write, rename, etc.)
- Data parsing using string manipulation
- Console UI formatting with f-strings
- Building modular projects with packages
- Basic CRUD logic and flow

---

## 📜 License

This project is open-source.  
Feel free to modify and improve it as needed.
