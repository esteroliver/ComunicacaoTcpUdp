import socket
import threading

# Lista para armazenar as conexões dos clientes
clientes = []

def gerenciar_cliente(conexao, endereco):
    print(f"Cliente conectado: {endereco}")
    while True:
        try:
            mensagem = conexao.recv(1024)
            if not mensagem:
                break
            # Repassar a mensagem para os outros clientes
            print(f"Mensagem recebida de {endereco}: {mensagem.decode('utf-8')}")
            for cliente in clientes:
                if cliente != conexao:  # Não envia a mensagem de volta ao remetente
                    cliente.send(mensagem)
        except:
            break
    # Remove o cliente desconectado da lista
    print(f"Cliente desconectado: {endereco}")
    clientes.remove(conexao)
    conexao.close()

def servidor():
    # Cria o socket TCP
    Socket_tcp_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Porta = int(input("Qual é a porta que o servidor vai ouvir? "))
    
    # Estabelece a conexão
    Socket_tcp_serv.bind(('', Porta))
    Socket_tcp_serv.listen(5)
    print("Servidor escutando...")

    while True:
        # Aceitar conexões de clientes
        conexao, endereco = Socket_tcp_serv.accept()
        clientes.append(conexao)  # Armazena o cliente
        # Cria uma nova thread para gerenciar o cliente
        threading.Thread(target=gerenciar_cliente, args=(conexao, endereco)).start()

if __name__ == "__main__":
    servidor()
