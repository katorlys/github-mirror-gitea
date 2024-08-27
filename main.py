import logging

from utils.githubRepo import fetch_github_repos
from utils.mirror import mirror_to_gitea


def main():
    logging.basicConfig(level=logging.INFO)
    repos = fetch_github_repos()
    for repo in repos:
        mirror_to_gitea(repo)


if __name__ == '__main__':
    main()
