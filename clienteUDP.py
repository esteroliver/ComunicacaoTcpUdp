import socket
from datetime import datetime 

def enviar_mensagem(sock, nome, ip, porta):
    mensagem = input(f"Digite sua mensagem: ")
    mensagem = f"[{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}] {nome}: {mensagem}"
    sock.sendto(mensagem.encode(encoding="utf-8"), (ip, porta))

def main():
    nome = input("Olá, diga-nos seu nome: ")
    ip = input("Digite o IP do servidor que deseja se conectar: ")
    porta = int(input("Digite a porta do servidor que deseja se conectar: "))

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # cria socket

    print(f"{nome} se conectou!") 

    while True: 
        try: 
            # sock.settimeout(3) # tempo para esperar por mensagens. se não mandar mais mensagens, o código vai executar outras partes
            # data, endereco = sock.recvfrom(1024) # espera receber mensagem
            # print(data.decode()) # mensagem decodificada e exibida na tela
            
            enviar_mensagem(sock, nome, ip, porta)

            data, endereco = sock.recvfrom(1024)
            print(f"Resposta do servidor: {data.decode()}")
        except socket.timeout:
            print("Tempo de espera excedido, tentando novamente.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            break

if __name__ == "__main__":
    main()