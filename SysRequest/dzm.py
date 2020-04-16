import requests
import yaml
from ReConfig.ReConfig import test_Case


def cookie():
    with open("../ReConfig/cookie.txt", "r") as f:  # 打开文件
        data = f.read()  # 读取文件
        return {"cookie": data}

#查询DZM订单发货状态
def get_dzm_order_info(fxOrderId):
    url = 'https://mt.lhs11.com/dzm/services/local/dzm/code/code.japi'
    r_data =test_Case()['dzm_search_base_data']
    r_data['params']['variables']['dealId'] = fxOrderId
    headers = cookie()
    r = requests.post(url=url, headers=headers, json=r_data)
    print("正在查询dzm订单状态....")
    return r.json()

def get_dzm_logistics_order_info(fcOrderId):
    pass

if __name__ == '__main__':
    print(test_Case())
    # get_dzm_order_info(2020040917061245005)