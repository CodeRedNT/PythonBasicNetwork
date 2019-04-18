from socket import *
import time
startTime = time.time()

if __name__ == '__main__':
   target = input('Informe o IP a ser scanneado: ')
   t_IP = gethostbyname(target)
   print ('Iniciando scan: ', t_IP)
   
   for i in range(50, 500):
      s = socket(AF_INET, SOCK_STREAM)
      
      conn = s.connect_ex((t_IP, i))
      if(conn == 0) :
         print ('Porta %d: OPEN' % (i,))
      s.close()
print('Tempo total:', time.time() - startTime)