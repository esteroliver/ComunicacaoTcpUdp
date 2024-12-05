import os

def main():
     protocolo = int(input("Olá, usuário! Qual protocolo você gostaria de usar para rodar o chat?\n Digite 1 para UDP e 2 para TCP: "))
     quem = int(input("Digite 1 para cliente e 2 para servidor: "))
     if protocolo == 1:
          if quem == 1:
               os.system("python UDP/clienteUDP.py")
          elif quem == 2:
               os.system("python UDP/servidorUDP.py")
     elif protocolo == 2:
          if quem == 1:
               os.system("python TCP/clienteTCP.py")
          elif quem == 2:
               os.system("python TCP/servidorTCP.py")

if __name__ == "__main__":
     main()