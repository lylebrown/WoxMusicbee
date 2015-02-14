from musicbeeipc import *
from wox import Wox,WoxAPI


class FileOperations:
    def __init__(self, filepath):
        self.filepath = filepath
        self.mbIPC = MusicBeeIPC()

    def play(self):
        self.mbIPC.play_now(self.filepath)
        WoxAPI.change_query("")
        return []

    def add(self):
        self.mbIPC.queue_next(self.filepath)
        WoxAPI.change_query("")
        return []

    def artist(self):
        return self.mbIPC.library_get_file_tag(self.filepath, 31)

    def title(self):
        return self.mbIPC.library_get_file_tag(self.filepath, 39)

    def artwork(self):
        return self.mbIPC.library_get_artwork_url(self.filepath, 0)

    def jsoncreate(self, function):
        json = {
            "Title": self.artist() + " - " + self.title(),
            "Subtitle": self.filepath,
            "IcoPath": self.artwork(),
            "JsonRPCAction": {
                "method": str(function),
                "parameters": [self.filepath.replace("\\", "\\\\")],
                "dontHideAfterAction": False
                }
            }

        return json


class MusicBee(Wox):
    def __init__(self):
        self.mbIPC = MusicBeeIPC()
        Wox.__init__(self)

    @staticmethod
    def actionparse(action):
        action = action.lower()
        playlist = ["play"]
        addlist = ["add"]
        if action in playlist:
            return "play"
        if action in addlist:
            return "add"
        else:
            return "play"

    @staticmethod
    def tagparse(tag):
        tag = tag.lower()
        titlelist = ["title", "song", "track"]
        artistlist = ["artist", "band", "singer"]
        albumlist = ["album", "cd", "record"]

        if tag in titlelist:
            return ["Title"]
        if tag in artistlist:
            return ["Artist"]
        if tag in albumlist:
            return ["Album"]
        else:
            return ["Title"]

    def argparser(self, key):
        results = []
        arguments = key.split(" ")
        if len(arguments) > 2:
            action = self.actionparse(arguments[0].lower())
            tag = self.tagparse(arguments[1].lower())
            query = " ".join(arguments[2:])

            for result in self.mbIPC.search(query, "Contains", tag):
                fileops = FileOperations(result)
                results.append(fileops.jsoncreate(action))

        return results

    def query(self, key):
        return self.argparser(key)


if __name__ == "__main__":
    MusicBee()