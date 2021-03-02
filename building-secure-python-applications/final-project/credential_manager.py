import json


def load_credential_db():
    with open("credentials.json") as f:
        return json.load(f)


def save_credential_db():
    with open("credentials.json", "w") as f:
        return json.dump(credentials_db, f)


credentials_db = load_credential_db()
