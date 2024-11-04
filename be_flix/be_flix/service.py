from typer import Any
import multiprocess import Process, Queue



class Service():
    def __init__(self, state: Any):
        self.state = state
        self.mailbox = Queue()
        
