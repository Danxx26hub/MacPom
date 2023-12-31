import subprocess
from config import get_settings


class Notify:
    """Creates a notification with the given title and message"""

    def __init__(self, title, message, sound):
        self.title = title
        self.message = message
        self.sound = sound
        self.cmd = f'display notification "{self.message}" with title "{self.title} sound name {self.sound}}"'

    def notify(self):
        subprocess.call(["osascript", "-e", self.cmd])


class timer:
    """Creates a timer that will notify the user after the given minutes, set minutes in config file"""

    def __init__(self, minutes):
        self.minutes = minutes
        self.seconds = minutes * 60

    def start(self):
        title = get_settings("dev").title
        message = get_settings("dev").message
        sound = get_settings("dev").sound
        subprocess.call(["sleep", str(self.seconds)])
        notification = Notify(title, message, sound)
        notification.notify()
    # used for timer testing.
    # def countdown(self):
    #     print(f"Timer set for {self.minutes} minutes")
    #     for i in range(self.seconds, 0, -1):

    #         print(f"{i} seconds remaining")
