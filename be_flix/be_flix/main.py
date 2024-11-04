# Main file that will handle the control of the different services

import time
from multiprocess import Process, Queue
from be_flix.rest import rest_server
from be_flix.file_browser import MOVIETYPE, FileManagerDb

def main():
    


    rest = Process(target=rest_server)
    rest.start()

    
    # time.sleep(5)
    # rest.terminate()


if __name__ == '__main__':
    main()
