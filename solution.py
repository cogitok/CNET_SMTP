from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, 1025))
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    mailsout = 'MAIL FROM: nojfree@gmail.com\r\n'
    clientSocket.send(mailsout.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2)
    #if recv2[:3] != '250':
        #print('250 reply not received from server')

    # Send RCPT TO command and print server response.
    recfrom = 'RCPT TO: jonanthonyhenderson@gmail.com\r\n'
    clientSocket.send(recfrom.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3)
    #if recv3[:3] != '250':
       #print('250 reply not received from server')

    datato = 'DATA\r\n'
    clientSocket.send(datato.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv4)
    #if recv4[:3] != '354':
       #print('reply not recveied ')

    clientSocket.send('SUBJECT: HELLO\r\n'.encode())
    clientSocket.send(msg.encode())

    # end message with single period
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    #print(recv5)
    #if recv5[:3] != '250':
        #print('250 reply not received')

    quitcmd = 'QUIT\r\n'
    clientSocket.send(quitcmd.encode())
    recv6 = clientSocket.recv(1024).decode()
    #int(recv6)
    #if recv6[:3] != '221':
        #print('221 reply not received from server')


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')






