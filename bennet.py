#!/usr/bin/env python3
from common.common import ic
from hodges.file_system.file_system_class import FileSystemManager
from anvil.anvil import Anvil
from common.config import version, debug
from rich import print

class Bennet:
    def __init__(self):
        print(f"BENNET version: {version}")
        self.fs = FileSystemManager()
        self.project = Anvil(filesystem=self.fs, root="project")
        
        ic(self.fs.root_) if debug else None
        
        if debug:
            self.root_dir = "./bennet_develop_space"
            if self.fs.file_exists(self.root_dir):
                self.fs.rmdir(self.root_dir)
            
            if(self.fs.mkdir(self.root_dir)):
                self.fs.cd(self.root_dir)

        else:
            ic("no debug")


    def init(self):
        self.project.init()

    def interactive_init(self):
        self.project.interactive_init()

    def change_root(self):
        self.project.change_root()

    def help(self):
        ic("Help function called") if debug else None

