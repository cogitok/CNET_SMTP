from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientsocket = socket(AF_INET, SOCK_STREAM)
    clientsocket.connect(('mailserver', port))
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO gmail.com\r\n'
    clientsocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    mailsout = 'MAIL FROM: nojfree@gmail.com\r\n'
    clientsocket.send(mailsout.encode())
    recv2 = clientsocket.recv(1024).decode()
    #print(recv2)
    #if recv2[:3] != '250':
        #print('250 reply not received from server')

    # Send RCPT TO command and print server response.
    recfrom = 'RCPT TO: jonanthonyhenderson@gmail.com\r\n'
    clientsocket.send(recfrom.encode())
    recv3 = clientsocket.recv(1024).decode()
    #print(recv3)
    #if recv3[:3] != '250':
       #print('250 reply not received from server')

    datato = 'DATA\r\n'
    clientsocket.send(datato.encode())
    recv4 = clientsocket.recv(1024).decode()
    #print(recv4)
    #if recv4[:3] != '354':
       #print('reply not recveied ')

    clientsocket.send('SUBJECT: HELLO\r\n'.encode())
    clientsocket.send(msg.encode())

    # end message with single period
    clientsocket.send(endmsg.encode())
    recv5 = clientsocket.recv(1024).decode()
    #print(recv5)
    #if recv5[:3] != '250':
        #print('250 reply not received')

    quitcmd = 'QUIT\r\n'
    clientsocket.send(quitcmd.encode())
    recv6 = clientsocket.recv(1024).decode()
    #int(recv6)
    #if recv6[:3] != '221':
        #print('221 reply not received from server')


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')






