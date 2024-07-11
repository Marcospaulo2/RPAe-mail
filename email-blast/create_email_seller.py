Seller_emails = {
"Ana": " Ana@example.com",
"Beatriz": "Beatriz@example.com",
"Bruna": "Bruna@example.com",
"Lucas": "Lucas@example.com",
"Maria": "Maria@example.com",

}
def create_file_seller_emails(sellers_emails, file_path ):
    with open(file_path, 'w', encoding='utf-8') as archive:
        for Seller, email in Seller_emails.items():
            archive.write(f'{Seller}, {email}\n')

file_path = 'Seller_emails.txt'
create_file_seller_emails(Seller_emails, file_path)