#!/usr/bin/python3
"""API usage"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit,
    or 0 if an invalid subreddit is given.
    """
