🖥️ Sistemas Distribuidos
Demonstrar o uso de MPI para paralelizar a busca de números primos, distribuindo a tarefa entre duas máquinas (simuladas com duas VMs) interconectadas em rede local, conforme os requisitos. Utilizar um framework distribuído (MPI ou PVM).

Requisitos:
1 computador com Windows 10/11
2 máquinas virtuais Ubuntu (VM1 e VM2)
VirtualBox 
Rede configurada para permitir comunicação entre as VMs
MPI e Python com mpi4py

Clone o repositório nas duas máquinas:
git clone [https://github.com/larif01/mpi-primos.git]

ETAPA 1 – Instalar Ferramentas no Windows
Instalar o VirtualBox
Baixe e instale normalmente.
Baixar Ubuntu ISO (versão 22.04)
Site: (https://ubuntu.com/download/desktop)

ETAPA 2 – Criar e Configurar as Máquinas Virtuais
Crie DUAS VMs no VirtualBox
Para cada VM:
Abra o VirtualBox > clique em "Novo"
Tipo: Linux
Versão: Ubuntu (64-bit)
Memória: pelo menos 2048 MB
Disco: 15 GB
Nomeie como: vm-gerente e vm-executora
Configure a rede das VMs
Ambas devem estar na mesma rede interna:
Com a VM desligada, vá em:
VM → Configurações → Rede
Mude de NAT para "Placa em modo Bridge"
Faça isso para ambas as VMs
Ligue as duas VMs
Verifique e anote os IPs de cada vm com o comando ip a 

ETAPA 3 – Instalar Ubuntu nas duas VMs
Inicie cada VM com a ISO
Instale normalmente o Ubuntu Desktop
Defina senhas fáceis 

ETAPA 4 – Instalar dependências
Em ambas as VMs, execute:
Atualize o sistema:
sudo apt update && sudo apt upgrade -y
Instale Python e MPI:
sudo apt install python3 python3-pip mpich -y
Instale a biblioteca mpi4py:
pip3 install mpi4py
Verifique se o MPI está funcionando:
mpiexec -n 2 hostname

ETAPA 4 – Habilitar comunicação entre as VMs
Na VM gerente, gere chave SSH:
ssh-keygen
# pressione ENTER em todas as perguntas
ssh-copy-id user@ip
Teste com ssh user@ip
# Deve entrar sem pedir senha

ETAPA 5 – Criar o script Python nas duas máquinas
Nome do arquivo: primos_mpi.py
Pode ser criado com o comando nano primos_mpi.py e colando o codigo dentro do arquivo 
Para salvar de ctrl+o Enter e ctrl+x para sair
Teste em cada maquina para ver se funciona, com o comando mpiexec python3 primos_mpi.py

ETAPA 6 – Testar a execu
Execute o comando mpiexec -n 4 python3 primos_mpi.py
#o número quatro é a quantidade de processos desejados
A saída caso estaja tudo certo deve ser como no exemplo a seguir:
lari@lari-VirtualBox:~$ mpiexec -n 4 python3 primos_mpi.py
Total de primos encontrados: 9592
Primeiros 10 primos: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
Últimos 10 primos: [99877, 99881, 99901, 99907, 99923, 99929, 99961, 99971, 99989, 99991]
