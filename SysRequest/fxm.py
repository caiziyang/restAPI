import requests
import yaml

f = open('../ReConfig/fxm.yaml', 'rb', encoding='utf-8')
content = yaml.load(f, Loader=yaml.FullLoader)

def cookie():
    with open("../ReConfig/cookie.txt", "rb") as f:  # 打开文件
        data = f.read()  # 读取文件
        return {"cookie": data}


def get_order_info(orderId):
    url = 'https://mt.lhs11.com/fxm/services/local/fxm/order/order.japi'
    r_data = content['fxm_search_base_data']
    r_data['params']['variables']['id'] = orderId
    headers = cookie()
    r = requests.post(url=url, headers=headers, json=r_data)
    print("正在查询fxm订单状态....")
    return r.json()


def get_logistics_order_info(orderId):
    pass

# if __name__ == '__main__':
#     get_order_info(2020040111411220066)

