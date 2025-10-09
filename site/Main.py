from flask import Flask, render_template, request
import sqlite3



app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catalog/')
def catalog():
    coon = sqlite3.connect("database.db")
    tovar = coon.execute('select * from avto').fetchall()
    print(tovar)
    coon.close()
    return render_template('catalog.html', tovar = tovar)

@app.route("/add/<id>" , methods=['post', 'get'])
def Add(id):
    if request.method == 'POST':
        user = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        print(user)
        coon = sqlite3.connect("database.db")
        sql = f'INSERT INTO zakazy (name_user,email,number) VALUES ("{user}","{email}","{number}")'
        print(sql)
        coon.execute(sql)
        coon.commit()
        print("Отпрака данных прошла")
        coon.close()
        
         
    coon = sqlite3.connect("database.db")
    tovar = coon.execute('select * from avto WHERE id = ' + id).fetchall()
    #print(tovar)
    coon.close()
    return render_template("form.html",tovar = tovar )


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)