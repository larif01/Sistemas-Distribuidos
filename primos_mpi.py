from mpi4py import MPI
import math

def is_prime(n):
    """Verifica se um número é primo."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    """Encontra números primos em um intervalo."""
    primes = [n for n in range(start, end) if is_prime(n)]
    return primes

# Configuração MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()  # ID do processo
size = comm.Get_size()  # Número total de processos

# Apenas o processo 0 gerencia a distribuição
if rank == 0:
    total_primes = []
    found_primes = 0
    next_start = 2
    batch_size = 100  # Define o tamanho do intervalo distribuído a cada worker

    while found_primes < 100:
        # Distribuir trabalho para os workers
        for worker in range(1, size):
            if found_primes >= 100:
                break
            comm.send((next_start, next_start + batch_size), dest=worker)
            next_start += batch_size

        # Receber resultados dos workers
        for worker in range(1, size):
            if found_primes >= 100:
                break
            primes = comm.recv(source=worker)
            total_primes.extend(primes)
            found_primes = len(total_primes)
            total_primes.sort()

    # Exibir os 100 primeiros primos encontrados
    print("100 primeiros números primos encontrados:")
    print(total_primes[:100])

    # Enviar sinal de término para os workers
    for worker in range(1, size):
        comm.send(None, dest=worker)

else:
    while True:
        task = comm.recv(source=0)
        if task is None:
            break  # Sinal de término recebido

        start, end = task
        primes = find_primes(start, end)
        comm.send(primes, dest=0)


