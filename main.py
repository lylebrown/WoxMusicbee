from musicbeeipc import *
from wox import Wox,WoxAPI

mbIPC = MusicBeeIPC()

'''
class MusicBeeMain():

    def search(self, searchtype, arg):
        searchtypetech = ""
        if searchtype.lower() in ["title", "song", "track"]:
            searchtypetech = "Title"
        elif searchtype.lower() in ["artist", "band", "singer"]:
            searchtypetech = "Artist"
        elif searchtype.lower() in ["album", "cd"]:
            searchtypetech = "Album"
        else:
            searchtypetech = "Title"

        resultlist = []
        for result in mbIPC.search(str(arg), "Contains", [searchtypetech]):
            resultlist.append(result)
        return resultlist

    def play(self, filepath):
        return mbIPC.play_now(filepath)

    def add(self, filepath):
        return mbIPC.queue_next(filepath)

    def query(self, query):
        command = query.split(" ")[0].lower()  # "play" or "add"
        argtype = query.split(" ")[1].lower()  # "track", "artist", "album", etc.
        argument = []
        for word in query.split(" ")[2:]:
            argument.append(word.lower())

        if command == "play":
            return self.play(self.search(argtype, argument))
        elif command == "add":
            return self.add(self.search(argtype, argument))

        # debug
        # print("Command: " + command + "\nArgumentType: " + argtype + "\nArgument:  " + argument + "\n")
'''

# mb.query("play artist alice")
# print mb.search("title","fake it")[0]
# for result in mbIPC.search("come", "Contains", ["Title"]):
#    print result


class MusicBee(Wox):
    def query(self, key):
        results = []
        arguments = key.split(" ")
        if len(arguments) > 2:
            if arguments[0].lower() == "play":
                if arguments[1].lower() in ["title", "song", "track"]:
                    for result in mbIPC.search(" ".join(arguments[2:]), "Contains", ["Title"]):
                        results.append({"Title": mbIPC.library_get_file_tag(result, 31) + " - " +
                                                 mbIPC.library_get_file_tag(result, 39),
                                        "Subtitle": result,
                                        "IcoPath": mbIPC.library_get_artwork_url(result, 0),
                                        "JsonRPCAction": {
                                            "method": "play",
                                            "parameters": [result.replace("\\", "\\\\")],
                                            "dontHideAfterAction": False
                                            }
                                        })
                elif arguments[1].lower() in ["artist", "band", "singer"]:
                    for result in mbIPC.search(" ".join(arguments[2:]), "Contains", ["Artist"]):
                        results.append({"Title": mbIPC.library_get_file_tag(result, 31) + " - " +
                                                 mbIPC.library_get_file_tag(result, 39),
                                        "Subtitle": result,
                                        "IcoPath": mbIPC.library_get_artwork_url(result, 0),
                                        "JsonRPCAction": {
                                            "method": "play",
                                            "parameters": [result.replace("\\", "\\\\")],
                                            "dontHideAfterAction": False
                                            }
                                        })
                elif arguments[1].lower() in ["album", "record", "cd"]:
                    for result in mbIPC.search(" ".join(arguments[2:]), "Contains", ["Album"]):
                        results.append({"Title": mbIPC.library_get_file_tag(result, 31) + " - " +
                                                 mbIPC.library_get_file_tag(result, 39),
                                        "Subtitle": result,
                                        "IcoPath": mbIPC.library_get_artwork_url(result, 0),
                                        "JsonRPCAction": {
                                            "method": "play",
                                            "parameters": [result.replace("\\", "\\\\")],
                                            "dontHideAfterAction": False
                                            }
                                        })
            elif arguments[0].lower() == "add":
                if arguments[1].lower() in ["title", "song", "track"]:
                    for result in mbIPC.search(" ".join(arguments[2:]), "Contains", ["Title"]):
                        results.append({"Title": mbIPC.library_get_file_tag(result, 31) + " - " +
                                                 mbIPC.library_get_file_tag(result, 39),
                                        "Subtitle": result,
                                        "IcoPath": mbIPC.library_get_artwork_url(result, 0),
                                        "JsonRPCAction": {
                                            "method": "add",
                                            "parameters": [result.replace("\\", "\\\\")],
                                            "dontHideAfterAction": False
                                        }
                        })
                elif arguments[1].lower() in ["artist", "band", "singer"]:
                    for result in mbIPC.search(" ".join(arguments[2:]), "Contains", ["Artist"]):
                        results.append({"Title": mbIPC.library_get_file_tag(result, 31) + " - " +
                                                 mbIPC.library_get_file_tag(result, 39),
                                        "Subtitle": result,
                                        "IcoPath": mbIPC.library_get_artwork_url(result, 0),
                                        "JsonRPCAction": {
                                            "method": "add",
                                            "parameters": [result.replace("\\", "\\\\")],
                                            "dontHideAfterAction": False
                                        }
                        })
                elif arguments[1].lower() in ["album", "record", "cd"]:
                    for result in mbIPC.search(" ".join(arguments[2:]), "Contains", ["Album"]):
                        results.append({"Title": mbIPC.library_get_file_tag(result, 31) + " - " +
                                                 mbIPC.library_get_file_tag(result, 39),
                                        "Subtitle": result,
                                        "IcoPath": mbIPC.library_get_artwork_url(result, 0),
                                        "JsonRPCAction": {
                                            "method": "add",
                                            "parameters": [result.replace("\\", "\\\\")],
                                            "dontHideAfterAction": False
                                        }
                        })
        return results

    def play(self, result):
        mbIPC.play_now(result)
        WoxAPI.change_query("")
        return []

    def add(self, result):
        mbIPC.queue_next(result)
        WoxAPI.change_query("")
        return []

if __name__ == "__main__":
    MusicBee()
