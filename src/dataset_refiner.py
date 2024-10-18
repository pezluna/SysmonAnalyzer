import sys
import os

raw_path = "../dataset/raw_dataset/"
refined_path = "../dataset/refined_dataset/"

class lmd_refiner:
    def __init__(self):
        self.raw_path = raw_path + "lmd/"
        self.refined_path = refined_path + "lmd/"
    
    def refine(self):
        pass

class aau_refiner:
    def __init__(self):
        import json

        self.raw_path = raw_path + "aau/"
        self.refined_path = refined_path + "aau/"

        with open(self.raw_path + "aau.json", "r") as f:
            self.data = json.load(f)

    def refine(self):
        pass