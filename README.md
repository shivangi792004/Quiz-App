# 🎯 Section-Wise Online Quiz Platform

A full-featured **exam-style quiz web application** built using **Flask, HTML, CSS, and JavaScript**.  
The platform supports **multiple quiz sections**, **timed assessments**, **progress tracking**, and a **modern responsive UI**.

---

## 🚀 Features

### ✅ Core Functionality
- Section-wise quizzes (DSA, OOPS, DBMS, OS, Python, Java, JavaScript)
- 20-minute countdown timer with auto-submit
- Score and percentage calculation
- Highest score tracking (session-based)
- Detailed answer review (correct / wrong)

### 🎨 UI / UX Features
- One-question-at-a-time exam interface
- Next / Previous navigation
- Question palette (jump to any question)
- Progress bar for quiz completion
- Auto-save answers (safe on refresh)
- Dark / Light mode toggle
- Fully responsive design
- Custom logo and favicon

---

## 🛠 Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML5, CSS3, JavaScript  
- **Templating Engine:** Jinja2  
- **State Handling:** Flask Sessions, Browser LocalStorage  

---

## 📂 Project Structure

quiz_app/
│
├── app.py
├── quiz_data.py
│
├── templates/
│ ├── index.html
│ ├── quiz.html
│ └── result.html
│
├── static/
│ ├── style.css
│ └── images/
│ ├── logo.png
│ └── favicon.png
│
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone <repository-link>
cd quiz_app
```
2️⃣ Install Dependencies
```
pip install flask
```
3️⃣ Run the Application
```
python app.py
```
4️⃣ Open in Browser
```
http://127.0.0.1:5000
```

🧪 Application Flow

User selects a quiz section
Quiz starts with a 20-minute timer
Questions are shown one by one

User can:
Navigate questions
Jump using question palette
Refresh safely (answers auto-saved)

On submit or timeout:
Score and percentage displayed
Highest score updated
Detailed answer review shown

🧠 Learning Outcomes

Flask routing and templating
Frontend–backend integration
JavaScript-based timers and navigation
UI/UX design for exam platforms
Debugging real-world issues (Jinja, JS, CSS)
Writing production-ready web applications

👤 Author

Shivangi Singh
B.Tech CSE | 2026 Batch
Skills: Python, Flask, HTML, CSS, JavaScript
