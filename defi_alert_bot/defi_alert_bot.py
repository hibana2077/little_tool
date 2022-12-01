# MIT License

# Copyright (c) 2022 李軒豪

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import time
import requests

LAB_WEBHOOK_URL = ''


class Discord_webhook :
    def __init__(self, url):
        self.url = url
        self.enable_embed = False
        self.enable_content = False
        self.embed = {}

    def set_content(self, content):
        self.enable_content = True
        self.content = content

    def set_embed(self, embed):
        self.enable_embed = True
        self.embed = embed

    def send(self):
        if self.enable_embed and self.enable_content:
            payload = {
                'username': 'defi_stablecoin_alert_bot',
                'avatar_url':'https://cdn-icons-png.flaticon.com/512/4745/4745932.png',
                'content': self.content,
                'embeds': [self.embed]
            }
        elif self.enable_embed:
            payload = {
                'username': 'defi_stablecoin_alert_bot',
                'avatar_url':'https://cdn-icons-png.flaticon.com/512/4745/4745932.png',
                'embeds': [self.embed]
            }
        elif self.enable_content:
            payload = {
                'username': 'defi_stablecoin_alert_bot',
                'avatar_url':'https://cdn-icons-png.flaticon.com/512/4745/4745932.png',
                'content': self.content
            }
        else:
            raise Exception('No content or embeds found')
        result = requests.post(self.url, json=payload)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(result.status_code))

class Defi:
    def __init__(self):
        self.url = 'https://yields.llama.fi/pools'
        self.webhook = Discord_webhook(LAB_WEBHOOK_URL)

    def query(self):
        r = requests.get(self.url)
        if r.status_code == 200:
            return r.json()['data']
        else:
            return r.status_code

    def get_defi(self):
        data = self.query()
        new_data = [t for t in data if t['stablecoin'] == True]
        return new_data

    def top_apy_defi(self, data):
        return sorted(data, key=lambda x: x['apy'], reverse=True)

    def get_website(self,pools):
        return 'https://defillama.com/yields/pool/'+pools
        
    def send_alert(self, data):
        temp_data = [[t['chain'],t['project'],t['symbol'],t['apy'],t['pool']] for t in data]
        self.webhook.set_embed(
            {
            'author': {
                'name': 'hibana2077🤑',
                'url': 'https://github.com/hibana2077',
                'icon_url': 'https://i.pinimg.com/564x/3c/cb/5d/3ccb5de9c80a5bc3cdbea6d018e02a1a.jpg'
            },
            'title': f"DEFI ALERT",
            'description': '''
This is a message from `defi_alert_bot`.
if you want to know more information, please click the link below.
also, you can check the code on [github](https://github.com/hibana2077).
            ''',
            'color': 0x00ff00,
            'fields': [
                {
                    'name': 'APY Tool',
                    'value': '[caculate APY](https://www.coingecko.com/en/impermanent-loss-calculator)',
                    'inline': True
                },
                {
                    'name': 'DEFI ranking',
                    'value': 'DEFI [ranking](https://defillama.com/)',
                    'inline': True
                },
                {
                    'name': 'Wallet dashboard',
                    'value': 'Trace your assets [here](https://zapper.fi/)',
                    'inline': True
                },
                {
                    'name': f"{temp_data[0][0]} : {temp_data[0][1]} : {temp_data[0][2]} : {temp_data[0][3]}",
                    'value': f"[{temp_data[0][2]}]({self.get_website(temp_data[0][4])})",
                },
                {
                    'name': f"{temp_data[1][0]} : {temp_data[1][1]} : {temp_data[1][2]} : {temp_data[1][3]}",
                    'value': f"[{temp_data[1][2]}]({self.get_website(temp_data[1][4])})",
                },
                {
                    'name': f"{temp_data[2][0]} : {temp_data[2][1]} : {temp_data[2][2]} : {temp_data[2][3]}",
                    'value': f"[{temp_data[2][2]}]({self.get_website(temp_data[2][4])})",
                },  
                {
                    'name': f"{temp_data[3][0]} : {temp_data[3][1]} : {temp_data[3][2]} : {temp_data[3][3]}",
                    'value': f"[{temp_data[3][2]}]({self.get_website(temp_data[3][4])})",
                },
                {
                    'name': f"{temp_data[4][0]} : {temp_data[4][1]} : {temp_data[4][2]} : {temp_data[4][3]}",
                    'value': f"[{temp_data[4][2]}]({self.get_website(temp_data[4][4])})",
                },
                {
                    'name': f"{temp_data[5][0]} : {temp_data[5][1]} : {temp_data[5][2]} : {temp_data[5][3]}",
                    'value': f"[{temp_data[5][2]}]({self.get_website(temp_data[5][4])})",
                },
                {
                    'name': f"{temp_data[6][0]} : {temp_data[6][1]} : {temp_data[6][2]} : {temp_data[6][3]}",
                    'value': f"[{temp_data[6][2]}]({self.get_website(temp_data[6][4])})",
                },
                {
                    'name': f"{temp_data[7][0]} : {temp_data[7][1]} : {temp_data[7][2]} : {temp_data[7][3]}",
                    'value': f"[{temp_data[7][2]}]({self.get_website(temp_data[7][4])})",
                },
                {
                    'name': f"{temp_data[8][0]} : {temp_data[8][1]} : {temp_data[8][2]} : {temp_data[8][3]}",
                    'value': f"[{temp_data[8][2]}]({self.get_website(temp_data[8][4])})",
                },
                {
                    'name': f"{temp_data[9][0]} : {temp_data[9][1]} : {temp_data[9][2]} : {temp_data[9][3]}",   
                    'value': f"[{temp_data[9][2]}]({self.get_website(temp_data[9][4])})",
                }
            ],
            'thumbnail': {
                'url':'https://i.pinimg.com/564x/98/ad/46/98ad4666e2f6e59d112be15fd0ed597f.jpg'
            },
            'footer': {
                "text" : "投資は自己責任でお願いします。",
                'icon_url': 'https://i.pinimg.com/564x/96/c2/d8/96c2d82136088fc6c99c08e3e2ebcaf5.jpg'
            }
        })
        self.webhook.send()

if __name__ == '__main__':
    while True:
        try:
            defi = Defi()
            data = defi.get_defi()
            top_apy_defi = defi.top_apy_defi(data)
            defi.send_alert(top_apy_defi)
            time.sleep(3600*4)
        except Exception as e:
            print(e)
            time.sleep(3600*4)

