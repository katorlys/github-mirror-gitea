import re

import config


def skip_repo(repo_name):
    matched = any(re.match(pattern, repo_name) for pattern in config.RULE_REGEX)
    if config.RULE_MODE == "blacklist":
        return matched
    return not matched  # whitelist
