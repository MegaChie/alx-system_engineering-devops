#!/usr/bin/python
# -*- coding: utf-8 -*-

"""API usage"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit,
    or 0 if an invalid subreddit is given.
    """

    # firstly, authenticate and get token

    client = 'XVngJrvVrijzTzOU09512w'
    client_key = 'h6FGkpwlvaqLY1RjMkr-fn4Yu26SNQ'
    login = requests.auth.HTTPBasicAuth(client, client_key)
    header = {'User-Agent': 'Mega/0.0.2'}
    sent_data = {'grant_type': 'client_credentials'}
    with requests.post('https://www.reddit.com/api/v1/access_token',
                       auth=login, headers=header, data=sent_data) as \
        authMarko:
        poloKey = authMarko.json()
    header['Authorization'] = 'bearer {}'.format(poloKey['access_token'
            ])

    # using the token to access the API

    url = 'https://oauth.reddit.com/r/{}/about'.format(subreddit)
    with requests.get(url, headers=header) as marko:
        if marko.status_code >= 300:
            return 0
        polo = marko.json().get('data').get('subscribers')
    return polo
