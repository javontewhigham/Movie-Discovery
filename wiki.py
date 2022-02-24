import requests

WIKI_BASE_URL = "https://en.wikipedia.org/w//api.php"


def get_wiki_data(title_params):
    wiki_query_params = {
        "action": "query",
        "format": "json",
        "titles": title_params,
        "prop": "info",
        "inprop": "url",
    }

    wiki_response = requests.get(WIKI_BASE_URL, params=wiki_query_params)

    response_link = wiki_response.json()["query"]["pages"].values()
    key = "fullurl"
    values_of_key = [a_dict[key] for a_dict in response_link]
    wiki_link = values_of_key[0]

    return wiki_link
