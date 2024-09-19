import os

import toml


credentials = toml.load("config/credentials.toml")
options = toml.load("config/options.toml")

GITHUB_PAT = os.getenv("GITHUB_PAT", credentials["GITHUB"]["PAT"])
GITEA_PAT = os.getenv("GITEA_PAT", credentials["GITEA"]["PAT"])
GITEA_HOST = os.getenv("GITEA_HOST", credentials["GITEA"]["HOST"])
GITEA_USERNAME = os.getenv("GITEA_USERNAME", credentials["GITEA"]["USERNAME"])
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", credentials["GITHUB"]["USERNAME"])

CREATE_ORG = (
    os.getenv("CREATE_ORG", str(options["CONFIG"]["CREATE_ORG"])).lower() == "true"
)
REMOVE_INEXIST_REPO = (
    os.getenv(
        "REMOVE_INEXIST_REPO", str(options["CONFIG"]["REMOVE_INEXIST_REPO"])
    ).lower()
    == "true"
)
REMOVE_EXISTING_REPO = (
    os.getenv(
        "REMOVE_EXISTING_REPO", str(options["CONFIG"]["REMOVE_EXISTING_REPO"])
    ).lower()
    == "true"
)
MIRROR_OWNED = (
    os.getenv("MIRROR_OWNED", str(options["CONFIG"]["MIRROR_OWNED"])).lower() == "true"
)
MIRROR_PRIVATE = (
    os.getenv("MIRROR_PRIVATE", str(options["CONFIG"]["MIRROR_PRIVATE"])).lower()
    == "true"
)
MIRROR_FORKED = (
    os.getenv("MIRROR_FORKED", str(options["CONFIG"]["MIRROR_FORKED"])).lower()
    == "true"
)
MIRROR_STARRED = (
    os.getenv("MIRROR_STARRED", str(options["CONFIG"]["MIRROR_STARRED"])).lower()
    == "true"
)
MIRROR_COLLABORATOR = (
    os.getenv(
        "MIRROR_COLLABORATOR", str(options["CONFIG"]["MIRROR_COLLABORATOR"])
    ).lower()
    == "true"
)
MIRROR_ORGANIZATION = (
    os.getenv(
        "MIRROR_ORGANIZATION", str(options["CONFIG"]["MIRROR_ORGANIZATION"])
    ).lower()
    == "true"
)
RULE_MODE = os.getenv("REPO_RULE", options["RULE"]["MODE"])
RULE_REGEX = os.getenv("REPO_NAME", ",".join(options["RULE"]["REGEX"])).split(",")
