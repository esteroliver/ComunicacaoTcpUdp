import socket # biblioteca do python que possibilita criar conexões de baixo nível
from datetime import datetime # para a funcionalidade de datetime.now()

def enviar_mensagem(sock, nome, ip_servidor, porta):
    mensagem = input(f"Digite sua mensagem: ")
    mensagem = f"[{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}] {nome}: {mensagem}" # adiciona hora e
    sock.sendto(mensagem.encode(encoding="utf-8"), (ip_servidor, porta))

def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # cria socket

    nome = input("Olá, diga-nos seu nome: ") # pergunta e registra nome

    ip_servidor = input("Digite o IP do servidor que deseja se conectar: ") # pergunta e registra ip

    porta = int(input("Digite a porta do servidor que deseja se conectar: ")) # pergunta e registra a porta

    sock.bind((ip_servidor, porta)) # liga o socket a endereço e porta. a partir daqui ele sempre estará ouvindo pela porta configurada

    print(f"{nome} se conectou!") # printa que o nome da pessoa que se conectou

    while True: # looping de envio e recebimento de mensagens

        try: # tente
            sock.settimeout(10) # tempo para esperar por mensagens. se não mandar mais mensagens, o código vai executar outras partes
            data, endereco = sock.recvfrom(65535) # espera receber mensagem
            print(data.decode()) # mensagem decodificada e exibida na tela
            enviar_mensagem(sock, nome, ip_servidor, porta)
        except socket.timeout: # exceção
            enviar_mensagem(sock, nome, ip_servidor, porta)

if __name__ == "__main__":
    main()