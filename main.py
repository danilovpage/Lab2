import re
from tqdm import tqdm
import time
import argparse
import json



parser = argparse.ArgumentParser()
parser.add_argument("input", help='Get path file input')
parser.add_argument("output", help='Get path file output')
args = parser.parse_args()

