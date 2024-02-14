
# author    : Julio C. Pereira
# sistema   : Linux
# incio     : 20240214

# -vou dispar icmp para equipamento e identificar se está vivo ou morto-

# importar subprocess para conseguir realizar comandos do sistema 
import subprocess

# - criar uma lista com vários targets -
hosts = ['8.8.8.8', 'japan.jp', 'fance.fr', 'usa.com']

# - função que pinga equipamento e retorna 0 ou 1 -
def live(ip):
    return subprocess.run(['ping', '-c', '1', '-i', '0.2', '-w', '1', ip], capture_output=True, text=True)

# - for para testar todos os ips da lista hosts -
for host in hosts:
    # chamar função live e receber o resultado do teste 0 ou 1
    ping = live(host)

    # se ping = 0 porque pingou se diferente então dispositivo inacessivel
    if ping.returncode == 0:
        print(f'{host} \t OK \t|seq= {count}')
    else:
        print(f'{host} \t -- \t|seq= {count}')
    
