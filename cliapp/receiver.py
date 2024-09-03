import socket
import datetime
import time

#socket.AF_INET-> through the internet
# socket.SOCK_DGRAM->udp protocol/ tcp protocol
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# ip_address =  "192.168.154.200"
ip_address = "127.0.0.1"
port_no = 63500
complete_address = (ip_address,port_no)
s.bind(complete_address)
print("....hey i am listening....")
while True:
    Data = s.recvfrom(100)
    message = Data[0]
    message = message.decode('ascii')
    sender_ip = Data[1][0]
    sender_port = Data[1][1]

    date = datetime.date.today()
    current_time=time.strftime("%H:%M:%S")
    message_with_datetime = f"{date}  ({current_time}) : message -> {message}"    
    file = open(sender_ip+'(S_to_R).txt','a')
    file.write(message_with_datetime+"\n")
    file.close()
    print(message)
    target_address = (sender_ip,sender_port)
    


