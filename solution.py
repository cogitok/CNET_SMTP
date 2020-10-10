from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
   msg = "\r\n My message"
   endmsg = "\r\n.\r\n"
   emailTo = "jonanthonyhenderson@gmail.com"
   emailFrom: "jonanthonyhenderson@gmail.com" 
   # Create socket called clientSocket and establish a TCP connection with mailserver and port
   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect((mailserver,port))

   recv = clientSocket.recv(1024).decode()
 #  print(recv)
   if recv[:3] != '220':
  #     print('220 reply not received from server.')

   # Send HELO command and print server response.
   heloCommand = 'HELO Alice\r\n'
   clientSocket.send(heloCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
  # print(recv1)
   if recv1[:3] != '250':
   #    print('250 reply not received from server.')

   # Send MAIL FROM command and print server response.

   #print("Sending MAIL from CMD")
   mailfromcmd = 'MAIL FROM: ' + emailFrom + '\r\n'  
   clientSocket.send(mailFromCmd.encode())
   recv2 = clientSocket.recv(1024).decode()
   #print(recv2)
   if recv1[:3] !='250':
    #  print('250 reply not received')

   # Send RCPT TO command and print server response.
   #print("Sending RCPT")
   rcptToCmd = 'RCPT TO:' + emailTo + '\r\n'
   clientSocket.send(rcptToCmd.encode())
   recv3 = clientSocket.recv(1024).decode()
   if recv1[:3] != '250':
      #print(recv3)

   #print("Sending DATA")
    datacmd = 'DATA\r\n'
    clientSocket.send(datacmd.encode())
    recv4 = clientSocket.recv(1024).decode()
   #print(recv4)
    if recv4[:3] !='354':
     # print('354 reply not received')

   clientSocket.send(msg.encode())
   recv5 = clientSocket.recv(1024).decode()
   clientSocket.send(endmsg.encode())
   recv5 = clientSocket.recv(1024).decode())



   clientSocket.send(endmsg.encode())
   recv5 = clientSocket.recv(1024).decode()
   #print(recv5)
   if recv5[:3] != '250':
      # print('250 reply not receieved')

   quitCommand = 'QUIT\r\n","utf-8'
   clientSocket.send(quitCommand.encode())
   recv6 = clientSocket.recv(1024).decode()
   #print(recv6)  
   if recv6[:3] != '221':
       #print('221 REPLY not received')

   if __name__ == '__main__':
       smtp_client(1025,'127.0.0.1')
