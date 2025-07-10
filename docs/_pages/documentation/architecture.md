---
title: Architecture
layout: single
permalink: /documentation/architecture/
---

![DLAB architecture](/_pages/documentation/assets/architecture.png)

The initial version of the data lake makes heavy use of GitHub. More
specifically we have created the DLAB organization to house repos related to
the data lake. The data lake is ultimately the union of many data sets. Each
individual data set is a git repository. The data set repos are then added to
the `Data Lake` repo as git submodules. Data analysts wanting to use the data
lake do so through the `Data Lake` repo. To facilitate discovery of data sets,
the DLAB organization maintains a pipeline which will analyze the data in
`Data Lake` and upload the results to a dashboard. The dashboard is part of
DLAB's website (maintained through the `dlab.github.io` repo).

## Why GitHub?

Based on [design goals](/documentation/design_goals) we know that the data lake
will need to be accessible via the internet, we also know that it will need to
have a web-based API for users that are not familiar with terminal commands.
GitHub satisfies both of these considerations (though we likely will need a
significant amount of tutorials for people unfamiliar with version control).
The use of git to version control the data lake provides primitive versioning
via commit hashes (and proper versioning via git tags). 

## Will GitHub scale?

GitHub's free plan allows for:

- Unlimited public repositories
- Unlimited CI/CD minutes for public repositories. 
- Repository sizes up to 5 GB.
- Max file size of 100 MB in repo and 2 GB as a release.

## Will git submodules scale?

- Can nest submodules, e.g. could have `Data Lake` be a submodule of another
  repo, say `Data Ocean`.
- Git does not require you to initialize all submodules (I think this is the 
  case at least)