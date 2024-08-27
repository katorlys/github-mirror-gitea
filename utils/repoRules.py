import re

import config


def skip_repo(repo_name):
    for pattern in config.RULE_REGEX:
        if re.match(pattern, repo_name):
            return config.RULE_MODE == "blacklist"  # else "whitelist" returns false
    return not config.RULE_MODE == "blacklist"      # else "whitelist" returns true
