import os

import toml


credentials = toml.load("config/credentials.toml")
options = toml.load("config/options.toml")


def _get_bool(env_key, config_value):
    return os.getenv(env_key, str(config_value)).lower() == "true"


GITHUB_PAT = os.getenv("GITHUB_PAT", credentials["GITHUB"]["PAT"])
GITEA_PAT = os.getenv("GITEA_PAT", credentials["GITEA"]["PAT"])
GITEA_HOST = os.getenv("GITEA_HOST", credentials["GITEA"]["HOST"])
GITEA_USERNAME = os.getenv("GITEA_USERNAME", credentials["GITEA"]["USERNAME"])
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", credentials["GITHUB"]["USERNAME"])

CREATE_ORG = _get_bool("CREATE_ORG", options["CONFIG"]["CREATE_ORG"])
REMOVE_INEXIST_REPO = _get_bool("REMOVE_INEXIST_REPO", options["CONFIG"]["REMOVE_INEXIST_REPO"])
REMOVE_EXISTING_REPO = _get_bool("REMOVE_EXISTING_REPO", options["CONFIG"]["REMOVE_EXISTING_REPO"])
MIRROR_OWNED = _get_bool("MIRROR_OWNED", options["CONFIG"]["MIRROR_OWNED"])
MIRROR_PRIVATE = _get_bool("MIRROR_PRIVATE", options["CONFIG"]["MIRROR_PRIVATE"])
MIRROR_FORKED = _get_bool("MIRROR_FORKED", options["CONFIG"]["MIRROR_FORKED"])
MIRROR_STARRED = _get_bool("MIRROR_STARRED", options["CONFIG"]["MIRROR_STARRED"])
MIRROR_COLLABORATOR = _get_bool("MIRROR_COLLABORATOR", options["CONFIG"]["MIRROR_COLLABORATOR"])
MIRROR_ORGANIZATION = _get_bool("MIRROR_ORGANIZATION", options["CONFIG"]["MIRROR_ORGANIZATION"])

RULE_MODE = os.getenv("REPO_RULE", options["RULE"]["MODE"])
RULE_REGEX = os.getenv("REPO_NAME", ",".join(options["RULE"]["REGEX"])).split(",")
