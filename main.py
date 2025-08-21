from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import requests
from datetime import datetime
import json


class AiAgentCardDebtCollector:
    def __init__(self):        
        load_dotenv()
        self.client = genai.Client()
        with open("config.json", encoding="utf-8") as config_file:
            self.config = json.load(config_file)
        
        
  
    def DebtsDataFromSheet(self,worksheet_id,api_key,sheet_range_to_read):
        request_url =f'https://sheets.googleapis.com/v4/spreadsheets/{worksheet_id}/values/{sheet_range_to_read}?key={api_key}'
        try:
            response = requests.get(request_url)
            response.raise_for_status()  # Lança um erro se a requisição falhar

            # Converte a resposta JSON em um dicionário Python
            data = response.json()

            # O campo 'values' contém os dados da sua planilha
            values = data.get('values', [])

            if not values:
                print('No Data Found in Sheet.')
                return values  
            else:
                print('Data readed from sheet succefully :')
                return values

        except requests.exceptions.RequestException as e:
            print(f'Erro in request found : {e}')

        except Exception as e:
            print(f'Erro  in request found : {e}')


 
    def AgentCreatMessage(self,name_friend, debt_description, debt_totalPrice):
        
        
        
        self.response = self.client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Crie e me retorne uma única mensagem, curta e divertida para essa pessoa {name_friend} avisando que ele tem de divida que passou no cartão do Mikael , mas que não fique muito com tom de cobrança, dos seguintes gastos {debt_description} e o valor total é de {debt_totalPrice} reais",
        config=types.GenerateContentConfig(
            system_instruction = "Você é um cobrador amigável, que além de cobrar quer divertir o dia da pessoa com mensagens curtas. Os valores separados por / são de parcelas do produto",
            thinking_config=types.ThinkingConfig(thinking_budget=0)  # Disables thinking
            )
        )
        return self.response.text   


if __name__ == '__main__':
    charge = AiAgentCardDebtCollector()
    now_month_year = datetime.now().strftime("%b-%y").lower()
    rows_info_debts_friends = charge.DebtsDataFromSheet(os.getenv("SPREADSHEET_ID"),os.getenv("API_KEY"),f"{now_month_year}!D13:G22")
    if not rows_info_debts_friends is None:
        for row in rows_info_debts_friends:
            if  charge.config["dictNumbersFriends"].get(row[0]) is not None:
                
                message = charge.AgentCreatMessage(name_friend=row[0], debt_description=row[1], debt_totalPrice=row[2])
                print(message)
                
                headers = {
                    'apikey': os.getenv("AUTHENTICATION_API_KEY"),
                    'Content-Type': 'application/json'
                }
                payload = {
                    'number': f'{charge.config["dictNumbersFriends"][row[0]]}',
                    'text': f'{message}',
                    # 'delay': 10000, # simular "digitando"
                }
                response = requests.post(
                    url=f'{os.getenv("BASE_URL")}/message/sendText/{os.getenv("INSTANCE_NAME")}',
                    json=payload,
                    headers=headers,
                )
                print(response.json())
                        
                
          
              
            else:
                print(f"Not exist number in dict on cofig to the name: {(row[0])}")

