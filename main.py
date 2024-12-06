from app import app
from storage_json import PostManager
import os

FILE_PATH = os.path.join("templates", "posts.json")


def main():
    """
    Initializes the PostManager and starts the Flask application.

    The PostManager is initialized with the given file path and added to the Flask
    app configuration. Then the Flask application is started.
    """
    post_manager = PostManager(FILE_PATH)
    app.config["post_manager"] = post_manager
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)

if __name__ == "__main__":
    main()