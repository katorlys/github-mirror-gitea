import config


HOST = f"{config.GITEA_HOST}/api/v1"

HEADERS = {"Authorization": f"token {config.GITEA_PAT}"}

HEADERS_JSON = {
    "Authorization": f"token {config.GITEA_PAT}",
    "Content-Type": "application/json",
}


def headers():
    return HEADERS


def headers_json():
    return HEADERS_JSON
