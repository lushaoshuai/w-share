import time
import datetime
import itchat
import tushare

def login():
    Help='请输入股票代码:\n请输入最低预警:\n请输入最高预警:\n example:\n600516 18.55 23.22\n\n退出登录可结束查询'
    itchat.auto_login(True)
    itchat.send(Help,'filehelper')
    
def stock(Text):
    while(True): 
            time1=datetime.datetime.now()
            now=time1.strftime('%H:%M:%S')
            print(type(Text))
            list1=Text.split()
            print(list1)
            data=tushare.get_realtime_quotes(list1[0])
            price_low=list1[1]
            price_high=list1[2]
            r1=float(data['price'])
            r2=float(data['open'])
            m=str(data['name'])
            print(data['name'])
            h=m.split()
            print(h)
            name=h[1]
            print(r1-r2)
            content=name+'\n'+now+'\n'+'当前价格为'+str(r1)
            if r1<=float(price_low):
                itchat.send('低于最低预警价格\n'+content+'\n当前涨幅'+str('%.2f' %((r1-r2)/r2*100))+'%','filehelper')
                break      

            elif r1>float(price_high):
                itchat.send('高于最高预警价格\n'+content+'\n当前涨幅'+str('%.2f' %((r1-r2)/r2*100))+'%','filehelper')
                break
            else:
                itchat.send('','filehelper')
                time.sleep(3)
                print(content)
    
   
@itchat.msg_register(itchat.content.TEXT)
def information(msg):
    print(msg['FromUserName'])
    if msg['FromUserName']=='@18270de907ba35e478e7ef56b6652dc05a54b80c8891b141841dbb239eec5008':
        text=msg['Text']
        stock(text)
    
if __name__=='__main__':
                  
    login()
    itchat.run()

'''
后续可以加入多只股票同时监测
股价溢出午休闹钟叫醒

'''


        
    
        
            
            














