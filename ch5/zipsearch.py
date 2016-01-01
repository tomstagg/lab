#!/usr/bin/env python3
import shutil
import zipfile
import sys
from pathlib import Path


class ZipReplace:
    def __init__(self, filename, search_string, replace_string):
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = Path('unzipped-{}'.format(filename))

    def zip_find_replace(self):
        self.unzip_files()
        self.find_replace()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(str(self.temp_directory))

    def find_replace(self):
        for filename in self.temp_directory.iterdir():
            if filename.is_file():
                with filename.open() as file:
                    contents = file.read()
                contents = contents.replace(self.search_string, self.replace_string)
                with filename.open('w') as file:
                    file.write(contents)

    def zip_files(self):
        with zipfile.ZipFile(self.filename, 'w') as file:
            for filename in self.temp_directory.iterdir():
                if filename.is_file():
                    file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))

if __name__ == '__main__':
    ZipReplace(*sys.argv[1:4]).zip_find_replace()


class ZipProcessor:
    def __init__(self, zipname):
        self.zipname = zipname
        self.temp_directory = Path('unzipped-{}'.format(zipname))

    def process_file(self):
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(str(self.temp_directory))

    def zip_files(self):
        with zipfile.ZipFile(self.filename, 'w') as file:
            for filename in self.temp_directory.iterdir():
                if filename.is_file():
                    file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))


class ZipReplace(ZipProcessor):
    def __init__(self, filename, search_string, replace_string):
        super().__init__(filename)
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self):
        for filename in self.temp_directory.iterdir():
            if filename.is_file():
                with filename.open() as file:
                    contents = file.read()
                contents = contents.replace(self.search_string, self.replace_string)
                with filename.open('w') as file:
                    file.write(contents)

class ZipProcessor2:
    def __init__(self, zipname, processor):
        self.zipname = zipname
        self.temp_directory = Path('unzipped-{}'.format(zipname))

    def process_file(self):
        self.unzip_files()
        self.processor.process()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(str(self.temp_directory))

    def zip_files(self):
        with zipfile.ZipFile(self.filename, 'w') as file:
            for filename in self.temp_directory.iterdir():
                if filename.is_file():
                    file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))


class ZipReplace2:
    def __init__(self, search_string, replace_string):
        self.search_string = search_string
        self.replace_string = replace_string

    def process(self):
        for filename in self.temp_directory.iterdir():
            if filename.is_file():
                with filename.open() as file:
                    contents = file.read()
                contents = contents.replace(self.search_string, self.replace_string)
                with filename.open('w') as file:
                    file.write(contents)
