from flask import Flask, redirect, render_template, request
from imdb import Cinemagoer
from cs50 import SQL
from api import search_result, get_detail, get_top_rated, get_upcoming, insert_list, get_now_playing, get_popular, get_trending
import urllib.parse

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
db = Cinemagoer()
li = SQL("sqlite:///list.db")
@app.route("/")
def home():
    playing = get_now_playing()
    popular = get_popular()
    trending = get_trending()
    return render_template('home.html', playing=playing, popular=popular, trending=trending)

@app.route("/list", methods = ["GET","POST"])
def index():
    list = li.execute("SELECT * FROM list ORDER BY id DESC")
    if request.method == "POST":
        id = request.form.get("id")
        detail = get_detail(id)
        insert_list(detail, li)
        print(id)
        return redirect("/list")
    else:
        return render_template("index.html", list=list)
@app.route("/search", methods = ["GET"])
def search():
    top = get_top_rated()
    upcoming = get_upcoming()
    return render_template("search.html", top=top, upcoming=upcoming)
@app.route("/result", methods = ["GET","POST"])
def result():
    page = request.args.get('page', 1, type=int)
    if request.method == "POST":
        search = request.form.get("search") 
    else:
        search = request.args.get("search") 
    encoded_search = urllib.parse.quote(search.encode("utf-8")) if search else ""
    data = search_result(search, page)
    mov = data["results"]
    max_page = data["total_pages"]
    return render_template("result.html", mov=mov, page=page, text = search, search=encoded_search, max_page=max_page)

@app.route("/detail", methods = ["GET", "POST"])
def detail():
    if request.method == "POST":
        id = request.form.get('id')
        detail = get_detail(id)
        return render_template("detail.html", detail=detail)
    else:
        return render_template("detail.html")

@app.route("/delete", methods = ["GET","POST"])
def delete():
    if request.method == "POST":
        movie_id = request.form.get("movie_id")
        li.execute("DELETE FROM list WHERE movie_id = ?", movie_id)
        return redirect('/list')
    else:
        return redirect('/list')

if __name__ == ('__main__'):
    app.run()