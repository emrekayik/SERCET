#Bu program 2019 yılında Emre KAYIK tarafından oluşturulmuştur. ©EK
#Programın ismi server ve chat kelimelerinin birleşmesi ile oluşturulmuştur
import socket
import time
import ctypes



ctypes.windll.kernel32.SetConsoleTitleW("SERÇET SERVER                                                                                                                                                                                                                      EMRE KAYIK")

s = socket.socket()
host_name = socket.gethostname() 
ip_address = socket.gethostbyname(socket.gethostname()) 
s.bind((ip_address, 12345))
s.listen(3)
# print hoşgeldiniz
print('SERÇET SERVER a hoşgeldiniz')
time.sleep(3)
print("|--------------------------|\n|       EMRE KAYIK         |\n|                          |\n|	SERÇET	SERVER		   |\n|						   |\n|                          |\n|--------------------------|")   

# print senin ip addres
print("server IP adresi:",ip_address)
ad = input('isminizi giriniz: ')
bos = ' '
print('isminizden sonra mesajınızı yazıp gönderebilirsiniz')


while True:  
    print ('bağlantı bekleniyor')
    connection, client_address = s.accept()
    try:
        print ('bağlı', client_address)
        connection.send(str("Şimdi bağlısın").encode("utf-8")) 
      
        while True:
            data = connection.recv(1024).decode("utf-8")
            if data:

                print(list(host_name)[0],end="")
                print (host_name + " : %s" % data)

                new_data = str(input(ad + bos)).encode("utf-8")
                connection.send(new_data)       
    finally:

        connection.close()
