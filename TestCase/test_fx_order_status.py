# !/usr/bin/python
#
# -*- coding:utf-8 -*-
from SysRequest.fxc import add_order_by_dzm,pay_order
from SysRequest.fxm import get_order_info
from SysRequest.dzm import get_dzm_order_info

def test_orderStatus_by_fxm_and_dzm():
    add_data = add_order_by_dzm()
    fxOrderId, orderId = add_data['result']['orderId'], add_data['result']['dzmResultJO']['result']['orderid']
    pay_order(fxOrderId=fxOrderId, orderId=orderId)
    d_fxm = get_order_info(fxOrderId)['result']['rows'][0]['status']
    d_dzm = get_dzm_order_info(fxOrderId)['result']['rows'][0]['sendDone']
    assert d_dzm == 1, "电子码系统订单异常"
    assert d_fxm == 3, "分销系统订单异常"
    print("测试通过，finsh。")

test_orderStatus_by_fxm_and_dzm()

