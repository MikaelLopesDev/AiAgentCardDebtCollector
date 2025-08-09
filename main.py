from google import genai
from dotenv import load_dotenv


class AiAgentCardDebtCollector:
    def __init__(self):        
        load_dotenv()
        self.client = genai.Client()



    def AgentCreatMessage(self,name_friend, debt_description, debt_totalPrice):
        
        self.response = self.client.models.generate_content(
            model = "gemini-2.5-flash",
            contents= f"Crie e me retorne uma única mensagem, curta e divertida para o meu amigo {name_friend} avisando que ele tem de divida, mas que não fique muito com tom de cobrança, no meu cartão os seguintes produtos { debt_description} e o valor total é de  {debt_totalPrice} reais"

        )
        return self.response.text



if __name__ == '__main__':
    charge = AiAgentCardDebtCollector()
    message = charge.AgentCreatMessage(name_friend="Manoel", debt_description="parcela 9/12 do minoxil, 9/12 roupas monte Leste", debt_totalPrice="50,67")
    
    print(message)

