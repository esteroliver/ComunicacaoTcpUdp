import socket
from datetime import datetime

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = ''
    porta = int(input("Digite a porta em que deseja ouvir: "))
    sock.bind((ip, porta))

    clientes = {}

    print(f"Ouvindo na porta {porta}")

    while True:
        try:
            dados, endereco = sock.recvfrom(1024)
            mensagem = f"Recebido de {str(endereco)}: {dados.decode()}\n"
            print(mensagem)

            clientes[endereco] = mensagem

            for cliente, msg in clientes.items():
                if cliente != endereco:
                    sock.sendto(f"{endereco}: {mensagem}".encode(), cliente)

        except Exception as e:
            print(f"Erro: {e}")
            break
            
    sock.close()

if __name__ == "__main__":
    main()