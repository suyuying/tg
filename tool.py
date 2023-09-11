import time

import requests

class TelegramBot:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.retry_times_max=3
    def send_message(self, message):
        url = f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chat_id}&text='
        count_try_times=0
        while count_try_times<self.retry_times_max:
            try:
                count_try_times+=1
                response = requests.get(url + message)
                print(response.text)
                return response.json()
            except Exception as e:
                print(e)
                time.sleep(1)
    def send_csv(self, csv_file):
        apiURL = f'https://api.telegram.org/bot{self.token}/sendDocument?chat_id={self.chat_id}'
        count_try_times = 0
        while count_try_times < self.retry_times_max:
            try:
                count_try_times += 1
                response = requests.post(apiURL, files=csv_file)
                print(response.text)
                return response.json()
            except Exception as e:
                print(e)
                time.sleep(1)
    def create_group_id(self):
        """
        when you create telegram group,after adding bot to ur group,you need to get group id!
        this def is used to update group, info
        """
        # 使用Bot Token向Telegram Bot API發送請求以獲取群組ID
        response = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')

        # 解析API回應以獲得群組ID
        if response.status_code == 200:
            data = response.json()
            # chat_id = data['result']['id']
            # print(f'The Group ID for {chat_name} is {chat_id}')
            print(data)
        else:
            print(f'Failed to retrieve Group ID: {response.status_code}')
    def get_group_id(self,chat_name="+1zmY14c1iTk4MmE1"):
        # 使用Bot Token向Telegram Bot API發送請求以獲取群組ID
        response = requests.get(f'https://api.telegram.org/bot{self.token}/getChat?chat_id={self.chat_id}')

        # 解析API回應以獲得群組ID
        if response.status_code == 200:
            data = response.json()
            chat_id = data['result']['id']
            print(f'The Group ID for {chat_name} is {chat_id}')
        else:
            print(f'Failed to retrieve Group ID: {response.status_code}')


