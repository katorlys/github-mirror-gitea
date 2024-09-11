import logging

import config
from utils.giteaRepo import fetch_gitea_repos, remove_inexist_repo
from utils.githubRepo import fetch_github_repos
from utils.mirror import mirror_to_gitea


def main():
    logging.basicConfig(level=logging.INFO)
    github_repos = fetch_github_repos()

    if config.REMOVE_INEXIST_REPO:
        gitea_repos = fetch_gitea_repos()
        remove_inexist_repo(github_repos, gitea_repos)

    for repo in github_repos:
        mirror_to_gitea(repo)


if __name__ == "__main__":
    main()
