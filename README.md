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
A Python script to mirror your GitHub repositories to your Gitea server, with multiple options.


## Usage
### Step 1
Add the following in your Gitea server's `gitea/conf/app.ini` file:
```ini
[migrations]
ALLOWED_DOMAINS = github.com, *.github.com
```

### Step 2
Open`credentials.toml`, and fill out all the fields.

Open `options.toml`, and adjust the options as needed.

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