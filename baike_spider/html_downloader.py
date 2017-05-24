from urllib.request import urlopen
class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None
        response=urlopen(url)
        #print(response.read().decode('utf-8'))
        if response.getcode() != 200:
                return None
        return response.read().decode('utf-8')
