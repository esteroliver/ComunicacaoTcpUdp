import socket # biblioteca do python que possibilita criar conexões de baixo nível 
import sys

def conexao():
    # Criando o socket TCP
    Socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # solicitar a porta que o servidor vai ouvir
    Porta = int(input("Qual é a porta que o servidor vai ouvir?"))

    # solicita ip 
    ip_servidor = input("Digite o IP do servidor que deseja se conectar: ") # pergunta e registra ip

    # Bind do ip e da porta para começar a ouvir. Estabelece conexão
    Socket_tcp.bind((ip_servidor, Porta))

    try:  
        Socket_tcp.connect()
        print("Conexão estabelecida com o servidor")

    except socket.error as error:
        print(f"Erro ao tentar se conectar: {error}")

    # Chat
    while True:
        mensagem = input("Digite a sua mensagem para o servidor")

        # envia a mensagem para o servidor
        Socket_tcp.send(mensagem.encode())

        # recebe resposta do servidor
        resposta = Socket_tcp.recv()
        print("Serv: ", resposta.decode())

        