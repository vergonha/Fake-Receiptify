import requests
import re

class FakeReceiptify:
    def __init__(self, link: str, playlist: str):
        self.bearer = re.findall(r"access_token=(.*?)&", link)[0]
        self.playlist = re.findall(r"playlist\/(.*?)\?", playlist)[0]
        self.playlist_data = self.scrap_data()

    def playlist_data(self):
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': f'Bearer {self.bearer}'
            }

            i = requests.get(f'https://api.spotify.com/v1/playlists/{self.playlist}', 
            headers = headers)
            if i.status_code == 200: 
                return i.json()
            else:
                return "error"
    
    def scrap_data(self):
        data = self.playlist_data()
        if data != "error":
            return data['tracks']['items'][:10]
        return "error"

    def fake_receipt(self):
        fake = {'items': []}
        for item in self.playlist_data:
            infos = {
                'name': item['track']['name'],
                'type': 'track',
                'duration_ms': item['track']['duration_ms'],
                'artists': [{
                    "name": ', '.join((artist['name'] for artist in item['track']['artists']))
                }]
            }

            fake['items'].append(infos)   
        return f'displayReceipt({fake})'