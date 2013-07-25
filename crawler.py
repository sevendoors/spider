#!/usr/bin/python
#-*-coding:utf-8-*-

import httplib,re

#抓取页面


#return list
def getProductUrl():
		f = file('Listurl.txt')
		result = list()

		while True:
				line = f.readline()
				if len(line) == 0:
						break
#打印获取内容  可注释掉
				result.append(line)
		f.close
#转换链接
		urlList = list()
		productlist = list()
		for url in result:
				url = re.sub('\s*http.*?com/','',url)
				url = url.strip()
				urlList.append(url)
		for url in urlList:
				productlist.extend(getProductList(getPageContent(url)))
				counter = 2
				while True:
						product = getProductList(getPageContent(urlincrease(url,counter)))
						if len(product) == 0:
								break
						productlist.extend(product)
						counter = counter + 1
		return productlist
				
def getUrlList(productlist):
		reParttern = '/.*?\.html'
		pattern = re.compile(reParttern, re.DOTALL)
		urlList = list()
		for product in productlist:
				url = pattern.search(product)
				if url:
						uri = url.group()
						uri = uri[1:]
						#uri=re.sub(".html",'-page'+str(counter)+'.html',url)
						urlList.append(uri)
		return urlList




def urlincrease(url,counter):
		return re.sub(".html",'-page'+str(counter)+'.html',url)


def getProductList(content):
		rePattern = "<h2>.*?\</h2>"
		pattern = re.compile(rePattern,re.DOTALL)
		if pattern.findall(content):
				list = pattern.findall(content)
				return list
		else:
				return ''

		




		
def getCategoryList():
		ListUrl=getListUrl()
		content = list()
		for url in ListUrl:
				content.append(getPageContent(url))

		for article in content:
				print article
		return content


def getPageContent(PageUrl="index.html"):
		conn = httplib.HTTPConnection("www.outdoorled-screens.com")
		PageUrl = '/'+PageUrl.strip()
		conn.request("GET",PageUrl)
		r1 = conn.getresponse()
		print PageUrl, r1.status, r1.reason
		data = r1.read()
		return data
		conn.close()

def getProductInfo(content):
		img_repattern=""
		img_pattern = re.compile(rePattern,re.DOTALL)
		

#程序执行
productList=getUrlList(getProductUrl())
contentList = list()
for url in productList:
		contentList.append(getPageContent(url))




