#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split



# TODO: Définissez vos fonctions ici

def lecture_csv(fichier_csv):

    df = pd.read_csv(fichier_csv, sep=";", header=0)
    y = df["quality"]
    x = df.drop(columns=["quality"])



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    liste = lecture_csv("./data/winequality-white.csv")
    print(liste)


