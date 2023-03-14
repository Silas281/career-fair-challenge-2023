import sys
import os


class ReadCMD:
    def __init__(self):
        self.filename = None

    def read_cmd(self):
        if len(sys.argv) == 2:
            self.filename = sys.argv[1]
            if os.path.isfile(self.filename):
                return self.filename
            else:
                sys.exit("File not found")
        else:
            sys.exit("File not found")
