
# Given a directory look at all the files inside and and 
# create MovieObjects to store in the FileManagerDB


import typer
import uuid
from pathlib import Path



app = typer.Typer()

MOVIETYPE = set([".mp4", ".avi"])

class MovieObject():
    def __init__(self, name: str, path: Path):
        self.name = name
        self.path = path
        self.annotation = ""
        self.image = ""

class FileManagerDb():
    def __init__(self, _path: Path):
        self.obj_db = {}
        if _path is not None:
            load_dir(_path)

    def add(self, obj: MovieObject):
        _id = uuid.uuid4()
        self.obj_db.update({str(_id): obj})


    def get(self, id: str) -> MovieObject:
        return self.obj_db[id]


    def load_dir(self, path: Path):
        for file in path.iterdir():
            if file.is_file() and file.suffix in MOVIETYPE:
                movie_obj = MovieObject(name=file.stem, path=file)
                self.add(movie_obj)


@app.command()
def setup(input: Path):
    db = FileManagerDb()
    db.load_dir(input)
    print(db.obj_db)

if __name__ == "__main__":
    app()

