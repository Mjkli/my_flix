# Main file that will handle the control of the different services

import time
from multiprocess import Process
from be_flix.rest import rest_server


def main():
    rest = Process(target=rest_server)

    rest.start()

    # time.sleep(5)
    # rest.terminate()


if __name__ == '__main__':
    main()
