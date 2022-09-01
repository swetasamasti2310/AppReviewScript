from google_play_scraper import Sort, reviews
result, continuation_token = reviews(
    'com.fiberlink.maas360.android.control',
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.NEWEST
    count=3, # defaults to 100
    filter_score_with=5 # defaults to None(means all score)
)

print('result is:')
print(result)