#!/usr/bin/python3
"""this script print commits for sha commit and author """


from requests import *
import sys


if __name__ == "__main__":

    user = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, owner)
    res = get(url)
    res_json = res.json()
    try:
        for i in res_json[:10]:
            sha = i.get('sha')
            commit = i.get('commit')

            if commit:
                author = commit.get('author')
            if author:
                name = author.get('name')

            print('{}: {}'.format(sha, name))
    except ValueError:
        pass
