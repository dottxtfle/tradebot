import httpx ,json ,settings
http =httpx .AsyncClient ()
cookies ={'.ROBLOSECURITY':settings .settings ['cookie']}
headers ={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:69.0) Gecko/20100101 Firefox/69.0','Accept':'*/*','Accept-Language':'en-US,en;q=0.5','Content-Type':'application/json; charset=utf-8','X-CSRF-TOKEN':'TWSGXzUxT212','Connection':'keep-alive','Referer':'https://www.roblox.com/my/money.aspx','Cache-Control':'max-age=0',}
headers2 ={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:69.0) Gecko/20100101 Firefox/69.0','Accept':'application/json, text/javascript, */*; q=0.01','Accept-Language':'en-US,en;q=0.5','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','X-CSRF-TOKEN':'5HpedRy6Tri+','Connection':'keep-alive','Referer':'https://www.roblox.com/my/money.aspx',}
async def get_trades ():
    O0OOO00O0O0000OO0 =json .dumps ({'startindex':0 ,'statustype':'inbound'})
    OOOO00OO0O0O0OO0O =await http .post ('https://www.roblox.com/my/money.aspx/getmyitemtrades',data =O0OOO00O0O0000OO0 ,headers =headers ,cookies =cookies )
    if OOOO00OO0O0O0OO0O .status_code ==403 and OOOO00OO0O0O0OO0O .headers .get ('X-CSRF-TOKEN'):
        headers ['X-CSRF-TOKEN']=OOOO00OO0O0O0OO0O .headers .get ('X-CSRF-TOKEN')
        OOOO00OO0O0O0OO0O =await http .post ('https://www.roblox.com/my/money.aspx/getmyitemtrades',data =O0OOO00O0O0000OO0 ,headers =headers ,cookies =cookies )
    return OOOO00OO0O0O0OO0O
async def execute_trade (O0O0OOOO0OOO0O00O ,OOOO000000OOO0OO0 )
    OOO00OOO0OO00O0O0 ={'TradeID':O0O0OOOO0OOO0O00O ,'cmd':OOOO000000OOO0OO0 }
    OO00O00O00O0000O0 =await http .post ('https://www.roblox.com/trade/tradehandler.ashx',headers =headers2 ,cookies =cookies ,data =OOO00OOO0OO00O0O0 )
    if OO00O00O00O0000O0 .status_code ==403 and OO00O00O00O0000O0 .headers .get ('X-CSRF-TOKEN'):
        headers2 ['X-CSRF-TOKEN']=OO00O00O00O0000O0 .headers .get ('X-CSRF-TOKEN')
        OO00O00O00O0000O0 =await http .post ('https://www.roblox.com/trade/tradehandler.ashx',headers =headers2 ,cookies =cookies ,data =OOO00OOO0OO00O0O0 )
    return OO00O00O00O0000O0
async def resellers (OOO0OO0OOO0OO00OO ):
    OO00OOO0OO00000O0 =await http .get (f'https://economy.roblox.com/v1/assets/{OOO0OO0OOO0OO00OO}/resellers?limit=10',headers =headers ,cookies =cookies )
    return OO00OOO0OO00000O0 
