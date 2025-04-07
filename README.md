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
Defina senhas fáceis, como larissa/larissa

ETAPA 4 – Instalar dependências
Em ambas as VMs, execute:
sudo apt update && sudo apt install -y python3 python3-pip mpich openssh-server git
pip3 install mpi4py

ETAPA 4 – Habilitar comunicação entre as VMs
Na VM1, gere chave SSH:
ssh-keygen
