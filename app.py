from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:@localhost/mscs"

db = SQLAlchemy(app)

class Mentor(db.Model):
    # mid mname mon tue wed thu fri sat

    mid = db.Column(db.Integer, primary_key=True)
    mname = db.Column(db.String(100), nullable=False)
    mon = db.Column(db.String(50), nullable=True)
    tue = db.Column(db.String(50), nullable=True)
    wed = db.Column(db.String(50), nullable=True)
    thu = db.Column(db.String(50), nullable=True)
    fri = db.Column(db.String(50), nullable=True)
    sat = db.Column(db.String(50), nullable=True)

class Student(db.Model):
    # roll_no name mid attendance phone_no email

    roll_no = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mid = db.Column(db.Integer, nullable=True)
    attendance = db.Column(db.Float, nullable=False)
    phone_no = db.Column(db.String, nullable=False)
    email = db.Column(db.String(50), nullable=False)

class Parent(db.Model):
    # pid parent_name roll_no phoneno pemail

    pid = db.Column(db.String(5), primary_key=True)
    parent_name = db.Column(db.String(100), nullable=True)
    roll_no = db.Column(db.String(50), nullable=True)
    phoneno = db.Column(db.String, nullable=False)
    pemail = db.Column(db.String(50), nullable=False)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/student", methods=['GET', 'POST'])
def student_section():
    if request.method == "POST":
        student_roll_no = request.form.get("stu_roll")
        
        mentor_id = db.session.execute(db.select(Student.mid).filter_by(roll_no=student_roll_no)).scalar_one()
        details = Mentor.query.filter_by(mid=mentor_id).all()
        return render_template("student.html", details=details)
        
    return render_template("student.html")

@app.route("/mentor", methods=['GET', 'POST'])
def mentor_section():
    if request.method == "POST":
        mentor_name = request.form.get("ment_name")
        
        mentor_id = db.session.execute(db.select(Mentor.mid).filter_by(mname=mentor_name)).scalar_one()
        det = Student.query.filter_by(mid=mentor_id).all()
        return render_template("mentor.html", det=det)
    
    return render_template("mentor.html")

@app.route("/addstu", methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        roll = request.form['roll_no']
        name = request.form['stu_name']
        mid = request.form['mid']
        phone = request.form['ph_no']
        email = request.form['email']
        attendance = request.form['attendance']

        det = Student(roll_no=roll, name=name, mid=mid, phone_no=phone, email=email, attendance=attendance)
        db.session.add(det)
        db.session.commit()
        
        return redirect("/mentor")
    return render_template("add.html")

@app.route('/update/<string:roll_no>', methods=['GET', 'POST'])
def update(roll_no):
    if request.method == "POST":
        roll = request.form['roll_no']
        name = request.form['stu_name']
        mid = request.form['mid']
        phone = request.form['ph_no']
        email = request.form['email']
        attendance = request.form['attendance']

        det = Student.query.filter_by(roll_no=roll_no).first()

        det.roll_no = roll
        det.name = name
        det.mid = mid
        det.phone_no = phone
        det.email = email
        det.attendance = attendance
        db.session.add(det)
        db.session.commit()
        return redirect("/mentor")
    
    det = Student.query.filter_by(roll_no=roll_no).first()
    return render_template("update.html", det=det)

@app.route('/delete/<string:roll_no>')
def delete(roll_no):
    del_stu = Student.query.filter_by(roll_no=roll_no).first()
    db.session.delete(del_stu)
    db.session.commit()
    return redirect("/mentor")

@app.route('/show/<string:roll_no>')
def show(roll_no):
    det = Parent.query.filter_by(roll_no=roll_no).all()
    return render_template("mentor.html", det=det)

if __name__ == "__main__":
    app.run(debug=True)
