# -*- coding: utf-8 -*-
import random
import pickle

# Gerador de salários da população basileira.
# Proporções fictícias:
#
# 60% - 1 salário
# 20% - entre 1 e 2 salários
# 15% - entre 2 e 5 salários
# 5% - mais de 5 salários

salario = 788
tamanhoPopulacao = 1E6
populacao = []

def populaFaixa(tamanho, min, max):
	for i in range(int(tamanho)):
		populacao.append(random.randint(min, max))

populaFaixa(tamanhoPopulacao*0.6, salario, salario)
populaFaixa(tamanhoPopulacao*0.2, salario+1, salario*2)
populaFaixa(tamanhoPopulacao*0.15, salario*2+1, salario*5)
populaFaixa(tamanhoPopulacao*0.05, salario*5+1, salario*10)

random.shuffle(populacao)

with open('pop.dat', 'wb') as f:
	pickle.dump(populacao, f)
