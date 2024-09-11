import json
import logging

import requests

import cache
import config


def check_gitea_org_exists(org_name):
    url = f"{config.GITEA_HOST}/api/v1/orgs/{org_name}"
    response = requests.get(url, headers=cache.headers())
    return response.status_code == 200


def create_gitea_org(org_name):
    url = f"{config.GITEA_HOST}/api/v1/orgs"
    data = {
        "username": org_name,
        "full_name": org_name,
        "description": f"Organization for {org_name}",
        "visibility": "public",
    }
    response = requests.post(url, headers=cache.headers(), data=json.dumps(data))
    if response.status_code == 201:
        logging.info(f"Organization created: {org_name}")
    else:
        logging.warning(f"Organization creation failed: {org_name}: {response.status_code} {response.content}")
