import requests


def list_files():
    response = requests.get("https://j1ytcgjjb6.execute-api.us-east-1.amazonaws.com/prod/files/")
    return response.json()


def put_files(body):
    response = requests.put("https://j1ytcgjjb6.execute-api.us-east-1.amazonaws.com/prod/file/", json=body)
    return response.json()


def get_file(file_name):
    response = requests.get(
        "https://j1ytcgjjb6.execute-api.us-east-1.amazonaws.com/prod/file/", params={"file_name": file_name}
    )
    return response.json()


print(list_files())
print(put_files(body={"file_name": "test.txt", "content": "Hello World"}))

print(list_files())

print(get_file(file_name="test.txt"))
