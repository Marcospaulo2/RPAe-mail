data = """ Seller, Products, Prices 
Ana, computers, 1500
Ana, Monitor, 500
Ana, keyboard, 1600
Ana, Tablets, 700 
Maria, computers, 1500
Maria, Notebook, 3500
Maria, keyboard, 4600
Maria, Tablets, 700 
Lucas, Mouse, 1500
Lucas, Monitor, 4500
Lucas, keyboard, 600
Lucas, Tablets, 7300 
Lucas, computers, 31500
Beatriz, Impressora, 500
Beatriz, keyboard, 2600
Beatriz, Fones, 700 
Beatriz, computers, 1500
Beatriz, Mini pc , 500
Bruna, keyboard, 4600
Bruna, Tablets, 700 
Bruna, computers, 21500
Bruna, Monitor, 2500
Bruna, keyboard, 600
Bruna, Tablets, 4700 """

file_path = 'sales.txt'
with open(file_path, 'w', encoding='utf-8') as archive:
    archive.write(data)