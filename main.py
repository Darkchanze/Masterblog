from app import app
from storage_json import PostManager


FILE_PATH = "posts.json"


def main():
    post_manager = PostManager(FILE_PATH)
    app.config["post_manager"] = post_manager
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)

if __name__ == "__main__":
    main()