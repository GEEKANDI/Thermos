from datetime import datetime
from flask import Flask, render_template,  redirect, url_for, flash

from forms import BookmarkForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "#5|\x0f\xd7\xee\xe2\xc6\t\xe5\xc5Z%\x91\xc2w\xc4\xce'Y\xe0cv\x8c"

bookmarks = []


def store_bookmarks(url):
    bookmarks.append(dict(
        url=url,
        user="Skux",
        date=datetime.utcnow()
    ))


def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=new_bookmarks(5))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()   # instance of form class
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        store_bookmarks(url)
        flash("Stored '{}' ".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
