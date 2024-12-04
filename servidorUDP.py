import socket # biblioteca do python que possibilita criar conexões de baixo nível
from datetime import datetime # para a funcionalidade de datetime.now()


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    porta = int(input("Dgite a porta em que deseja ouvir: "))
    sock.bind(('', porta))
    print(f"Ouvindo na porta {porta}")
    while True:
        dados, endereco = sock.recvfrom(65535)
        mensagem = f"Recebido de {str(endereco)}: {dados.decode()}"
        sock.sendto(mensagem, (endereco, porta))

if __name__ == "__main__":
    main()