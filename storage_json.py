import json

class PostManager:
    """"""

    def __init__(self, file_path):
        """"""
        if file_path.strip() == "":
            raise ValueError("Given file_path must not be empty!")
        if not isinstance(file_path, str):
            raise TypeError(f"Given file_path must be a string! Input was {type(file_path)}.")
        file_format = file_path.split(".")[-1]
        if file_format != "json":
            raise ValueError(f"Invalid file extension. Expected .json file but got {file_format}")
        self.file_path = file_path.strip()


    def load_json(self):
        """"""
        try:
            with open(self.file_path, "r") as handle:
                data = json.load(handle)
        except json.JSONDecodeError as e:
            print(f"Data type was not in JSON format: {e}")
            data = {}
        except FileNotFoundError:
            print(f"File {self.file_path} was not found.")
            data = {}
        return data

    def save_json(self, new_posts):
        """"""
        try:
            with open(self.file_path, "w") as handle:
                json.dump(new_posts, handle, indent=4)
        except IOError as e:
            print(f"Error at opening file: {e}")













# todo add delete update read if post add id +1