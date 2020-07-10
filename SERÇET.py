#Bu program 2019 yılında Emre KAYIK tarafından oluşturulmuştur. ©EK
#Programın ismi server ve chat kelimelerinin birleşmesi ile oluşturulmuştur
import socket  
import time
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("SERÇET                                                                                                                                                                                                                             EMRE KAYIK")

s = socket.socket()
host_name = socket.gethostname() 
print('SERÇET e hoşgeldiniz')
time.sleep(3) 
print("|--------------------------|\n|       EMRE KAYIK         |\n|                          |\n|	SERÇET	           |\n|			   |\n|                          |\n|--------------------------|")
ad = input('isminizi giriniz: ')
time.sleep(2) 
server=input("IP GİRİNİZ: ")
bos = ' '
print('isminizden sonra mesajınızı yazıp gönderebilirsiniz')
s.connect((server,12345))  
data = s.recv(1024).decode("utf-8")
print(server+": "+data) 
while True:
		    new_data = str(input(ad + bos)).encode("utf-8")
		    s.sendall(new_data)
		    data = s.recv(1024).decode("utf-8")
		    print(host_name+ " : "+data)     
# bağlantıyı kapat
s.close()  
#server
