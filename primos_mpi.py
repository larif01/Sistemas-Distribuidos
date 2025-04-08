#!/usr/bin/env python3
from mpi4py import MPI

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
MAX_NUM = 100000
inicio = (rank * MAX_NUM) // size
fim = ((rank + 1) * MAX_NUM) // size

# Encontrar primos no intervalo atribuído a este processo
primos_locais = [n for n in range(inicio, fim) if eh_primo(n)]

# Coletar todos os primos encontrados
primos_totais = comm.gather(primos_locais, root=0)

if rank == 0:
    # Unir todas as listas de primos e ordenar
    todos_primos = sorted([primo for sublist in primos_totais for primo in sublist])
    print(f"Total de primos encontrados: {len(todos_primos)}")
    print(f"Primeiros 10 primos: {todos_primos[:10]}")
    print(f"Últimos 10 primos: {todos_primos[-10:]}")
