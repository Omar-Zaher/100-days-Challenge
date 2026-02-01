# ------- Imports ---------
import requests as rq
import os 
import datetime as dt

# ------ Pixela Class ---------
class Pixela:
    def __init__(self, token: str, username: str, graph_id: str):
        self.TOKEN = token
        self.USER = username
        self.GRAPH_ID = graph_id
        self.url = "https://pixe.la/v1"
        self.graph_url = f"{self.url}/users/{self.USER}/graphs/{self.GRAPH_ID}"
        self.graph_header = {
            "X-USER-TOKEN": self.TOKEN
        }
        self.today = dt.datetime.now()
    
    # ----- Methods for posting, updating, deleting, and pulling pixels -----
    # Adding a pixel
    def post(self, quantity: str):
        
        pixel_info ={
            "date": self.today.strftime("%Y%m%d"),
            "quantity": quantity
            
        }
        adding = rq.post(url=f"{self.graph_url}", json = pixel_info, headers= self.graph_header)
        print(adding.text)
    
    # Updating a pixel    
    def update(self, quantity: str, date: str):
        update_info ={
            "quantity": quantity
        }
        updating = rq.put(url=f"{self.graph_url}/{date}", json= update_info, headers= self.graph_header)
        print(updating.text)
    
    # Deleting a pixel    
    def delete(self, date: str):
        deleting = rq.delete(url=f"{self.graph_url}/{date}", headers= self.graph_header)
        print(deleting.text)
    
    # Pulling a pixel    
    def pull(self):
        pulling = rq.get(url= self.graph_url, headers= self.graph_header)
        print(pulling.text)
    
