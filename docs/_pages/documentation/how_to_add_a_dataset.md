---
title: How to add a data set
layout: single
permalink: /documentation/how_to_add_a_dataset/
---

TODO: Explain how to add a dataset

Step by Step guide to adding your dataset to the DLAB organization
--

#  1) Create repository in organization

1. Go to the **DLAB organization** page on GitHub.
2. Click the **"Repositories"** tab.
3. Click the green **"New"** button (top right).
4. Choose whether the repo will be **public** or **private**.
5. Give the repo a descriptive name and create it.

***

#  2) Metadata.json file follows schema 1 file template

1. Go to the datalake repository.
2. Locate the file `schema_1.0.json` — this is your metadata **template**.
3. In your own dataset repo:
   - Click the **"Add File"** dropdown near the green **"<> Code"** button.
   - Select **"Create new file"**.
   - Name it `metadata.json`.
4. Copy the contents of `schema_1.0.json` into your new `metadata.json`.
5. Replace the placeholder values with your dataset’s real information.
6. Click **"Commit new file"** to save it to the repo.

***

# 3) Steps to set up git sub modular repo

  1) Platform to run git commands
     - CMD
     - Git Bash
     - Github Desktop
     - VS Code
  3) GUIDE FOR:Open terminal or Powershell in VS Code
  4) Clone your main repo to your local devices
  5) Run these commands:
  6) git clone URL
  7) cd REPONAME
  8) Ex) git clone https://github.com/sadak2004/gitsubmodulerepo.git
  9) cd gitsubmodulerepo
  10) Now add the second repo as a submodule inside a folder.
  11) Run these commands:
  12) Git submodule add URLSUBREPO
  13) ex) git submodule add https://github.com/sadak2004/subrepo.git
  14) Commit and push the changes.
  15) Run these commands:
  16) git add .gitmodules REPONAME
  17) git commit -m "COMMIT MESSAGE"
  18) git push origin main
  19) For further help/information: visit this link https://gist.github.com/gitaarik/8735255

***

