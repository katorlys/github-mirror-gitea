import config


def headers():
    return {
        "Authorization": f"token {config.GITEA_PAT}",
        "Content-Type": "application/json",
    }
