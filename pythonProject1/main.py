import urllib.request
import urllib.parse

# def request():
#     data = urllib.parse.quote(
#         '{"name":"Barkov Danil Nikolaevich, 11-906", "currency1":"JPY", "currency2":"CHF", "currency3":"NOK", "currency4":"AUD", "strategy": "S2"}')
#     resp = urllib.request.urlopen("http://89.108.115.118/currency?value=" + data).read()
#     print(resp)

def request():
    data = urllib.parse.quote(
        '{"name":"Romanov Oleg Vladimirovich, 11-906", "currency1":"CNY", "currency2":"JPY", "currency3":"USD", "currency4":"AUD", "strategy": "S1"}')
    resp = urllib.request.urlopen("http://89.108.115.118/currency?value=" + data).read()
    print(resp)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    request()