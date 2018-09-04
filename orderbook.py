import queue
class Order(object):
    def __init__(self,agent):
        pass
    def decision_function(self,history_info):
        pass
    def utility_function(self):
        pass

    pass
# class OrderBook(object):
#     def __init__(self):
#         self.sell=-1#表示当前卖单队列为空的标志
#         self.buy=-1#表示当前买单队列为空的标志
#         q = queue.Queue()
#
#         #提交订单
#     def place_order(self,order,world):
#         is_placed=False
#         if(order.sell_or_buy==1):#当前订单为卖单
#             print('卖单')
#             if((order.price>buy) or (buy==-1)):#当前订单为限价订单
#                 is_placed=place_limit_order_s(order)
#                 print('限价')
#             else:
#                 is_placed = place_market_order_s(order)
#                 print('市价')
#         else:#当前订单为买单
#             print('买单')
#             if ((order.price > =sell) and (sell !== -1)):  # 当前订单为市价订单
#                 is_placed = place_market_order_b(order):
#                 print('市价')
#             else:
#                 is_placed = place_limit_order_b(order):
#                 print('限价')
#         return is_placed
#
#     # 提交限价卖订单
#     def place_limit_order_s(self,order):
#         is_placed=False
#         if(sell==-1):#即当前卖单队列为空时，在卖单队列中新建订单队列
#             sell_queue.put(create_order_queue(order))#原文java方法将指定元素e追加到此列表的末尾
#             sell=order.price#把新来订单的价格赋值给sell
#             is_placed=True#结束提交订单
#             order.agent.orders.add(order)#设置agent订单队列    不太明白？？？？？？？
#         else:#当前订单簿中有卖单队列
#             if(order.price<sell):#更改最优卖价
#                 sell=order.price
#             for i in sell_queue.size():#在卖单队列中插入防止订单
#                 current_qq=sell_queue.get(i)
#                 if(order.price<current_qq.price)#队列中不存在欲提交价格
#                     sell_queue.put(i,create_order_queue(order))#在卖单队列中插入订单队列
#                     is_placed=True
#                     order.agent.orders.add(order)  # 设置agent订单队列
#                     break#结束提交订单
#                 elif(order.price==current_qq.price):#队列中存在欲提交叫个
#                     current_qq.set_total_share(current_qq.get_total_share()+order.share)
#                     #sell_queue.set(i,currnet_qq)#在卖单队列中添加订单，可省
#                     is_placed=True
#                     order.agent.orders.add(order)  # 设置agent订单队列
#                     break  # 结束提交订单
#              if(not is_placed)  #在卖单队列的尾部新建订单队列
#                  sell_queue.add(create_order_queue(order))
#                  is_placed=True
#                  order.agent.orders.add(order)  # 设置agent订单队列
#
#             return is_placed
