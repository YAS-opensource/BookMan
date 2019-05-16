import os
from sys import platform


path = ''


def get_path():
    """  returns the location of firefox's local sqlite database """

    if platform == "linux" or platform == "linux2":
        # TODO implement for LINUX platform
        return path
        pass
    elif platform == "darwin":
        root_path = os.getcwd().split('/')
        root_path = '/'.join(root_path[:3])
        root_path = os.path.join(root_path, "Library",
                                 "Application Support", "Firefox", "Profiles")
        possible_paths = [os.path.join(root_path, x) for x in os.listdir(
            root_path)]
        possible_paths = [x for x in possible_paths if os.path.isdir(x)]
        possible_paths = [
            os.path.join(x, "places.sqlite") for x in possible_paths if "places.sqlite" in os.listdir(x)]
        print(possible_paths)
        return path
    elif platform == "win32":
        # TODO implement for Windows platform
        return path
