import config


HOST = f"{config.GITEA_HOST}/api/v1"


def headers():
    return {"Authorization": f"token {config.GITEA_PAT}"}


def headers_json():
    return {
        "Authorization": f"token {config.GITEA_PAT}",
        "Content-Type": "application/json",
    }
