import mysql.connector
from flask import Flask, redirect, render_template, request


app=Flask(__name__)

mydb = mysql.connector.connect(
    host="mysql-sportclub.mysql.database.azure.com",
    user="lytathi",
    password="ly135246.",
    database="sportclub"
)
mycursor = mydb.cursor()

@app.route('/classes')
def classes():
    query1 = "SELECT * FROM classes"
    mycursor.execute(query1)
    classes = mycursor.fetchall()
    query2 ="SELECT * FROM comments"
    mycursor.execute(query2)
    comments = mycursor.fetchall()
    return render_template("classes.html", classes=classes, comments=comments)

@app.route('/add_comments', methods=['POST'])
def add_comments():
    name = request.form["comment_name"]
    email = request.form["comment_email"]
    comment = request.form["comment"]
    query = "INSERT INTO comments(person, email, content) VALUES (%s, %s, %s)"
    mycursor.execute(query, (name, email, comment))
    mydb.commit()
    return redirect('/classes')

@app.route('/home')
def home():
    return render_template("dashboard.html")

@app.route('/classForm')
def classForm():
    query1 = "SELECT * FROM classes"
    mycursor.execute(query1)
    classes = mycursor.fetchall()
    return render_template("class.html", classes=classes)


@app.route('/addClass', methods=["POST"])
def addClass():
    className = request.form["className"]
    class_description = request.form["class_description"]
    query = "INSERT INTO classes (className, class_description) VALUES (%s,%s)"
    mycursor.execute(query, (className, class_description))
    mydb.commit()
    return redirect('/classForm')

@app.route('/memberForm')
def memberForm():
    query1 = "SELECT * FROM classes"
    mycursor.execute(query1)
    classes = mycursor.fetchall()
    return render_template('member.html', classes=classes)

@app.route('/add_member', methods=['POST'])
def addMember():
    name = request.form["name"]
    personNumber= request.form["personnumber"]
    phone = request.form["phone"]
    address = request.form["address"]
    email = request.form["email"]
    registerClass = request.form["class_name"]
    query2 = "INSERT INTO members (member_name, person_number, phone, address, email, classID) VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(query2, (name, personNumber, phone, address, email, registerClass))
    mydb.commit()
    return redirect('/memberForm')

@app.route('/')
def members():
    query = "SELECT * FROM members"
    mycursor.execute(query)
    members = mycursor.fetchall()
    return render_template("members.html", members=members)

@app.route('/remove/<int:id>', methods=['GET'])
def remove_member(id):
    query = "DELETE FROM members WHERE member_id=%s"
    mycursor.execute(query, (id,))
    mydb.commit()
    return redirect('/')

@app.route('/member_info')
def member_info():
    member_id = request.args["member"]
    query = "SELECT members.member_name, members.person_number, members.phone, members.address, members.email, members.member_id, members.classID, classes.className FROM members LEFT JOIN classes ON members.classID = classes.classID WHERE members.member_id=" +member_id
    mycursor.execute(query)
    response = mycursor.fetchone()
    query1 = "SELECT * FROM classes"
    mycursor.execute(query1)
    classes = mycursor.fetchall()
    return render_template('member_info.html', response=response, classes=classes, id=member_id)


@app.route('/edit/<int:id>', methods=['POST'])
def edit_member(id):
    name = request.form["member_name"]
    personNumber = request.form["personnumber1"]
    phone = request.form["phone1"]
    address = request.form["address1"]
    email = request.form["email1"]
    registerClass = request.form["class_name1"]
    query = "UPDATE members SET member_name=%s, person_number=%s, phone=%s, address=%s, email=%s, classID=%s WHERE member_id="+str(id)
    mycursor.execute(query,(name, personNumber, phone, address, email, registerClass,))
    mydb.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
