import json
import logging

import requests

import cache


def check_gitea_org_exists(org_name):
    response = requests.get(
        f"{cache.HOST}/orgs/{org_name}", headers=cache.headers_json()
    )
    return response.status_code == 200


def create_gitea_org(org_name):
    data = {
        "username": org_name,
        "full_name": org_name,
        "description": f"{org_name} on GitHub",
        "visibility": "public",
    }
    response = requests.post(
        f"{cache.HOST}/orgs", headers=cache.headers_json(), data=json.dumps(data)
    )

    if response.status_code == 201:
        logging.info(f"Organization created: {org_name}")
    else:
        logging.warning(
            f"Organization creation failed: {org_name}: {response.status_code} {response.content}"
        )
