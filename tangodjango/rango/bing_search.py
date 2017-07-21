import json
import urllib
import urllib.request, urllib.parse


def read_bing_key():
    bing_api_key = None

    try:
        with open('bing.key', 'r') as f:
            bing_api_key = f.readline()
    except:
        raise IOError('bing.key file not found.')

    return bing_api_key


def run_query(search_item):
    bing_api_key = read_bing_key()

    if not bing_api_key:
        raise KeyError("Bing Key not found")

    root_url = 'https://api.cognitive.microsoft.com/bing/v5.0'
    responseFilter = 'Webpages'
    count = 10
    offset = 0

    query = "'{}'".format(search_item)
    query = urllib.parse.quote(query)

    search_url = "{}{}?format=json$top={}&$top={}&$skip={}&$Query={}".format(
        root_url,
        responseFilter,
        count,
        offset,
        query
    )

    username = ''
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, search_url, username, bing_api_key)

    results = []

    try:
        handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
        opener = urllib.request.build_opener(handler)
        urllib.request.install_opener(opener)

        response = urllib.request.urlopen(search_url).read()
        response = response.decode('utf-8')

        json_response = json.loads(response)

        for result in json_response['d']['results']:
            results.append({
                'title': result['Title'],
                'link': result['Url'],
                'summary': result['Description']
            })
    except:
        print("Error when querying the BING API")

    return results
