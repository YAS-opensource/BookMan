import os
from sys import platform


def __find_possible_paths__(root_path):
    possible_paths = [os.path.join(root_path, x) for x in os.listdir(
        root_path)]
    possible_paths = [x for x in possible_paths if os.path.isdir(x)]
    possible_paths = [
        os.path.join(x, "places.sqlite") for x in possible_paths if "places.sqlite" in os.listdir(x)]
    return possible_paths


def get_path():
    """  returns the location of firefox's local sqlite database """

    if platform == "linux" or platform == "linux2":
        # TODO implement for LINUX platform, just assign the root_path variable
        root_path = ''
        possible_paths = __find_possible_paths__(root_path)
        return possible_paths
    elif platform == "darwin":
        root_path = os.getcwd().split('/')
        root_path = '/'.join(root_path[:3])
        root_path = os.path.join(root_path, "Library",
                                 "Application Support", "Firefox", "Profiles")
        possible_paths = __find_possible_paths__(root_path)
        return possible_paths
    elif platform == "win32":
        # TODO implement for LINUX platform, just assign the root_path variable
        root_path = ''
        possible_paths = __find_possible_paths__(root_path)
        return possible_paths
