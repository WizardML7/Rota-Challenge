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
    
    def next(self):
        res = requests.get(f'{self.base_url}?request=next')
        self.cookies = res.cookies
        return json.loads(res.text)

# Example usage
rota_api = RotaAPI()
# print(rota_api.place(1))
# print(rota_api.move(2, 3))
# print(rota_api.status())
# print(rota_api.reset())

class RotaGame:
    
	def __init__(self):
		self.board = "---------"
		self.rota_api = RotaAPI
          
		  
	


#I need a method that can take in a board string with positions 0-8 with symbols p - c
#This method should account for whether there are all the pices on the board and whether to use place or move
#This could be split into two parts, place move and make move
#The first three turns should be place move and every additional one should be a make move until thirty moves have passed. 
#This is then repeated 50 times for hash
#Additionally player gets the first move. This means that placing at 0 will give us the top left corner. 
#I also need to find a programatic way to ensure that I only choose valid moves. 
#A valid move does not move farther than one connected component away
#It also does not override another piece
#Using nodes will allow for the checking of win conditions as well as valid moves easiest
#