# 🏫 MSCS - Mentor-Student Communication System

## 📌 Overview

MSCS is a web application designed to facilitate communication and management between mentors, students, and parents. It provides features for managing student details, mentor schedules, and parent information. This project is built using Flask, SQLAlchemy, and MySQL.

---

## ✨ Features

- **Mentor Management**:
  - View mentor schedules.
  - Assign students to mentors.
- **Student Management**:
  - Add, update, and delete student details.
  - View assigned mentor details.
- **Parent Management**:
  - View parent contact information.
- **Interactive UI**:
  - Responsive design using CSS.
  - Dynamic templates with Jinja2.
- **Database Integration**:
  - MySQL for storing mentor, student, and parent data.

---

## 🛠️ Technologies Used

- **Backend**:
  - Flask
  - SQLAlchemy
  - MySQL
- **Frontend**:
  - HTML for structure
  - CSS for styling
  - Jinja2 for server-side rendering
- **Database**:
  - MySQL for data storage

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python (v3.8 or higher)
- pip (comes with Python)
- MySQL
- Git

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Sri-Galaxy/mscs.git
cd mscs
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Database
- Create a MySQL database named `mscs`.
- Import the SQL files located in the `static` folder:
  - `msc_mentor.sql`
  - `msc_student.sql`
  - `msc_parent.sql`

### 4. Run the Application
```bash
python app.py
```

The application will be available at:
- `http://localhost:5000`

---

## 📁 Project Structure
```
mscs/
├── static/              # Static files
│   ├── add-style.css    # CSS for add student page
│   ├── ment-style.css   # CSS for mentor page
│   ├── stu-style.css    # CSS for student page
│   ├── style.css        # General CSS
│   ├── bg2.png          # Background image
│   ├── Designer-Photoroom.png # Design image
│   ├── msc_mentor.sql   # Mentor table schema
│   ├── msc_student.sql  # Student table schema
│   ├── msc_parent.sql   # Parent table schema
│   └── Teacher-Teaching-Kids.png # Design image
├── templates/           # HTML templates
│   ├── add.html         # Add student page
│   ├── index.html       # Home page
│   ├── mentor.html      # Mentor page
│   ├── student.html     # Student page
│   └── update.html      # Update student page
├── app.py               # Main application file
└── requirements.txt     # Project dependencies
```

---

## 🌐 Deployment

The application can be deployed on any Python hosting platform, such as:
- Heroku
- Render
- PythonAnywhere

### Deployment Steps
1. Upload the project files to your hosting platform.
2. Configure environment variables for the database connection.
3. Start the application.

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

## 🙏 Acknowledgments

Special thanks to:
- The Flask and SQLAlchemy communities
- All contributors who help improve this project

---

*Made with ❤️ by Srinath*
