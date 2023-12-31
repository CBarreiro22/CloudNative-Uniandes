import json
import os
import uuid

import requests

TOKEN_TRUE_NATIVE = os.environ["TOKEN_SERVICE"]


class TrueNativeService:

    @staticmethod
    def register_card(body_card_creation):
        transaction_identifier = uuid.uuid4()
        headers = {
            'Authorization': TOKEN_TRUE_NATIVE,
            'Content-Type': 'application/json'
        }
        body_request = {
            "card": {
                "cardNumber": body_card_creation["cardNumber"],
                "cvv": body_card_creation["cvv"],
                "expirationDate": body_card_creation["expirationDate"],
                "cardHolderName": body_card_creation["cardHolderName"]
            },
            "transactionIdentifier": f"{transaction_identifier}"
        }
        updated_body_json = json.dumps(body_request)
        response = requests.post(os.environ["TRUE_NATIVE_PATH"] + '/native/cards', headers=headers,
                                 data=updated_body_json)
        if response.status_code == 201:
            return response.json(), ''
        else:
            return "", response.status_code

    @staticmethod
    def get_cards(token, card_number, cvv, expiration_date, card_holder_name, transaction_identifier):
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        body_request = {
            "card": {
                "cardNumber": card_number,
                "cvv": cvv,
                "expirationDate": expiration_date,
                "cardHolderName": card_holder_name
            },
            "transactionIdentifier": transaction_identifier
        }
        updated_body_json = json.dumps(body_request)
        response = requests.post(os.environ["TRUE_NATIVE_PATH"] + '/native/cards', headers=headers,
                                 data=updated_body_json)
        if response.status_code == 201:
            return response.json(), ""
        else:
            return "", response.status_code

    @staticmethod
    def get_card_status(ruv):
        headers = {
            'Authorization': TOKEN_TRUE_NATIVE,
            'Content-Type': 'application/json'
        }
        response = requests.get(os.environ["TRUE_NATIVE_PATH"] + '/native/cards/' + ruv, headers=headers)
        if response.status_code == 200:
            return response.json(), ''
        else:
            return '', response.status_code
