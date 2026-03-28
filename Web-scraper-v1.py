from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key="ICANTSHARE")
what_you_want = input("What topic do you want??: ")
what_source = input("What source do you want??: ")
biggest_headlines = newsapi.get_everything(q = f'{what_you_want}', sources = f"{what_source}")
articles = biggest_headlines["articles"]
for x in articles:
    print(f"According to {x["source"]["name"]} {x["description"]}")


