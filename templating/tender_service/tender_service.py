from templating.tender_service import constants
import requests


class ProzorroTenderService:

    def send_request(self, method, endpoint, headers=None, data=None, add_params=None):
        headers = headers.copy() if headers else {}
        data = data.copy() if data else {}
        add_params = add_params.copy() if add_params else {}

        response = requests.Session().request(
            method=method,
            url=f'{constants.HOST}{endpoint}',
            headers=headers,
            data=data,
            params=add_params
        )
        if response.status_code < 500:
            return response.json()
        else:
            print(response.content)


    def get_tender(self, hash):
        endpoint = f'{constants.GET_TENDER_ENDPOINT}{hash}'
        return self.send_request('GET', endpoint)