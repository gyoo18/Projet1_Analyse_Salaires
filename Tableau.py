import math
import pandas as pd
from pandas import DataFrame


class Tableau:
    def __init__(self, nom: str, data_frame : DataFrame):
        self.nom = nom
        self.df = data_frame
