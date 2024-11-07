# Main file that will handle the control of the different services

import time
import asyncio

from pathlib import Path
from fastapi import FastAPI
from rest_handles import app
from rest_api.rest import serve 
from be_flix.service import Service
from be_flix.file_browser import MOVIETYPE, FileManagerDb



def main():
    asyncio.run(serve(app))


    # fp = Path("~/Videos").expanduser().resolve()
    # with Service(FileManagerDb(fp)) as db:
    #     print(db)
                
    


if __name__ == '__main__':
    main()
