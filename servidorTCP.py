import socket 

def servidor():
    # Cria o socket tcp
    Socket_tcp_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Solicitar a porta que o servidor vai ouvir
    Porta = int(input("Qual é a porta que o servidor vai ouvir?"))

    # Solicitar o IP do servidor
    ip_servidor = input("Digite o IP do servidor que deseja se conectar: ")

    # Bind do IP e da porta para começar a ouvir. Estabelece conexão
    Socket_tcp_serv.bind((ip_servidor, Porta))

    # Começar a escutar
    Socket_tcp_serv.listen(1)

    # Aceitar a conexão do cliente
    conexao, endereco = Socket_tcp_serv.accept()  # Agora a aceitação da conexão está dentro da função

    # Chat
    while True: 
        # Receber a mensagem do cliente
        mensagem = conexao.recv(1024)
        if not mensagem:
            break  # Se não houver mensagem, sai do loop
        print("Cliente enviou: ", mensagem.decode("utf-8"))