# Copyright 2020-2021 the openage authors. See copying.md for legal info.

"""
Associate files or filepaths with hash values to determine the exact version of a game.
"""


class GameFileVersion:
    """
    Associates a file hash with a specific version number.
    This can be used to pinpoint the exact version of a game.
    """
    hash_algo = "SHA3-256"

    def __init__(self, filepaths, hashes):
        """
        Create a new file hash to version association.

        :param filepaths: Paths to the specified file. Only one of the paths
                          needs to exist. The other paths are interpreted as
                          alternatives, e.g. if the game is released on different
                          platforms with different names for the same file.
        :type filepaths: list
        :param hashes: Maps hashes to a version number string.
        :type hashes: dict
        """
        self.paths = filepaths
        if len(self.paths) < 1:
            raise Exception(f"{self}: List of paths cannot be empty.")

        self.hashes = hashes

    def get_paths(self):
        """
        Return all known paths to the file.
        """
        return self.paths

    def get_hashes(self):
        """
        Return the hash-version association for the file paths.
        """
        return self.hashes
