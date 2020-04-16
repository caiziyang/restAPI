#!/usr/bin/python

# -*- coding:utf-8 -*-
import requests
import json
import yaml
from urllib import parse


f = open('../ReConfig/fxc.yaml', 'rb', encoding='utf-8')


content = yaml.load(f, Loader=yaml.FullLoader)

def add_order_by_dzm():
        url = 'https://fx3t-ysqg.lhs11.com/fxc/services/ms/fxc/store@addOrderByDZM.japi'
        params = content['add_order_by_dzm']
        data = parse.urlencode(params).encode('utf-8')
        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        r = requests.post(url=url, params=data, headers=headers)
        print("创建抢购订单成功")
        return r.json()

def pay_order(fxOrderId, orderId):

        url = 'https://fx3t-ysqg.lhs11.com/fxc/services/ms/fxc/store@payOrder.japi'
        params = {"variables[orderId]": orderId,
                  "variables[fxOrderId]": fxOrderId}

        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        data = parse.urlencode(params).encode('utf-8')
        r = requests.post(url=url, params=data, headers=headers)
        print("支付抢购订单成功")
        return r.json()

# if __name__ == '__main__':
#         add_data = add_order_by_dzm()
#         fxOrderId,orderId=add_data['result']['orderId'],add_data['result']['dzmResultJO']['result']['orderid']
#         pay_order(fxOrderId=fxOrderId,orderId=orderId)