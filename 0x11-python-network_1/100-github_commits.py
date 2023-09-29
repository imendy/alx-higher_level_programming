#!/usr/bin/python3
"""
Module to access to the GitHub API and uses the information
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def main(argv):
    """
    Function that list 10 commits (from the most recent to oldest)
    of the repository.The first argument will be the repository name
    and the second argument will be the owner name
    """

    def the_printed_commits(a, the_commits):
        """
        List the commits, less than 10 commits
        """
        sha = the_commits[a].get('sha')
        commit = the_commits[a].get('commit')
        author = commit.get('author')
        name = author.get('name')
        print('{}: {}'.format(sha, name))

    repository_name = argv[1]
    owner_name = argv[2]
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get('https://api.github.com/repos/' + owner_name +
                            '/' + repository_name + '/commits', headers=headers)
    the_commits = response.json()
    size = len(the_commits)
    if size < 10:
        for a in range(0, size):
            the_printed_commits(a, the_commits)
    else:
        for a in range(0, 10):
            the_printed_commits(a, the_commits)


if __name__ == "__main__":
    main(argv)
