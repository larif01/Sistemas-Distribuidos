# Sistemas-Distribuídos
Demonstrar o uso de MPI para paralelizar a busca de números primos, distribuindo a tarefa entre duas máquinas (simuladas com duas VMs) interconectadas em rede local, conforme os requisitos. Utilizar um framework distribuído (MPI ou PVM)

Requisitos:
1 computador com Windows 10/11
2 máquinas virtuais Ubuntu (VM1 e VM2)
VirtualBox 
Rede configurada para permitir comunicação entre as VMs
MPI e Python com mpi4py

ETAPA 1 – Instalar Ferramentas no Windows
Instalar o VirtualBox
Baixe e instale normalmente.
Baixar Ubuntu ISO (versão 22.04)
Site: [https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop)

ETAPA 2 – Criar e Configurar as Máquinas Virtuais
Crie DUAS VMs no VirtualBox
Para cada VM:
Tipo: Linux
Versão: Ubuntu (64-bit)
Memória: pelo menos 2048 MB
Disco: 15 GB
Nomeie como: vm-gerente e vm-executora
Configure a rede das VMs
Ambas devem estar na mesma rede interna:
Vá em Configurações da VM → Rede
Em "Adaptador 1", marque:
Ativar Placa de Rede
Modo de Conexão: Rede Interna
Nome: rede-mpi
Assim elas estarão em uma rede local 192.168.X.X simulada.

ETAPA 3 – Instalar Ubuntu nas duas VMs
Inicie cada VM com a ISO
Instale normalmente o Ubuntu Desktop
Defina senhas fáceis, como larissa/larissa
