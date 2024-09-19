import json
import logging
import time

import requests

import cache
import config
from utils.giteaRepo import check_gitea_repo_exists, remove_gitea_repo
from utils.giteaOrg import check_gitea_org_exists, create_gitea_org
from utils.repoRules import skip_repo


def mirror_to_gitea(repo):
    repo_name = f"{repo['owner']['login']}/{repo['name']}"
    logging.info(f"Mirroring repository: {repo_name}")
    if skip_repo(repo_name):
        logging.info(f"\tSkip (regex): {repo_name}")
        return

    if not config.MIRROR_PRIVATE and repo.get("private"):
        logging.info(f"\tSkip (private): {repo_name}")
        return

    if not config.MIRROR_FORKED and repo.get("fork"):
        logging.info(f"\tSkip (fork): {repo_name}")
        return

    repo_owner = config.GITEA_USERNAME
    target_repo_name = repo_name
    if config.CREATE_ORG and repo["owner"]["login"] != config.GITEA_USERNAME:
        repo_owner = repo["owner"]["login"]
        target_repo_name = f"{repo_owner}/{repo['name']}"
        if not check_gitea_org_exists(repo_owner):
            create_gitea_org(repo_owner)

    if check_gitea_repo_exists(target_repo_name):
        if config.REMOVE_EXISTING_REPO:
            logging.info(f"\tRemove (exists): {target_repo_name}")
            remove_gitea_repo(repo_name)
        else:
            logging.info(f"\tSkip (exists): {target_repo_name}")
            return

    description = (
        repo["description"] if repo["description"] else "No description provided."
    )
    clone_addr = repo["clone_url"].replace("https://", f"https://{config.GITHUB_PAT}@")
    data = {
        "clone_addr": clone_addr,
        "repo_owner": repo_owner,
        "repo_name": repo["name"],
        "description": description,
        "mirror": True,
        "private": repo["private"],
    }

    for attempt in range(3):  # Retry if failed
        response = requests.post(f"{cache.HOST}/repos/migrate", headers=cache.headers_json(), data=json.dumps(data))
        if response.status_code == 201:
            logging.info(f"\tSuccess: {target_repo_name}")
            break
        else:
            logging.warning(
                f"\tFailed: {target_repo_name}: {response.status_code} {response.content}"
            )
            if attempt < 2:
                logging.info(f"\tRetrying: {target_repo_name}")
                time.sleep(5)
