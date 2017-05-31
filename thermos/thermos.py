from flask import Flask, render_template, url_for

app = Flask(__name__)


class User:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def initials(self):
        return '{}. {}.'.format(self.f_name[0], self.l_name[0])


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Passed from view',
                           user=User('Tito', 'Thumbi'))


@app.route('/add')
def add():
    return render_template('add.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html', 500)


if __name__ == "__main__":
    app.run(debug=True)
