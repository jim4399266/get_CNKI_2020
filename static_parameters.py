import time
class Parameters(object):
    def __init__(self):
        self.cnkiUserKey = '3cf841c8-ec7f-50cb-a8f1-c7010190d461'
        self.headers_kns = {
            'Host': 'kns.cnki.net',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
            'Sec-Fetch-Mode': 'nested-navigate',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Sec-Fetch-Site': 'same-origin',
            # 'Referer': 'https://kns.cnki.net/kns/brief/brief.aspx?pagename=ASP.brief_result_aspx&isinEn=1&dbPrefix=SCDB&dbCatalog=%e4%b8%ad%e5%9b%bd%e5%ad%a6%e6%9c%af%e6%96%87%e7%8c%ae%e7%bd%91%e7%bb%9c%e5%87%ba%e7%89%88%e6%80%bb%e5%ba%93&ConfigFile=SCDB.xml&research=off&t=1571652866593&keyValue=&S=1&sorttype=(%e8%a2%ab%e5%bc%95%e9%a2%91%e6%ac%a1%2c%27INTEGER%27)+desc',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Origin': 'https://kns.cnki.net',
            # 'Cookie': 'Ecp_notFirstLogin=90SlXb; ASP.NET_SessionId=kvza4ikmafohrhmscwj4wdvf; Ecp_ClientId=6201105165501004934; SID_kns=025123115; SID_kinfo=125105; SID_klogin=125143; c_m_LinID=LinID=WEEvREcwSlJHSldSdmVqelcxVTI2bUdjNFRieVJMUHpmQXB2ZTNjN3VtVT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=11/05/2020 17:15:26; LID=WEEvREcwSlJHSldSdmVqelcxVTI2bUdjNFRieVJMUHpmQXB2ZTNjN3VtVT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; c_m_expire=2020-11-05 17:15:26; Ecp_session=1; Ecp_LoginStuts={"IsAutoLogin":false,"UserName":"K10054","ShowName":"%E5%8C%97%E4%BA%AC%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6","UserType":"bk","BUserName":"","BShowName":"","BUserType":"","r":"90SlXb"}; SID_kns_new=kns123109; KNS_SortType=',
        }
        self.headers_login = {
            'Host': 'login.cnki.net',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
            'Sec-Fetch-Mode': 'nested-navigate',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Sec-Fetch-Site': 'same-origin',
            'Referer': 'https://kns.cnki.net/kns/brief/brief.aspx?',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.headers_post = {
            'Host': 'kns.cnki.net',
            'Connection': 'keep-alive',
            'Content-Length': '797',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Origin': 'https://kns.cnki.net',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://kns.cnki.net/kns/brief/result.aspx',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

        self.headers_get_page = {
            'Host': 'kns.cnki.net',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'iframe',
            'Referer': 'https://kns.cnki.net/kns/brief/result.aspx',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

        self.headers_get_ajax = {
            'Host': 'kns.cnki.net',
            'Connection': 'keep-alive',
            'Accept': 'text/html, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }


        self.paramters = {
            'curpage':'1',###
            'RecordsPerPage':'20',
            'QueryID':'1',###
            'ID':'',
            'turnpage':'1',
            'tpagemode':'L',
            'dbPrefix':'CJFQ',###
            'Fields':'',
            'DisplayMode':'listmode',
            'SortType':'(发表时间,\'TIME\') desc',
            'PageName':'ASP.brief_result_aspx',
            'isinEn':'1',
        }

        self.static_post_data = {
            'action': '',
            'NaviCode': 'I135',#查找的类别（此处为互联网技术）
            'ua': '1.25',
            'isinEn': '1',
            'PageName': 'ASP.brief_result_aspx',
            'DbPrefix': 'CJFQ',##
            'DbCatalog': '中国学术期刊网络出版总库',
            'ConfigFile': 'CJFQ.xml',##
            'db_opt': 'CJFQ,CDFD,CMFD,CPFD,IPFD,CCND,CCJD',  # 搜索类别（CNKI右侧的）
            'db_value': '中国学术期刊网络出版总库',
            'year_type': 'echar',
            'CKB_extension':  'ZYW',
            'his': '0',
            'db_cjfqview': '中国学术期刊网络出版总库,WWJD',
            'db_cflqview': '中国学术期刊网络出版总库',
            '__': time.asctime(time.localtime()) + ' GMT+0800 (中国标准时间)'
        }

my_parameters = Parameters()