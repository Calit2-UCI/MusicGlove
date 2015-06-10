__author__ = 'Nathan'
from threading import Thread
from RIVA_Main import MusicGloveSong, reset_RIVA_log


def songLoop():
    reset_RIVA_log()
    MusicGloveSong(user="Nathan").test_for_restart()

thread = Thread(target=songLoop)
thread.daemon = True  # die when the main thread dies
thread.start()

while 1:
    UserInput = raw_input("please enter something")
    print UserInput