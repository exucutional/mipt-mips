import argparse
import json
from tgraph import Topology

class App():
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Visualize MIPT-V topology')
        parser.add_argument(
            'filepath', 
            help='path to JSON file', 
            metavar="'File_path'")
        args = parser.parse_args()
        self.filepath = args.filepath
        self.config = {}

    def run(self):
        try:
            with open(self.filepath, 'r') as f:
                self.config = json.load(f)

            topology = Topology(self.config)
            topology.view()
        except Exception as e:
            print(e)
