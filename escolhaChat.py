import os

def main(){
    protocolo = int(input("Olá, usuário! Qual protocolo você gostaria de usar para rodar o chat?\n Digite 1 para UDP e 2 para TCP"))

    if protocolo == 1{
        quem = int(input("Digite 1 para cliente e 2 para servidor"))
        if quem == 1{
             os.system("python UDP/clienteUDP.py")
        }else if quem == 2{
             os.system("python UDP/teTCPdorUDP")

        }

    }else if protocolo == 2{
 
        if quem == 1{
             os.system("python TCP/clienteTCP.py")
        }else if quem == 2{
             os.system("python TCP/servidorTCP.py")

        }

    }
}




