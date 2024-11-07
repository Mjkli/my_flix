from typing import Any
from multiprocess import Process, Queue


# Need to think how to keep alive
class Service():
    def __init__(self, state: Any):
        self.state = state
        self.mailbox = Queue()

    def __enter__(self):
        print("New Service")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting ctx")

    

