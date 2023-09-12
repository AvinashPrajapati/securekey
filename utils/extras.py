####### get update date
def get_updated_date(item):
    updated_date_str = item['updated'].split('|')[-1].strip()
    return updated_date_str
def get_url(item):
    return item['url']