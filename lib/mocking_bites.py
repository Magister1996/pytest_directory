import requests
import time

class MusicLibrary:
    def __init__(self):
        self.track_list = []

    def add(self, track):
        self.track_list.append(track)

    def search(self, keyword):
        answer_list = [track for track in self.track_list if track.matches(keyword) == True]
        print(answer_list)
        return answer_list

class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def matches(self, keyword):
        if keyword.lower() in self.title.lower() or keyword.lower() in self.artist.lower():
            return True
        else:
            return False

class Task:
    def __init__(self, title):
        self.title = title
        self.complete = False

    def mark_complete(self):
        self.complete = True

    def is_complete(self):
        return self.complete

class TaskList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def all(self):
        return self.tasks

    def all_complete(self):
        if len(self.tasks) == 0:
            return False
        return all([task.is_complete() for task in self.tasks])
    
class TaskFormatter:
    def __init__(self, task): # task is an instance of Task
        self.formatter_title = task.title
        self.formatter_complete = task.complete

    def format(self):
        if self.formatter_complete == False:
            return (f"[ ] {self.formatter_title}")
        else:
            return (f"[X] {self.formatter_title}")

class SecretDiary:
    def __init__(self, diary):
        self.secret_diary = diary
        self.secret_status = False

    def read(self):
        if self.secret_status == True:
            raise Exception("Go away!")
        else:
            return self.secret_diary.read()

    def lock(self):
        self.secret_status = True

    def unlock(self):
        self.secret_status = False

class Diary:
    def __init__(self, contents):
        self.contents = contents

    def read(self):
        return self.contents
    
class ActivitySuggester:
    def __init__(self, requester):  # requester is usually `requests`
        self.requester = requester

    def suggest(self):
        response = self._make_request_to_api()
        return f"Why not: {response['activity']}"

    def _make_request_to_api(self):
        # We use 'self.requester' rather than 'requests'
        response = self.requester.get("http://www.boredapi.com/api/activity")
        return response.json()

class TimeError:
    def __init__(self, requester):
        self.requester = requester
    # Returns difference in seconds between the time on an external server
    # and the time on this computer
    def error(self, time):
        return self._get_server_time() - time.time()

    # The underscore denotes this is a private method not to be called from the
    # outside. You also shouldn't stub it in your tests. So if your tests contain
    # the words `get_server_time`, you're on the wrong track.
    def _get_server_time(self):
        response = self.requester.get("https://worldtimeapi.org/api/ip")
        json = response.json()
        return json["unixtime"]

class CatFacts:
    def __init__(self, requester):
        self.requester = requester

    def provide(self):
        return f"Cat fact: {self._get_cat_fact()['fact']}"

    # Again, don't stub this method.
    def _get_cat_fact(self):
        response = self.requester.get("https://catfact.ninja/fact")
        return response.json()