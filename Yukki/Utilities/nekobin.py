import requests

def paste_to_nekobin(msg):
    data = msg
    key = (
        requests.post("https://nekobin.com/api/documents", json={"content": data})
        .json()
        .get("result")
        .get("key")
    )
    q = f"paste-{key}"
    url = f"https://nekobin.com/{key}"
    return url