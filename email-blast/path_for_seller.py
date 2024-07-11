def dat_for_seller(file_path):
    with open(file_path, 'r', encoding='utf-8') as archive:
        lines = archive.readlines()

    header = lines[0]
    line_data = lines[1:]

    data_for_sallers = {}
    for line in line_data:
        Seller, Products, Prices = line.strip().split(',')
        if Seller not in data_for_sallers:
            data_for_sallers[Seller] = []
        data_for_sallers[Seller].append(f'{Seller}, {Products}, {Prices}')
 
    return header, data_for_sallers

def create_file_for_seller(header, data_for_sallers):
    files_created = []
    for Seller, data in data_for_sallers.items():
        vendor_file_path = f'C:\\RPAe-mail\\path_sellers\\{Seller}.txt'
        
        with open(vendor_file_path, 'w', encoding='utf-8') as archive:
            archive.write(header)
            for data in data:
                archive.write(f'{data}\n')
            files_created.append(vendor_file_path)
    return files_created

file_path = 'sales.txt'

header, data_for_sallers = dat_for_seller(file_path)

files_created = create_file_for_seller(header, data_for_sallers)
