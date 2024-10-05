from flask import Flask, render_template,request,url_for
from flask_mysqldb import MySQL,MySQLdb

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mysqldb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route("/",methods=["POST","GET"])
def index():
    if request.method == 'POST':
        Key = request.form["Key"]
        return   render_template(url_for('result',Key=Key))
    return render_template("index.html")

@app.route("/result",methods=["POST","GET"])
def result():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    Key = request.form["Key"]
    if request.method == 'POST':
        if Key =="":
           license_key = "SELECT * from users WHERE name LIKE '%{}%'  ORDER BY id DESC LIMIT 20".format(Key)
           cur.execute(license_key)
           license_key = cur.fetchall()
           if Key == license_key[0-3]:
               print("Found!")
           else:
               print("Not Found!")
        else:
            render_template('indexs.html')
    return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)
     