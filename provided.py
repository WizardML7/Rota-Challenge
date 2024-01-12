import requests
import json

class RotaAPI:

    def __init__(self):
        self.base_url = 'https://rota.praetorian.com/rota/service/play.php'
        res = requests.get(f'{self.base_url}?request=new&email=dml3483@g.rit.edu')
        self.cookies = res.cookies

    def place(self, x):
        response = requests.get(f'{self.base_url}?request=place&location={x}', cookies=self.cookies)
        return json.loads(response.text)

    def move(self, x, y):
        response = requests.get(f'{self.base_url}?request=move&from={x}&to={y}', cookies=self.cookies)
        return json.loads(response.text)

    def status(self):
        response = requests.get(f'{self.base_url}?request=status', cookies=self.cookies)
        return json.loads(response.text)

    def reset(self):
        res = requests.get(f'{self.base_url}?request=new')
        self.cookies = res.cookies
        return json.loads(res.text)

# Example usage
rota_api = RotaAPI()
print(rota_api.place(1))
print(rota_api.move(2, 3))
print(rota_api.status())
print(rota_api.reset())
