from musicbeeipc import *
from wox import Wox, WoxAPI


class MusicBee(Wox):
    def __init__(self):
        self.mbIPC = MusicBeeIPC()
        Wox.__init__(self)

    def play(self, file_path):
        self.mbIPC.play_now(file_path)
        WoxAPI.change_query("")
        return []

    def add(self, file_path):
        self.mbIPC.queue_next(file_path)
        WoxAPI.change_query("")
        return []

    def artist(self, file_path):
        return self.mbIPC.library_get_file_tag(file_path, 31)

    def title(self, file_path):
        return self.mbIPC.library_get_file_tag(file_path, 39)

    def artwork(self, file_path):
        local_art = self.mbIPC.library_get_artwork_url(file_path, 0)
        mb_icon = "Images\\pic.png"
        if ".tmp" not in local_art:
            return self.mbIPC.library_get_artwork_url(file_path, 0)
        else:
            return mb_icon

    def json_create(self, function, file_path):
        json = {
            "Title": self.artist(file_path) + " - " + self.title(file_path),
            "Subtitle": file_path,
            "IcoPath": self.artwork(file_path),
            "JsonRPCAction": {
                "method": function,
                "parameters": [file_path.replace("\\", "\\\\")],
                "dontHideAfterAction": False
            }
        }

        return json

    @staticmethod
    def action_parse(action):
        action = action.lower()
        play_list = ["play"]
        add_list = ["add"]
        if action in play_list:
            return "play"
        if action in add_list:
            return "add"
        else:
            return "play"

    @staticmethod
    def tag_parse(tag):
        tag = tag.lower()
        title_list = ["title", "song", "track"]
        artist_list = ["artist", "band", "singer"]
        album_list = ["album", "cd", "record"]

        if tag in title_list:
            return ["Title"]
        if tag in artist_list:
            return ["Artist"]
        if tag in album_list:
            return ["Album"]
        else:
            return ["Title"]

    def arg_parser(self, key):
        results = []
        arguments = key.split(" ")
        if len(arguments) > 2:
            action = self.action_parse(arguments[0].lower())
            tag = self.tag_parse(arguments[1].lower())
            query = " ".join(arguments[2:])

            for result in self.mbIPC.search(query, "Contains", tag):
                results.append(self.json_create(action, result))

        return results

    def query(self, key):
        return self.arg_parser(key)


if __name__ == "__main__":
    MusicBee()