import logging

import requests

import config


def headers():
    return {
        "Authorization": f"token {config.GITHUB_PAT}",
        "Content-Type": "application/json",
    }


def fetch_request(raw_url, headers, name):
    repos = []
    page = 1
    per_page = 200

    while True:
        response = requests.get(raw_url.format(per_page=per_page, page=page), headers=headers)
        if response.status_code != 200:
            logging.warning(
                f"Failed to fetch {name}: {response.status_code} {response.content}"
            )
            break

        page_repos = response.json()
        if not page_repos:
            break
        repos.extend(page_repos)
        page += 1

    return repos


def fetch_github_repos():
    repos = []

    logging.info("\nFetching GitHub repositories...")
    if config.MIRROR_STARRED:
        repos.extend(
            fetch_request(
                f"https://api.github.com/user/starred?page={{page}}&per_page={{per_page}}",
                headers(),
                "GitHub repositories",
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
                f"https://api.github.com/user/repos?page={{page}}&per_page={{per_page}}&affiliation={affiliation_param}",
                headers(),
                "GitHub repositories",
            )
        )

    logging.info(f"Total GitHub repositories fetched: {len(repos)}")
    return repos
