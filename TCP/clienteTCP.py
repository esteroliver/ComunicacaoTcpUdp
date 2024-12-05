import socket
import threading

def receber_mensagens(Socket_tcp):
    while True:
        try:
            mensagem = Socket_tcp.recv(1024)
            print("\nOutro cliente: ", mensagem.decode("utf-8"))
        except:
            print("Conexão com o servidor perdida.")
            Socket_tcp.close()
            break

def conexao():
    Socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Porta = int(input("Qual é a porta que o servidor vai ouvir? "))
    ip_servidor = input("Digite o IP do servidor que deseja se conectar: ")

    try:
        Socket_tcp.connect((ip_servidor, Porta))
        print("Conexão estabelecida com o servidor")
    except socket.error as error:
        print(f"Erro ao tentar se conectar: {error}")
        return

    # Cria uma thread para receber mensagens
    threading.Thread(target=receber_mensagens, args=(Socket_tcp,)).start()

    # Chat
    while True:
        mensagem = input("Você: ")
        if mensagem.lower() == "sair":
            print("Encerrando conexão...")
            Socket_tcp.close()
            break
        Socket_tcp.send(mensagem.encode())

if __name__ == "__main__":
    conexao()
