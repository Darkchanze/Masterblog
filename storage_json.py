import json

class PostManager:
    """
    Manages loading and saving posts in a JSON file.
    """

    def __init__(self, file_path: str):
        """
        Initializes the PostManager with the given file path.

        :param file_path: The path to the JSON files, containing the posts.
        :raises ValueError: If the file path is empty or does not point to a JSON file.
        :raises TypeError: If the file path is not a string.
        """
        if file_path.strip() == "":
            raise ValueError("Given file_path must not be empty!")
        if not isinstance(file_path, str):
            raise TypeError(f"Given file_path must be a string! Input was {type(file_path)}.")
        file_format = file_path.split(".")[-1]
        if file_format != "json":
            raise ValueError(f"Invalid file extension. Expected .json file but got {file_format}")
        self.file_path = file_path.strip()


    def load_json(self):
        """
        Loads the content of the JSON file and returns the data as a list of dictionarys.

        :return: The loaded data from the JSON file as a list of dictionarys.
        :raises json.JSONDecodeError: If the file was not in JSON format.
        :raises FileNotFoundError: If the file was not found.
        """
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


    def save_json(self, new_posts: list):
        """
        Saves the new posts to the JSON file.

        :param new_posts (list): A list of dictionarys containing the new posts to be saved.
        :raises IOError: If there is an error opening or writing to the file.
        """
        try:
            with open(self.file_path, "w") as handle:
                json.dump(new_posts, handle, indent=4)
        except IOError as e:
            print(f"Error at opening file: {e}")