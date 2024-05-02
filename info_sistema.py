
import platform

# Obter informações gerais do sistema
print("-" * 40)
print("Informações do Sistema")
print("-" * 40)
print(f"Sistema: {platform.system()}")
print(f"Lançamento: {platform.release()}")
print(f"Versão: {platform.version()}")
print(f"Máquina: {platform.machine()}")
print(f"Processador: {platform.processor()}")

# Obter informações de hardware
print("-" * 40)
print("Informações de Hardware")
print("-" * 40)
import cpuinfo
print(f"Informações da CPU: {cpuinfo.get_cpu_info()['brand_raw']}")
import psutil
print(f"RAM: {psutil.virtual_memory().total / (1024 * 1024):.2f} MB")
print(f"Uso do Disco: {psutil.disk_usage('/').percent:.2f}%")

# Obter informações de rede
print("-" * 40)
print("Informações de Rede")
print("-" * 40)
import socket
print(f"Nome da Máquina: {socket.gethostname()}")
print(f"Endereço de IP: {socket.gethostbyname(socket.gethostname())}")