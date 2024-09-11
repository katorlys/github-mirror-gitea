import logging

import requests

import config


def fetch_request(raw_url, headers, name):
    repos = []
    per_page = 50

    response = requests.get(raw_url.format(per_page=per_page), headers=headers)
    if response.status_code != 200:
        logging.warning(
            f"Failed to fetch {name}: {response.status_code} {response.content}"
        )
        return repos

    repos = response.json()
    return repos


def fetch_github_repos():
    headers = {"Authorization": f"token {config.GITHUB_PAT}"}
    repos = []

    logging.info("\nFetching GitHub repositories...")
    if config.MIRROR_STARED:
        repos.extend(
            fetch_request(
                "https://api.github.com/user/starred?per_page={per_page}",
                headers, "GitHub repositories"
            )
        )

    affiliations = []
    if config.MIRROR_OWNED:
        affiliations.append("owner")
    if config.MIRROR_COLLABORATOR:
        affiliations.append("collaborator")
    if config.MIRROR_ORGANIZATION:
        affiliations.append("organization_member")

    if affiliations:
        affiliation_param = ",".join(affiliations)
        repos.extend(
            fetch_request(
                f"https://api.github.com/user/repos?per_page={{per_page}}&affiliation={affiliation_param}",
                headers, "GitHub repositories"
            )
        )

    logging.info(f"Total GitHub repositories fetched: {len(repos)}")
    return repos
