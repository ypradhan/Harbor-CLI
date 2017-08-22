import sys

from lib.constants.build_platforms import BuildPlatforms
from lib.services.build_strategies import build_strategies
from lib.exceptions.DirNotFound import DirNotFoundException
from lib.exceptions.FileNotFound import FileNotFoundException

def builder(build_platform=BuildPlatforms.REACT_NATIVE):
    class Builder():

        def __init__(self):
            self.build_platform = build_platform

        def build(self):
            try:
               return build_strategies()[self.build_platform]()
            except DirNotFoundException as e:
                print(e.message)
                sys.exit(1)
            except FileNotFoundException as e:
                print(e.message)
                sys.exit(0)

    return Builder
