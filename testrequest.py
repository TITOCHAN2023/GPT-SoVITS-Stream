import requests

def main():
    url = "http://localhost:8176/tts"
    data = {
        "text": "你好 我是今天的主持人",
        "voice": "Person1",
    }
    response = requests.post(url, json=data)
    print(response.json()['path'])


if __name__ == '__main__':
    main()