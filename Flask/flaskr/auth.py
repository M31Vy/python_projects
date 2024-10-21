import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from flaskr.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = (
            get_db().execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
        )


@bp.route("/register", methods=("GET", "POST"))
def register():
    """Register a new user.

    Validates that the username is not already taken. Hashes the
    password for security.
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                # The username was already taken, which caused the
                # commit to fail. Show a validation error.
                error = f"User {username} is already registered."
            else:
                # Success, go to the login page.
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None
        user = db.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user["password"], password):
            error = "Incorrect password."

        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("index"))

        flash(error)

    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for("index"))



from distutils.log import debug
from fileinput import filename
import os
import pandas as pd
import pymysql
from pymysql.converters import escape_string

@bp.route('/upload')  
def upload():  
    return render_template("auth/upload.html")

@bp.route('/success', methods = ['GET','POST'])
def success():
    if request.method == 'POST':  
        f = request.files['file']
        f.save(os.path.join("Downloads",f.filename))

        # for row in f.iterrows():
        #     print(row['name'],row['gender'])

        # 读取 Excel 数据
        data = pd.read_excel("Downloads/"+f.filename)

        # data = json_data.values.tolist()
        # for i in data:
        #     print(i)

        conn = pymysql.connect(host="localhost",
                       port=3306,
                       user="XXX",
                       password="XXXXXX")

        cursor = conn.cursor()
        conn.select_db("mydb1")

        # command = f"""
        # LOAD DATA INFILE {data}
        # INTO TABLE 'student'
        # FIELDS TERMINATED BY ',' ENCLOSED BY '"'
        # LINES TERMINATED BY '\n';
        # """

        for _,row in data.iterrows():
            print(row['name'], row['gender']) 
            command = "INSERT INTO student3 (sid,name,gender) values({},'{}','{}')".format(row['sid'],escape_string(row['name']),escape_string(row['gender']))
            print(command)
            cursor.execute(command)

        # for _,row in data.iterrows():
        #     cursor.execute("INSERT INTO student3 (sid, name, gender) VALUES (?, ?, ?)",(row["sid"],row["name"],row["gender"]))
        conn.commit()
        conn.close()

        # json_1 = open("Downloads/json_1.txt",'w',encoding='UTF-8')
        # json_1.write(json_data)
        # json_1.close()

        return render_template("auth/Acknowledgement.html", name = f.filename)