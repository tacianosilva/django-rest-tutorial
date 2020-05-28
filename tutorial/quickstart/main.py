import json, requests


def main():
    print("Teste API")
    url = "http://localhost:8000/groups/"
    username = 'admin'
    password = 'password123'
    data_str = {'username': 'admin', 'password': 'password123'}
    data = json.dumps(data_str)
    response = requests.get(url, auth=(username, password))
    print(response.status_code)
    print(response.headers['content-type'])
    print(response.encoding)
    print(response.text)
    # print(response.json())
    # print(response.content)

    # token = json.loads(response.content)['']
    # print(token)

    data = {'name': 'Empreendedores'}
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    response = requests.post(url, data, auth=(username, password))
    print(response.status_code)
    print(response.text)

    data = {'name': 'Serviços'}
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    url = 'http://localhost:8000/groups/2/'
    response = requests.put(url, data, auth=(username, password))
    print(response.status_code)
    print(response.text)

    url = 'http://localhost:8000/groups/2/'
    response = requests.delete(url, auth=(username, password))
    print(response.status_code)
    print(response.text)


if __name__ == "__main__":
    main()
