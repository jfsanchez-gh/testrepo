import urllib2, sys, re

def download(url, retries=2):
	user_agent = 'wswp'
	headers = {'User-agent' : user_agent}
	request = urllib2.Request(url, headers=headers)
	print 'Downloading:', url
	try:
		html = urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		print 'Download error:', e.reason
		html = None
		if retries>0 and hasattr(e, 'code') and 500 <= e.code < 600:
			return download(url, retries-1)

	return html



def crawl_sitemap(url):
	sitemap = download(url)
	links = re.findall('<loc>(.*?)</loc>', sitemap)
	print 'Founded %d links' %len(links)
	for link in links:
		print link


if __name__ == '__main__':
	url = sys.argv[1]
	print crawl_sitemap(url)