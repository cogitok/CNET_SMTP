from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
   msg = "\r\n My message"
   endmsg = "\r\n.\r\n"

   # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
   mailserver = "127.0.0.1"
   port = "1025"
   # Create socket called clientSocket and establish a TCP connection with mailserver and port
   clientsocket = socket(AF_INET, SOCK_STREAM)
   clientsocket.connect((mailserver,mailport))
   recv = mailclientsocket.recv(1024)
   #print (recv)
   #if recv[:3] != '250':
    #   print ('220 reply not received')


   # Send HELO command and print server response.
   heloCommand = 'HELO Alice\r\n'
   clientSocket.send(heloCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   #print(recv1)
   #if recv1[:3] != '250':
     #  print('250 reply not received from server.')

   # Send MAIL FROM command and print server response.
   mailfrom = 'Mail from: <jonanthonyhenderson@gmail.com\r\n'
   clientsocket.send(mailfrom)
   recv2 = clientsocket.recv(1024)
   #print (recv1)
   #if recv2[:3] != '250':
       #print("250 reply not received")


   # Send RCPT TO command and print server response.
   rcptToCommand = 'RCPT TO: <nojfree@gmail.com>\r\n'
   #print (rcptToCommand)
   clientsocket.send(rcptToCommand)
   recv3 = clientsocket.recv(1024)
   #print (recv1)
   #if recv3[:3] != '250':
      # print ("250 reply to received")


  
   # Send DATA command and print server response.
   dataCmd = 'DATA\r\n'
   clientsocket.send(dataCmd)
   recv4 = clientsocket.recv(1024)
   #print (recv1)
   #if recv4[:3] != '250'
     #  print('250 reply not received')

   # Send message data.
   clientsocket.send(msg)
   #print ('Message is: , msg')

   # Message ends with a single period.
   clientsocket.send(endmsg)
   #print ('End message is: ', endmsg)
   recv5 = clientsocket.recv(1024)
   #print (recv1)
   #if recv5[:3] != ‘250’:
      # print (‘250 reply not recieved from server.’)


   # Send QUIT command and get server response.

 quitCommand = ‘QUIT\r\n’
 clientsocket.send(quitCommand)
 recv1 = SMTPClientSocket.recv(1024)
 #rint recv1
 #if recv1[:3] != ‘250’:
     #print (‘250 reply not recieved from server.’)




if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')



