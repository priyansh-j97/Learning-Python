from urllib import request

bitcoin_data_url="https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1592946686&period2=1624482686&interval=1mo&events=history&includeAdjustedClose=true"

def download_file(url):
    url_open=request.urlopen(url)
    url_read=url_open.read()
    str_data=str(url_read)
    data_lines=str_data.split("\\n")
    dest_address=r'bitcoin_data.csv'
    f = open("bitcoin_data.csv",'w')
    for i in data_lines:
        f.write(i+"\n")
    f.close()

download_file(bitcoin_data_url)