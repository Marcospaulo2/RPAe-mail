import win32com.client as win32
import os

outlook = win32.Dispatch('outlook.application')

name_archive =  'Seller_emails.txt'

with open(name_archive, 'r', encoding="utf-8") as archive:
    lines = archive.readlines()

for line in lines:
    data = line.strip().split(',')
    name = data[0]
    email = data[1]

    emailOutlook = outlook.CreateItem(0)

    emailOutlook.to = email
    emailOutlook.HTMLBody = emailOutlook.HTMLBody = f"""
    <html>
        <header>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line_height: 1.6;
                }}
                .container {{
                    max-width: 600px;
                    margin: 26px auto;
                    padding: 2Õpx;
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    background-color:#f9f9f9;

                }}
                . header {{
                
                    background-color:#007bff;
                    color :#fff;
                    text-align: center;
                    padding: 16px;
                    border-radius: 8px 8px 0 0;
                }}
                .content {{
                    padding:20px;
                }}
                .footer{{
                    text-align: center;
                    margin-top: 20px;
                    color: #666;
                }}

            </style>
        </header>
        <body>
            <div class="container">
                <div class="header">
                    <h2>Relatório de Vendas</h2>
                </div>
                <div class="content">
                    <p>Ola <b>{name}</b></p>    
                    <p>Espero que esteja bem. Segue abaixo o relatório com suas vendas mais recebidos
                    <p p>Atenciosamente,</p>
                </div>    
                <div class="footer">
                    <p>Este é um e-mail automático.Por favor, não responda.
                </div>
           </div>  
        </body>
    </html>

"""
    anexoEmail =  f'C:\\RPAe-mail\\path_sellers\\{name}.txt'

    if os.path.exists(anexoEmail):
        emailOutlook.Attachments.Add(anexoEmail)
    else:
        print(f'Arquivo{anexoEmail} não encotrado')

    emailOutlook.Save() #emailOutlook.Send() para enviar.