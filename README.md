<a name="readme-top"></a>
<div align="center">

<!-- <a href="#">
  <img src="https://github.com/katorlys/.github/blob/main/assets/logo/logo.png" height="100">
</a><br> -->

<h1>
  github-mirror-gitea
</h1>

<p>
  Mirror your GitHub repositories to your Gitea server.
</p>

[![Pull Requests][github-pr-badge]][github-pr-link]
[![Issues][github-issue-badge]][github-issue-link]
[![License][github-license-badge]](LICENSE)

</div>


<!-- Main Body -->

## Introduction
A Python script to mirror all of your GitHub repositories to your Gitea server, with multiple options.

Repositories created are mirrors of the original repositories, and by default Gitea will automatically fetch them every 8 hours.

Using GitHub APIs and Gitea APIs -- especially the `migrate` function.

### Features
There are many options to choose from:
- Mirror, or not mirror repos:
  - you own
  - you forked
  - you starred
  - you have access to as a collaborator
  - you have access to as an organization member
- Whether to remove existing repos in Gitea
- Whether to create new organizations in Gitea if `{username}` in `{username}/{repo_name}` doesn't match your GitHub username

If the repository on GitHub is private, the mirror repository will also be private.

### Tech Stack
- Python3


## Getting Started
### Allow migration from GitHub
Add the following in your Gitea server's `gitea/conf/app.ini` file:
```ini
[migrations]
ALLOWED_DOMAINS = github.com, *.github.com
```

### Configure credentials and options
Configure [`credentials.toml`](config/credentials.toml):

|    Key     | Description                                                                                                               |
|:----------:|:--------------------------------------------------------------------------------------------------------------------------|
| **GITHUB** |                                                                                                                           |
|  USERNAME  | Your GitHub username                                                                                                      |
|    PAT     | Your GitHub personal access token, needed permissions:<br> - repo (Full control of private repositories)                  |
| **GITEA**  |                                                                                                                           |
|  USERNAME  | Your Gitea username                                                                                                       |
|    HOST    | Your Gitea hostname, starts with `http://` or `https://`                                                                  |
|    PAT     | Your Gitea personal access token, needed permissions:<br> - repository: Read and Write<br> - organization: Read and Write |

Configure [ `options.toml`](config/options.toml):

|         Key          | Description                                                                                                                                                |
|:--------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
|      **CONFIG**      |                                                                                                                                                            |
|      CREATE_ORG      | Create a new organization in Gitea when the repository username is different from your GitHub username.                                                    |
| REMOVE_EXISTING_REPO | Remove existing repositories in Gitea. You may not want to enable this option, since Gitea will automatically fetch the mirror repositories every 8 hours. |
|     MIRROR_OWNED     | Mirror the repositories you own.                                                                                                                           |
|    MIRROR_FORKED     | Mirror the repositories you forked.                                                                                                                        |
|    MIRROR_STARRED    | Mirror the repositories you starred.                                                                                                                       |
| MIRROR_COLLABORATOR  | Mirror the repositories that you have collaborator access. See: https://docs.github.com/zh/rest/repos/repos#list-repositories-for-the-authenticated-user   |
| MIRROR_ORGANIZATION  | Mirror the repositories in organizations that you are a member.                                                                                            |
|       **RULE**       |                                                                                                                                                            |
|         MODE         | `whitelist` or `blacklist` to only mirror or skip repositories that match the regex.                                                                       |
|        REGEX         | Regex list.                                                                                                                                                |


## Usage
Install the required packages:
```bash
pip install -r requirements.txt
```
Run the script:
```bash
python main.py
```

<!-- /Main Body -->


<div align="right">
  
[![BACK TO TOP][back-to-top-button]](#readme-top)

</div>

---

<div align="center">

<p>
  Copyright &copy; 2024-present <a target="_blank" href="https://github.com/katorlys">Katorly Lab</a>
</p>

[![License][github-license-badge-bottom]](LICENSE)

</div>

[back-to-top-button]: https://img.shields.io/badge/BACK_TO_TOP-151515?style=flat-square
[github-pr-badge]: https://img.shields.io/github/issues-pr/katorlys/github-mirror-gitea?label=pulls&labelColor=151515&color=79E096&style=flat-square
[github-pr-link]: https://github.com/katorlys/github-mirror-gitea/pulls
[github-issue-badge]: https://img.shields.io/github/issues/katorlys/github-mirror-gitea?labelColor=151515&color=FFC868&style=flat-square
[github-issue-link]: https://github.com/katorlys/github-mirror-gitea/issues
[github-license-badge]: https://img.shields.io/github/license/katorlys/github-mirror-gitea?labelColor=151515&color=EFEFEF&style=flat-square
<!-- https://img.shields.io/badge/license-CC_BY--NC--SA_4.0-EFEFEF?labelColor=151515&style=flat-square -->
[github-license-badge-bottom]: https://img.shields.io/github/license/katorlys/github-mirror-gitea?labelColor=151515&color=EFEFEF&style=for-the-badge
<!-- https://img.shields.io/badge/license-CC_BY--NC--SA_4.0-EFEFEF?labelColor=151515&style=for-the-badge -->