from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key="bfb8aed228c54fd99333d7dc74a436ea")
what_you_want = input("What topic do you want??: ")
what_source = input("What source do you want??: ")
biggest_headlines = newsapi.get_everything(q = f'{what_you_want}', sources = f"{what_source}")
articles = biggest_headlines["articles"]
count = 0
OIlprice = 0
for x in articles:
    print(f"According to {x["source"]["name"]} {x["description"]}")
    count += 1
    if what_you_want == "Oil":
        for x in articles:
            if "risk" or "Risk" in x["description"]:
                OIlprice += 1
print(count)
print(f"The Oil price risk is currently {OIlprice/count}")