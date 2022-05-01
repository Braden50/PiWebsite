from flask import render_template, request, Blueprint, jsonify
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
def home():
    # page = request.args.get('page', 1, type=int)
    # posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    r = request.form.get("red")
    g = request.form.get("green")
    b = request.form.get("blue")
    print(r,g,b)
    print("HOME")
    # return render_template('home.html', shortcode=request.form['']
    if request.method == 'POST':
        print("POST")
        form = request.form
        data = request.data
        print(form)
        print(data)
        return jsonify(message='success')
    elif request.method == 'GET':
        return render_template('home.html')
    else:
        return 'Not a valid request method for this route'


@main.route("/about")
def about():
    return render_template('about.html', title='About')
