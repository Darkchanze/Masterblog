from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)


@app.route('/')
def index():
    """
    Displays the home page with all posts.

    Loads all posts and renders the `index.html` template.
    """
    block_posts = load_block_posts()
    return render_template('index.html', posts=block_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Adds a new post.

    If the request is a POST request, a new post is added and the home page is
    displayed with the new post. If its a GEt request, the form for adding a post is shown.
    """
    if request.method == 'POST':
        block_posts = load_block_posts()
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')
        id = block_posts[-1]["id"] + 1
        if author != "" and title != "" and content != "":
            block_posts.append({"id": id,
                                "author": author,
                                "title": title,
                                "content": content})
            save_block_posts(block_posts)
        return render_template('index.html', posts=block_posts)  # add the post
    return render_template('add.html')


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id: int):
    """
    Deletes a post by its ID.

    Searches for the post with the given ID, removes it from the list,
    and saves the modified posts to the JSON file.
    """
    block_posts = load_block_posts()
    for post in block_posts:
        if post["id"] == post_id:
            block_posts.remove(post)
            save_block_posts(block_posts)
            break
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id: int):
    """
     Updates an existing post.

     If the request is a POST request, the post is updated with the new data
     and the changes are saved. If its a GEt request, the form for editing the post is shown.
     """
    selected_post = fetch_post_by_id(post_id)
    if selected_post is None:
        return "Post not found", 404

    if request.method == 'POST':
        block_posts = load_block_posts()
        for post in block_posts:
            if post["id"] == post_id:
                post['author'] = request.form.get('author')
                post['title'] = request.form.get('title')
                post['content'] = request.form.get('content')
                save_block_posts(block_posts)
                break
        return redirect(url_for('index'))
    return render_template('update.html', post = selected_post)


def load_block_posts():
    """
    Loads the posts from the JSON file using the PostManager.

    :return: A list of posts.
    """
    post_manager = app.config["post_manager"]
    block_posts = post_manager.load_json()
    return block_posts


def save_block_posts(block_posts: list):
    """
    Saves the given posts to the JSON file using the PostManager.

    :param block_posts: A list of posts to be saved.
    """
    post_manager = app.config["post_manager"]
    post_manager.save_json(block_posts)


def fetch_post_by_id(post_id: int):
    """
    Fetches a post by its ID.

    :param post_id: The ID of the post to be fetched.
    :return: The post if found, otherwise None.
    """
    block_posts = load_block_posts()
    try:
        for post in block_posts:
            if post["id"] == post_id:
                return post
    except (KeyError, TypeError):
        return None


@app.errorhandler(404)
def page_not_found(error):
    """Displays the error page, if a 404 is caught."""
    return render_template('404.html'), 404
