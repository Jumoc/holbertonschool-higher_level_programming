#!/usr/bin/python3
"""hbtn status module"""
import requests
import sys


if __name__ == "__main__":
    repository = sys.argv[1]
    name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        name, repository
    )
    s = requests.Session()
    r = s.get(url)
    if (r.status_code < 400):
        # with open("commits.json", "r", encoding="utf8") as file:
        #     f_json = json.loads(file.read())

        i = 0
        for commit in r.json():
            if i > 9:
                break
            sha = commit.get('sha')
            name = commit.get('commit').get('author').get('name')
            print("{}: {}".format(sha, name))
            i += 1
