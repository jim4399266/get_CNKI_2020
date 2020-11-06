from bs4 import BeautifulSoup
from Logging import log
import math,random,time
import re,os
import requests
from static_parameters import my_parameters
import json

#设立缓存，如果已经有期刊信息，则直接将影响因子复制即可
# try:
#     with open('Journal_Point.json','r') as f:
#         Journal_Point = json.load(f)
# except:
#     Journal_Point = {}

GET_ARTICAL_DETAIL_URL = 'https://kns.cnki.net/KCMS/detail/detail.aspx?'


class GetPageInfo(object):
    def __init__(self):
        self.count = 0  #用于递归计数
        self.session = None


    def find_ajax(self,url,article_url, parameters):
        time.sleep(0.1)
        #根据url和参数获取相应页面的信息
        info = {
            '题名':'',
            '作者':'',
            '发表时间': '',
        }
        # print(parameters)
        my_parameters.headers_get_ajax['Referer'] = article_url + '&v=MDY0MzdvUjhlWDFMdXhZUzdEaDFUM3FUcldNMUZyQ1VSN3FlWnVacUZDbmdVTHpCSmpYU2Q3RzRITkhQckk5Q1o='
        ajax_list_page = self.session.get(url, params=parameters, headers=my_parameters.headers_get_ajax, verify=False)
        print(ajax_list_page.url)
        print(ajax_list_page.text)
        # exit()
        try:
            ajax_list_page = requests.get(url, params=parameters, headers=my_parameters.headers_kns)
            print(ajax_list_page.text)
            soup = BeautifulSoup(ajax_list_page.text, 'lxml')
            ajax_list = soup.find('div', attrs={'class': 'ebBd'}).find_all('li')
            for item in ajax_list:
                href = 'https://kns.cnki.net' + item.find('a')['href']
                text = item.text.strip(' \n\r')
                text = re.sub(r'(&nbsp&nbsp)','', text)
                text = re.sub(r'[\n\r\s]+', '', text)
                info.append(text)
                info.append(href)
        except:
            pass
        return info


    def get_artical_detail(self,article_href,dict_article):
        time.sleep(0.1)
        #获取文章详细内容的url，发现和href中的三个关键参数有关
        parameters = {
            'DbCode':'',
            'DbName':'',
            'FileName':'',
        }
        pattern_DbCode = re.compile(r'.*?[dD]b[cC]ode=\s?(.*?)&')
        pattern_DbName = re.compile(r'.*?[dD]b[nN]ame=\s?(.*?)&')
        pattern_FileName = re.compile(r'.*?[fF]ile[nN]ame=\s?(.*?)&')
        parameters['DbCode'] = re.search(pattern_DbCode,article_href).group(1)
        parameters['DbName'] = re.search(pattern_DbName,article_href).group(1)
        parameters['FileName'] = re.search(pattern_FileName,article_href).group(1)
        print('FileName=' + parameters['FileName'])

        req = self.session.get(GET_ARTICAL_DETAIL_URL,params=parameters, headers=my_parameters.headers_kns, verify=False)
        article_url = req.url
        # print(article_url)
        #请求到文章详细内容的页面后，获取文章关键词
        soup = BeautifulSoup(req.text, 'lxml')
        # 查找摘要
        try:
            summary = soup.find('span', attrs={'id': 'ChDivSummary'}).text
        except:
            summary = ''
        dict_article['摘要'] = summary

        keyword = []
        try:
            keyword_list = soup.find('p', attrs={'class': 'keywords'}).find_all('a')
            for item in keyword_list:
                keyword.append(item.text.strip(';\r\n\t '))
        except:
            pass
        #将获取的关键词保存为列表，插入到每个文章的信息中
        dict_article['关键词'] = keyword

        #查找相似文献
        # parameters.update({
        #     'curdbcode': 'CJFQ',
        #     'reftype': '604',
        #     'vl': 'ZbIPwwnMJoSm2swYcmDVgmmd2FSAAyADbiRV9mmd2BWkE5fO94xVk5dXrDXdexcCCXmmd2BTZqBh',
        #     # 'vl': 'ZbIPwwnMJoSm2swYcmDVg%mmd2FSAAyADbiRV9%mmd2BWkE5fO94xVk5dXrDXdexcCCX%mmd2BTZqBh',
        #     # 'catalogId': 'lcatalog_func604',
        #     # 'catalogName': '相似文献',
        # })
        # ajax_url = 'https://kns.cnki.net/kcms/detail/frame/asynlist.aspx?'
        # dict_article['相似文献'] = self.find_ajax(ajax_url, article_url, parameters)

        # print(dict_article)




    def get_Page_Info(self,text,session):
        time.sleep(0.2)
        self.session =session
        '''
        从每个文章列表中提取出文章的相关信息
        '''
        soup = BeautifulSoup(text,'lxml')
        #将每个文章列表中的信息装在一个列表中
        dict_per_page = []
        article_list = soup.find('table', attrs={'class': 'GridTableContent'}).find_all('tr')
        for i in range (1, len(article_list)):#artical_list[0]是表头
            print('正在获取第' + str(i) + '条信息，',end='')
            dict_article = {'题名': '',
                             '作者':'',
                             '刊名': '',
                             '发表时间': '',
                             '被引量': '',
                             '下载量': '',
                            }
            # 获取题名
            dict_article['题名'] = article_list[i].find('a', attrs={'class': 'fz14'}).text
            article_href = article_list[i].find('a', attrs={'class': 'fz14'})['href']

            # 获取作者
            tmp = article_list[i].find('td', attrs={'class': 'author_flag'}).text.strip('\r\n ')#用strip函数去除字符串首尾的非法字符
            dict_article['作者'] = [name.strip() for name in tmp.split(';') if name]
            # 获取来源
            dict_article['刊名'] = article_list[i].find('td', attrs={'class': 'cjfdyxyz'}).find('a').text
            # 获取发表时间
            dict_article['发表时间'] = article_list[i].find('td', attrs={'align': 'center'}).text.strip('\r\n ')
            # 获取被引量
            try:
                dict_article['被引量'] = article_list[i].find('td', attrs={'align': 'right'}).text.strip('\n ')
            except:
                dict_article['被引量'] = '0'
            # 获取下载量
            try:
                dict_article['下载量'] = article_list[i].find('span', attrs={'class': 'downloadCount'}).text
            except:
                dict_article['下载量'] = '0'
            self.get_artical_detail(article_href, dict_article)
            dict_per_page.append(dict_article)

        #返回每一页信息的列表
        return dict_per_page




get_page_info = GetPageInfo()
if __name__ == '__main__':
    pass