import requests
from django.conf import settings


def get_token():
    print('get_token 실행1')
    access_data = {
        'imp_key': settings.IAMPORT_KEY,
        'imp_secret': settings.IAMPORT_SECRET
    }
    url = "https://api.iamport.kr/users/getToken"
    req = requests.post(url, data=access_data) # json 형태로 받을 예정
    print('get_token 실행2',req.status_code)
    access_res = req.json()
    print('get_token', access_res)

    if access_res['code'] == 0:
        return access_res['response']['access_token']
    else:
        return None


def payments_prepare(order_id, amount, *args, **kwargs):
    print('payments 실행1')
    access_token = get_token()
    print('payments 실행2', access_token)
    if access_token:
        access_data = {
            'merchant_uid': order_id,
            'amount': amount
        }
        url = "https://api.iamport.kr/payments/prepare"
        headers = {
            'Authorization': access_token
        } # 토큰값 집어 넣어준다.
        req = requests.post(url, data=access_data, headers=headers)
        res = req.json()
        if res['code'] != 0:
            raise ValueError("API 통신 오류")
    else:
        raise ValueError("토큰 오류")


def find_transaction(order_id, *args, **kwargs):
    access_token = get_token()
    if access_token:
        url = "https://api.iamport.kr/payments/find/" + order_id
        headers = {
            'Authorization': access_token
        }
        req = requests.post(url, headers=headers)
        res = req.json()
        if res['code'] == 0:
            context = {
                'imp_id': res['response']['imp_uid'],
                'merchant_order_id': res['response']['merchant_uid'],
                'amount': res['response']['amount'],
                'status': res['response']['status'],
                'type': res['response']['pay_method'],
                'receipt_url': res['response']['receipt_url']
            }
            return context
        else:
            return None
    else:
        raise ValueError("토큰 오류")