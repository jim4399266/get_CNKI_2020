import requests
import sys
import time,os,logging
from static_parameters import my_parameters
from getPage import get_page_info
import re
import json
from Logging import log
import urllib3
urllib3.disable_warnings()

class_path = "39_1"



# # 获取cookie
# BASIC_URL = 'https://kns.cnki.net/kns/brief/result.aspx'
# 利用post请求先行注册一次
SEARCH_HANDLE_URL = 'https://kns.cnki.net/kns/request/SearchHandler.ashx'
# 发送get请求获得文献列表
GET_PAGE_URL = 'https://kns.cnki.net/kns/brief/brief.aspx?pagename='
# 切换页面基础链接
CHANGE_PAGE_URL = 'https://kns.cnki.net/kns/brief/brief.aspx'

LOGIN_URL = 'https://login.cnki.net/TopLogin/api/loginapi/IpLoginFlush?callback=jQuery111301373735351583667_1604572409572&_=1604572409573'

class SearchTool(object):
    def __init__(self, dir_path):
        self.dir_path = dir_path

        self.session = requests.Session()# 保持会话
        self.session.get(LOGIN_URL, headers=my_parameters.headers_login, verify=False) #获取cookies

        self.cur_page = 1
        self.all_info = []

        self.start_page = 1

        self.end_page = 300

    def get_max_page(self):  # 从文件夹中查找已下载的页面号
        max_page = 0
        for file in os.listdir(self.dir_path):
            cur_page = int(file.split('.')[0])
            if cur_page > max_page:
                max_page = cur_page
        return max_page + 1  # 从下一页开始

    def get_another_page(self):
        '''
        请求其他页面和请求第一个页面形式不同
        重新构造请求
        '''
        # time.sleep(config.crawl_stepWaitTime)
        # time.sleep(0.1)
        # 搜索页面中切换页码的url，将其提取出来
        change_page_pattern_compile = re.compile(
            r'.*?pagerTitleCell.*?<a href="(.*?)".*')
        change_page_url = re.search(change_page_pattern_compile,
                                         self.get_result.text).group(1)
        # 将url中的括号进行转义  (:%28    ):%29
        change_page_url = re.sub(r'\(', '%28', change_page_url)
        change_page_url = re.sub(r'\)', '%29', change_page_url)
        #将原url中的页码替换成下一个页码，由CHANGE_PAGE_URL、替换部分、self.change_page_url三个部分组成
        curpage_pattern_compile = re.compile(r'.*?curpage=(\d+).*?')
        self.get_result_url = CHANGE_PAGE_URL + re.sub(
            curpage_pattern_compile, '?curpage=' + str(self.cur_page),
            change_page_url)

        #get_res = self.session.get(self.get_result_url, headers=my_parameters.headers)
        #self.parse_page(download_page_left, get_res.text)

    def search_reference(self):
        #首先创建存放数据的文件夹
        if not os.path.exists(self.dir_path):
            os.mkdir(self.dir_path)
        '''
        第一次发送post请求
        再一次发送get请求,这次请求没有写文献等东西
        两次请求来获得文献列表
        '''

        my_parameters.static_post_data['NaviCode'] = 'I1' + class_path
        first_post_res = self.session.post(SEARCH_HANDLE_URL, data=my_parameters.static_post_data, headers=my_parameters.headers_post, verify=False)
        self.get_result_url = GET_PAGE_URL + first_post_res.text + '&t=1604567480096&keyValue=&S=1&sorttype='
        self.get_result = self.session.get(self.get_result_url, headers=my_parameters.headers_get_page, verify=False)

        #如果此文件未被保存过，则找到其内容保存下来
        cur_file = os.path.join(self.dir_path ,str(self.cur_page) + '.json')
        if not os.path.exists(cur_file):
            #将第一页的所需内容加入列表
            dict_per_page = get_page_info.get_Page_Info(self.get_result.text,self.session)
            with open(cur_file, 'w', encoding='utf8') as fp:
                json.dump(dict_per_page, fp)
            time.sleep(0.1)
            log('第' + str(self.cur_page) + '页下载完毕！')
            exit()

        self.start_page = self.get_max_page()
        print("初始页码",self.start_page)
        for self.cur_page in range(self.start_page,self.end_page+1):
            time.sleep(0.5)
            # 如果此文件未被保存过，则找到其内容保存下来
            cur_file = os.path.join(self.dir_path, str(self.cur_page) + '.json')
            if not os.path.exists(cur_file):
                self.get_another_page()
                self.get_result = self.session.get(self.get_result_url, headers=my_parameters.headers_kns)
                dict_per_page = get_page_info.get_Page_Info(self.get_result.text, self.session)
                with open(cur_file, 'w') as fp:
                    json.dump(dict_per_page, fp)
                time.sleep(0.1)
                log('第' + str(self.cur_page) +'页下载完毕！')
            exit()


def main():
    s = SearchTool('计算机网络理论')
    s.search_reference()
    # print(s.session.cookies)

if __name__ == '__main__':
    #根据运行的条件设置
    main()
    # class_path = str(sys.argv[1])
    # print("class_path:",class_path)
    # my_parameters.static_post_data["NaviCode"] = "I1"+str(class_path)
