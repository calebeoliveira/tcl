# -*- coding: utf-8 -*-
import random
import pickle
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import mlab

# Demonstração do Teorema Central do Limite
# Para gerar o banco de dados, executar o arquivo populator.py

# Primeiro importa-se os dados gerados pelo populador.
def importData():
    print 'Importando dados...'
    with open('pop.dat', 'rb') as f:
            return pickle.load(f)

# Gera um array de Medias Amostrais com amostras de tamanho igual à meanSize
def sampleMean(sampleSize, meanSize, populacao):
    sampleMean = []

    for i in range(sampleSize):
        temp = 0
        for i in range(meanSize):
            temp += populacao[random.randint(0,1E6 - 1)]

        sampleMean.append(temp/meanSize)

    return sampleMean

if __name__ == '__main__':
    populacao = importData()
    sample = sampleMean(1000, 200, populacao)

    mean = np.mean(sample)
    std  = np.std(sample)
    n, bins, patches = plt.hist(sample, color="pink")
    y = mlab.normpdf(bins, mean, std)

    print mean, std

    plt.plot(bins, y, 'r--')
    plt.xlabel("Media Amostral")
    plt.ylabel("Frequencia")
    plt.subplots_adjust(left=0.15)
    plt.show()
