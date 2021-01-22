from flask import Flask, render_template, request
from flask import Flask, render_template, json, request
from flask_mysqldb import MySQL
from werkzeug import generate_password_hash, check_password_hash
import pymysql
import sys
import pymysql.cursors
from flask import Flask, render_template, request, redirect
from flask import Flask, render_template, request
from flask import flash
from werkzeug import secure_filename
from flask import Flask, session, redirect, url_for, escape, request
#from settings import PROJECT_ROOT
#import pyqrcode
import os

#import mysql.connector
app = Flask(__name__)

#UPLOAD_FOLDER = url_for('static',='/uploads')

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='softwaredisplaydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def user():
   return render_template('home.html')

@app.route('/adlogin',methods = ['POST', 'GET'])
def adlogin():
    return render_template("adminlogin.html")

@app.route('/ulog',methods = ['POST', 'GET'])
def ulog():
    return render_template("login.html")

@app.route('/reg',methods = ['POST', 'GET'])
def reg():
    return render_template("register.html")

@app.route('/contact',methods = ['POST', 'GET'])
def contact():
    return render_template("contact.html")

@app.route('/adminentry',methods = ['POST', 'GET'])
def adminentry():
    try:
        with connection.cursor() as cursor:
            sql1 = "select * from softwares"
            cursor.execute(sql1)
            data1 = cursor.fetchall()
            connection.commit()
            # return data1 # render_template("addcourse.html", data=data)
    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        #  cursor.close()
        # connection.close()
        return render_template("adminentry.html", data1=data1)


@app.route('/search1',methods = ['POST', 'GET'])
def search1():
    try:
        name= request.form["name"]
        with connection.cursor() as cursor:
            sql1 = "select * from softwares where sname like %s"
            cursor.execute(sql1,"%" + name + "%")
            data1 = cursor.fetchall()


            connection.commit()
    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        #  cursor.close()
        # connection.close()
        return render_template("userviewsoftwares.html", data=data, authors=authors,publishers=publishers,years=years)

@app.route('/select', methods=['GET','POST'])
def selectDisplay():
     i = int(request.args.get('id'))
     # do things according to value of i

     return render_template('display.html', response = deserialized_bug_data['list_of_turns'])

@app.route('/searchAuthor',methods = ['POST', 'GET'])
def searchAuthor():
    try:
       # i = int(request.args.get('author'))

        name1 = request.args.get('author') #request.form["author"]
        with connection.cursor() as cursor:
            sql = "select * from softwares where author=%s"
            cursor.execute(sql,name1 )
            data = cursor.fetchall()

            sql1 = "select distinct author from softwares"
            cursor.execute(sql1)
            data1 = cursor.fetchall()
            authors = data1;

            sql2 = "select distinct author from softwares"
            cursor.execute(sql2)
            data2 = cursor.fetchall()
            publishers = data2;

            sql3 = "select distinct pub_year from softwares"
            cursor.execute(sql3)
            data3 = cursor.fetchall()
            years = data3;

            connection.commit()


    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        #  cursor.close()
        # connection.close()
        return render_template("userviewsoftwares.html", data=data, authors=authors,publishers=publishers,years=years)



@app.route('/searchPrice',methods = ['POST', 'GET'])
def searchPrice():
    try:
       # i = int(request.args.get('author'))

        name1 = request.args.get('pricetype') #request.form["author"]
        with connection.cursor() as cursor:
            if name1=="Low to High":
                sql = "select * from softwares order by price "
            else:
                sql = "select * from softwares order by price desc"


            cursor.execute(sql)
            data = cursor.fetchall()

            sql1 = "select distinct author from softwares"
            cursor.execute(sql1)
            data1 = cursor.fetchall()
            authors = data1;

            sql2 = "select distinct author from softwares"
            cursor.execute(sql2)
            data2 = cursor.fetchall()
            publishers = data2;

            sql3 = "select distinct pub_year from softwares"
            cursor.execute(sql3)
            data3 = cursor.fetchall()
            years = data3;


            connection.commit()
    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        #  cursor.close()
        # connection.close()
        return render_template("userviewsoftwares.html", data=data, authors=authors,publishers=publishers,years=years)




@app.route('/search3',methods = ['POST', 'GET'])
def search3():
    try:
       # i = int(request.args.get('author'))

        publisher3 = request.args.get('publisher3') #request.form["author"]
        year = request.args.get('year')
        with connection.cursor() as cursor:
            sql = "select * from softwares where author=%s and pub_year=%s"
            cursor.execute(sql,(publisher3,year))
            data = cursor.fetchall()

            sql1 = "select distinct author from softwares"
            cursor.execute(sql1)
            data1 = cursor.fetchall()
            authors = data1;

            sql2 = "select distinct author from softwares"
            cursor.execute(sql2)
            data2 = cursor.fetchall()
            publishers = data2;

            sql3 = "select distinct pub_year from softwares"
            cursor.execute(sql3)
            data3 = cursor.fetchall()
            years = data3;

            connection.commit()


    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        #  cursor.close()
        # connection.close()
        return render_template("userviewsoftwares.html", data=data, authors=authors,publishers=publishers,years=years)




@app.route('/search4',methods = ['POST', 'GET'])
def search4():
    try:
        with connection.cursor() as cursor:
            sql = "select * from softwares order by author,pub_year"
            cursor.execute(sql)
            data = cursor.fetchall()

            sql1 = "select distinct author from softwares"
            cursor.execute(sql1)
            data1 = cursor.fetchall()
            authors = data1;

            sql2 = "select distinct author from softwares"
            cursor.execute(sql2)
            data2 = cursor.fetchall()
            publishers = data2;

            sql3 = "select distinct pub_year from softwares"
            cursor.execute(sql3)
            data3 = cursor.fetchall()
            years = data3;

            connection.commit()
    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        #  cursor.close()
        # connection.close()
        return render_template("userviewsoftwares.html", data=data, authors=authors,publishers=publishers,years=years)


@app.route('/asigninclick',methods = ['POST', 'GET'])
def asigninclick():
    try:
        name = request.form["email"]
        pwd = request.form["pwd"]
        qr = pyqrcode.create(name)
        qr.png(pwd, scale=8)
    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        #  cursor.close()
        # connection.close()
        return render_template("adminhome.html")


@app.route('/adminhome', methods=['POST', 'GET'])
def adminhome():
    return render_template("adminhome.html")

@app.route('/userhome', methods=['POST', 'GET'])
def userhome():
    return render_template("userhome.html")

@app.route('/regclick', methods=['POST', 'GET'])
def regclick():
        try:
            if request.method == 'POST':
                p1 = request.form["fname"]
                p2= request.form["lname"]
                p3= request.form["age"]
                p4= request.form["gender"]
                p5= request.form["email"]
                p6 = request.form["native"]
                p7 = request.form["ph"]
                p8 = request.form["pwd"]
                # validate the received values
                if p1 and p2:

                    try:
                        with connection.cursor() as cursor:
                            # _hashed_password = generate_password_hash(pwd)
                            # Read a single record
                            sql = "INSERT INTO user VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                            cursor.execute(sql, (p1, p2, p3, p4, p5, p6, p7, p8))
                            connection.commit()
                    except Exception as e:
                        print(str(e))
                    finally:
                        connection.close()
                        return "Saved successfully."
                    data = cursor.fetchall()

                else:
                    return json.dumps({'html': '<span>Enter the required fields</span>'})

        except Exception as e:
            return json.dumps({'error': str(e)})

        finally:
            # cursor.close()
            return render_template("login.html")
        connection.close()

@app.route('/bookclick', methods=['POST', 'GET'])
def bookclick():
        try:
            if request.method == 'POST':
                p1 = request.form["sid"]
                p2= request.form["sname"]
                p3= request.form["author"]
                p4= request.form["version"]
                p5= request.form["pub_year"]
                p6 = request.form["price"]
                # validate the received values
                if p1 and p2:

                    try:
                        with connection.cursor() as cursor:
                            # _hashed_password = generate_password_hash(pwd)
                            # Read a single record
                            sql = "INSERT INTO softwares VALUES (null, %s, %s, %s, %s, %s, %s)"
                            cursor.execute(sql, (p1, p2, p3, p4, p5, p6))
                            connection.commit()
                            sql = "select * from softwares"
                            cursor.execute(sql)
                            data1 = cursor.fetchall()
                            connection.commit()
                            return render_template("adminentry.html", data1=data1)
                    except Exception as e:
                        print(str(e))
                else:
                    return json.dumps({'html': '<span>Enter the required fields</span>'})

        except Exception as e:
            return json.dumps({'error': str(e)})

        finally:
            # cursor.close()
            return render_template("adminentry.html", data1=data1)



@app.route('/asigninclick1', methods=['POST', 'GET'])
def asigninclick1():
    if request.method == 'POST':
        try:
            email = request.form["email"]
            pwd = request.form["pwd"]
            # validate the received values
            if email and pwd:
                connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='softwaredisplaydb',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
                with connection.cursor() as cursor:
                    # Read a single record
                    # res = "select * from signup where email=%s and pwd=%s"
                    sql = "select * from adminlogin where uname=%s and pwd=%s"
                    cursor.execute(sql, (email, pwd))
                    res = cursor.fetchall()
                    if len(res) == 1:
                        connection.commit()
                        connection.close()
                        return render_template('adminhome.html')

                    else:
                        flash('Invalid', 'success')
                        error = "Invalid login"
                        connection.commit()
                        connection.close()
                        return "Invalid login"

        except Exception as e:
            return json.dumps({'error': str(e)})



@app.route('/usigninclick1', methods=['POST', 'GET'])
def usigninclick1():
    if request.method == 'POST':
        try:
            email = request.form["email"]
            pwd = request.form["pwd"]

            # validate the received values
            if email and pwd:
                connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='softwaredisplaydb',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
                with connection.cursor() as cursor:
                    # Read a single record
                    # res = "select * from signup where email=%s and pwd=%s"
                    sql = "select * from user where email=%s and pwd=%s"
                    cursor.execute(sql, (email, pwd))
                    res = cursor.fetchall()
                    if len(res) == 1:
                        connection.commit()
                        connection.close()
                        session['username']=email
                        return render_template('userhome.html')

                    else:
                        error = "Invalid login"
                        connection.commit()
                        connection.close()
                        return "Invalid login"


        except Exception as e:
            return json.dumps({'error': str(e)})

@app.route('/viewuser', methods=['POST', 'GET'])
def viewuser():
            try:
                with connection.cursor() as cursor:
                    sql = "select * from user"
                    cursor.execute(sql)
                    data = cursor.fetchall()
                    return render_template("adminview.html", data=data)
            except Exception as e:
                return json.dumps({'error': str(e)})

@app.route('/adeletefees/<int:id>',methods = ['POST', 'GET'])
def adeletefees(id):
    try:
       if request.method == 'GET':
          # validate the received values
          if id:
              try:
                  connection = pymysql.connect(host='localhost',
                                               user='root',
                                               password='',
                                               db='softwaredisplaydb',
                                               charset='utf8mb4',
                                               cursorclass=pymysql.cursors.DictCursor)
                  with connection.cursor() as cursor1:
                      # Read a single record
                      sql = "delete from softwares where id=%s"
                      cursor1.execute(sql, (id))
                      connection.commit()
                      sql = "select * from softwares"
                      cursor1.execute(sql)
                      data12 = cursor1.fetchall()
                      connection.commit()
                      return render_template("adminentry.html", data1=data12, eid=0)
                      #return render_template("adminviewusers.html", data=data, eid=0)
              except Exception as e:
                  print(str(e))
          else:
              return json.dumps({'html': '<span>Enter the required fields</span>'})

    except Exception as e:
       return json.dumps({'error': str(e)})





@app.route('/adminview', methods=['POST', 'GET'])
def adminview():
            try:
                with connection.cursor() as cursor:
                    sql = "select * from softwares"
                    cursor.execute(sql)
                    data = cursor.fetchall()
                    return render_template("adminviewsoftwares.html", data=data)
            except Exception as e:
                return json.dumps({'error': str(e)})

@app.route('/userview1', methods=['POST', 'GET'])
def userview1():
            try:
                with connection.cursor() as cursor:
                    sql = "select * from softwares"
                    cursor.execute(sql)
                    data = cursor.fetchall()

                    sql1 = "select distinct author from softwares"
                    cursor.execute(sql1)
                    data1 = cursor.fetchall()
                    authors = data1;

                    sql2 = "select distinct author from softwares"
                    cursor.execute(sql2)
                    data2 = cursor.fetchall()
                    publishers = data2;

                    sql3 = "select distinct pub_year from softwares"
                    cursor.execute(sql3)
                    data3 = cursor.fetchall()
                    years = data3;
                    return render_template("userviewsoftwares.html", data=data, authors=authors,publishers=publishers,years=years)



            except Exception as e:
                return json.dumps({'error': str(e)})


if __name__ == '__main__':
   app.secret_key = "sadfsdfdfssdfadsfsdfsd"
   app.run(port=5011)