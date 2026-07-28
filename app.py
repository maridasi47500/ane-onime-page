from flask import Flask, render_template, request
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_bboxzoneouvoyager", methods=["GET","POST"])
def add_one_bboxzoneouvoyager():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into bboxzoneouvoyager (min_lat,min_lon,max_lat,max_lon,name) values (:min_lat,:min_lon,:max_lat,:max_lon,:name)",request.form)
        user = query_db('select * from bboxzoneouvoyager')
        return render_template("bboxzoneouvoyagerform.html", bboxzoneouvoyagers=user, one_user=one_user, the_title="add new bboxzoneouvoyager")
    user = query_db('select * from bboxzoneouvoyager')
    one_user = query_db("select * from bboxzoneouvoyager limit 1", one=True)
    return render_template("bboxzoneouvoyagerform.html", bboxzoneouvoyagers=user, one_user=one_user, the_title="add new bboxzoneouvoyager")

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user (username,email,password,country_id,phone,pic,bboxzoneouvoyager_id,transport_mode) values (:username,:email,:password,:country_id,:phone,:pic,:bboxzoneouvoyager_id,:transport_mode)",request.form)
        user = query_db('select * from user')
        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")
    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")

@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into country (name) values (:name)",request.form)
        user = query_db('select * from country')
        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")
    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_post", methods=["GET","POST"])
def add_one_post():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into post (title,content,lat,lon,location,pic,user_id) values (:title,:content,:lat,:lon,:location,:pic,:user_id)",request.form)
        user = query_db('select * from post')
        return render_template("postform.html", posts=user, one_user=one_user, the_title="add new post")
    user = query_db('select * from post')
    one_user = query_db("select * from post limit 1", one=True)
    return render_template("postform.html", posts=user, one_user=one_user, the_title="add new post")

