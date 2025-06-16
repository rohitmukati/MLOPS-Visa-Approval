import os

def from_root():
    return os.path.dirname(os.path.abspath(__file__)).rsplit("us_visa", 1)[0]
