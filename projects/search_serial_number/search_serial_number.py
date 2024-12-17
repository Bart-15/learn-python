import os
import datetime
import time
import re

def search_serial_number(path):
  pattern = r'\bN[a-zA-Z]{3}-\d{5}\b'
  serial_numbers = []
  start_time = time.time()

  for root, dirs, files in os.walk(path):
    for file in files:
      if file.endswith('.txt'):
        file_path = os.path.join(root, file)

        with open(file_path, 'r') as text_file:
          content = text_file.read()
          matches = re.findall(pattern, content)

          if matches:
            serial_numbers.append((file, matches[0]))
  
  today_date = datetime.datetime.today().strftime('%d/%m/%y')
  duration = time.time() - start_time
  duration_rounded = round(duration)
   
  print('-' * 50)
  print(f'''
  Search Date: {today_date}

  {'FILE':<10} {'SERIAL NO.':<15}
  ----       -----------
  ''')

  for file, serial in serial_numbers:
    print(f'{file:<10}    {serial:<15}')
  
  print(f'''
  Numbers found: {len(serial_numbers)}
  Search duration: {duration_rounded} seconds
  ''')

  print('-' * 50)



search_serial_number('dir_out')