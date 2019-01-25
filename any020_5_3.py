count = 0

while(True):   
  entry = input('Skriv ett tall eller avslutt for a avslutte programmet:')

  if entry == 'avslutt':
    print('Adjo', count)   
    break
  elif isinstance(entry, int):
    count += int(entry)       
  else:
    print('Du skrev hverken tall eller avlsutt')   
    
  print('Forelopig sum: ', count) 
  
    
