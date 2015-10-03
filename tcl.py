# -*- coding: utf-8 -*-
import pickle
import numpy as np
from matplotlib import pyplot as plt

# Demonstração do Teorema Central do Limite
# Para gerar o banco de dados, executar o arquivo populator.py

# Primeiro importa-se os dados gerados pelo populador.
print 'Importando dados...'
with open('pop.dat', 'rb') as f:
	populacao = pickle.load(f)

