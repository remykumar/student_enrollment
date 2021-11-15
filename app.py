from flask import Flask, render_template, request
import os
import mysql.connector

app = Flask(__name__)

user = os.popen('cat /home/remy/.secret.txt | grep user | awk -F "=" \'{print $2}\'').read().strip()
password = os.popen('cat /home/remy/.secret.txt | grep password | awk -F "=" \'{print $2}\'').read().strip()
host = os.popen('cat /home/remy/.secret.txt | grep host | awk -F "=" \'{print $2}\'').read().strip()
database = os.popen('cat /home/remy/.secret.txt | grep "database=" | awk -F "=" \'{print $2}\'').read().strip()
conn = mysql.connector.connect(user=''+user+'',password=''+password+'',host=''+host+'',database=''+database+'', auth_plugin='mysql_native_password') 

@app.route("/", methods =['GET', 'POST'])
def index():
    if request.method == "POST" or request.method == "post":
     enrollment = request.form 
     ids = enrollment['ids']
     firstName = enrollment['firstName']
     lastName = enrollment['lastName']
     quarter = enrollment['quarter']
     cur = conn.cursor(buffered=True) 
     insert_query = """INSERT INTO registrations(ID, FirstName, LastName, Quarter) VALUES (%s, %s, %s, %s) """
     record = (ids, firstName, lastName, quarter)
     cur.execute(insert_query,record)
     conn.commit()
     cur.close() 
     return 'Successfully Enrolled\n' 
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

