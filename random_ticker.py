import requests, random, time


markets = {'nyse_url':'https://pkgstore.datahub.io/core/nyse-other-listings/nyse-listed_json/data/e8ad01974d4110e790b227dc1541b193/nyse-listed_json.json',
           'nasdaq_url':'https://pkgstore.datahub.io/core/nasdaq-listings/nasdaq-listed-symbols_json/data/5c10087ff8d283899b99f1c126361fa7/nasdaq-listed-symbols_json.json'}

def create_tickers_db(markets):
    all_companies = {}
    tickers = []
    for market, url in markets.items():
        r = requests.get(url)
        #print('request')
        for el in r.json():
            if market == 'nyse_url':
                all_companies.update({el['ACT Symbol']: el['Company Name']})
                tickers.append(el['ACT Symbol'])
            elif market == 'nasdaq_url':
                all_companies.update({el['Symbol']: el['Company Name']})
                tickers.append(el['Symbol'])
    return all_companies, tickers

def random_company(db):
    num = random.randint(0, len(db[1])-1)
    ticker = db[1][num]
    company_name = db[0][db[1][num]]
    return ticker, company_name

tickers_db = create_tickers_db(markets)

n = 0
while n == 0:
    t, c = random_company(tickers_db)
    print(t)
    print(c)
    time.sleep(1)