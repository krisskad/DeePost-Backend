import json
from django.conf import settings
import os
import requests


def regenerate_access_token(refresh_token, client_id, client_secret, authorization, creds_file):
    url = "https://api.imgur.com/oauth2/token"

    payload = {
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'refresh_token'
    }

    response = requests.request("POST", url, data=payload)

    cred = response.json()

    obj = {
        "Authorization": authorization,
        "client_id": client_id,
        "client_secret": client_secret,
        "log": f"{e}"
    }

    obj.update(cred)

    with open(creds_file, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=4)


def get_imgur_images(page=1):
    # Opening JSON file
    creds_file = os.path.join(settings.BASE_DIR, "imgur_creds.json")
    f = open(creds_file)
    data = json.load(f)

    client_id = data["client_id"]
    client_secret = data["client_secret"]
    access_token = data["access_token"]
    refresh_token = data["refresh_token"]
    account_username = data["account_username"]
    authorization = data["Authorization"]

    url = f"https://api.imgur.com/3/account/{account_username}/images/{page}"
    header = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.request("GET", url, headers=header)
    all_data = response.json()
    if all_data["status"] == 200:
        return all_data
    else:
        regenerate_access_token(
            client_id=client_id,
            client_secret=client_secret,
            authorization=authorization,
            refresh_token=refresh_token,
            creds_file=creds_file
        )


