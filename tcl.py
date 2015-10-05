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
    with open('pop.dat', 'rb') as f:
            return pickle.load(f)

# Gera um array de Medias Amostrais com amostras de tamanho igual à meanSize
def sampleMean(sampleSize, meanSize, populacao):
    sampleMean = []
    popSize = len(populacao)

    for i in range(sampleSize):
        temp = 0
        for i in range(meanSize): # Somatório de elementos das amostras
            temp += populacao[random.randint(0, popSize - 1)]

        sampleMean.append(temp/meanSize) # Média das amostras

    return sampleMean # Médias de todas as amostras

if __name__ == '__main__':
    print 'Importando dados...'
    populacao = importData()
    print 'Calculando médias...'
    sample = sampleMean(1000, 200, populacao) # 1000 amostras com 200 elementos

    mean = np.mean(sample) # Média de todas as amostras
    std  = np.std(sample) # Desvio padrão
    n, bins, patches = plt.hist(sample, color="pink") # Histograma das amostras
    y = mlab.normpdf(bins, mean, std) # Função densidade de probabilidade

    print 'Média: '+str(mean), 'Desvio padrão: '+str(std)

    plt.plot(bins, y, 'r--')
    plt.xlabel("Media Amostral")
    plt.ylabel("Frequencia")
    plt.subplots_adjust(left=0.15)
    plt.show()
