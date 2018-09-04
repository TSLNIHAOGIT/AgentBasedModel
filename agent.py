import queue
# from numpy import
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# print(len(a1[1])==0,a1[0])
iris=load_iris()
class OrdersBoook(object):
    # def agent_system(self):
    #     while True:
    #         select_agent()#随机选择阿根廷进行决策
    #         agent_decide()#angent决策函数
    #         agent_send_order()#agent提交订单
    #         update_order_book()#更新订单簿状态
    def choose_best_orders(self):
        pass
    def clear_orders(self):
        pass
    def trading_system(self,bid_time,ask_time,trading_price,bid_price,ask_price):
        while True:
            # choose_best_orders()#选择最佳买卖订单
            if bid_price>=ask_price:

                if bid_time>=ask_time:
                    trading_price=bid_price
                else:
                    trading_price =ask_price
                if bid_volume<ask_volume:
                    trading_volume=bid_volume
                    ask_volume=ask_volume-trading_volume
                else:
                    trading_volume = ask_volume
                    bid_volume=bid_volume-trading_volume
            else:
                return
            # store_trading_information()#存储交易信息
            # update_order_book()#更新订单状态
            # if day_time_end :#如果当天交易结束
            #     clear_order_book()
class decision_funciton(object):
    def __init__(self):
        self.samples=iris.data
        self.target=iris.target

    def logisitic_train(self,sample,target):
        cls=LogisticRegression()
        cls.fit(sample,target)
        return cls
    def logisitic_predict(self,cls):
        result=cls.predict([1,4,1,5])
        return result
    def main(self):
        cls=self.logisitic_train(self.samples,self.target)
        result=self.logisitic_predict(cls)
        print(result)
if __name__=='__main__':
    deci_func=decision_funciton()
    deci_func.main()



