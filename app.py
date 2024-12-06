from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
def index():
    block_posts = load_block_posts()
    return render_template('index.html', posts=block_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        block_posts = load_block_posts()
        username = request.form.get('username')
        title = request.form.get('title')
        content = request.form.get('content')
        id = block_posts[-1]["id"] + 1
        if username != "" and title != "" and content != "":
            block_posts.append({"id": id,
                                "author": username,
                                "title": title,
                                "content": content})
            save_block_posts(block_posts)
        return render_template('index.html', posts=block_posts)  # add the post
    return render_template('add.html')

@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    block_posts = load_block_posts()
    for post in block_posts:
        if post["id"] == post_id:
            block_posts.remove(post)
            save_block_posts(block_posts)
            break
    return redirect(url_for('index'))




def load_block_posts():
    post_manager = app.config["post_manager"]
    block_posts = post_manager.load_json()
    return block_posts


def save_block_posts(block_posts):
    post_manager = app.config["post_manager"]
    post_manager.save_json(block_posts)




