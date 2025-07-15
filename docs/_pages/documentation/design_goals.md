---
title: Design Goals
layout: single
permalink: /documentation/design_goals/
---

## Target audience

Below are the actors we expect to interact with the data lake and the notable
features of each actor. We note that people at Ames National Laboratory often
wear multiple hats and may interact with the data lake in multiple roles.

- Experimentalists. 

  - Primarily interact with the data lake by contributing experimental data.
  - Most will have limited coding skills.
  - Unlikely to know Linux/terminal.
  - Can upload files via GitHub's Web API.

- Computational scientists. 

  - Will primarily contribute data.
  - May reuse data for subsequent studies.
  - Assumed to have some Linux/terminal experience.
  - Can upload files via terminal or Web API.   

- Data engineer.

  - Will be responsible for maintaining the organization.
  - Build actions for automating dashboards.
  - Fluent in GitHub actions.
  - Can develop in Python.
  - Can use Linux/terminal.

- Data analysts.

  - Will primarily consume data.
  - May be able to use GitHub actions.
  - Fluent in Python.
  - Can use Linux/terminal.

## Types of data 

- Experimentalists.

  - Research notes. 
  - Results may be in proprietary file formats.
  - Some results may be uploaded to more common data locations, e.g., protein
    data bank, materials genome project

- Computational scientists.

  - Molecular geometries.
  - Input/output files for computational science codes.
  - Usually text files, but may be compressed or binary to optimize space.

- Data engineer.
  
  - GitHub workflows and actions.
  - Documentation for the data lake.

# Other design parameters

- Accessible from off-site.
- Ability to scale to large data sets and complicated workflows.
- Will need different levels of access control, e.g., not everyone needs to be
  able to delete data.
- Support for data versioning.
- Free hosting is preferred (at least initially).
- Ability to assign credit/authorship to data subsets.

# Services the data lake should provide

- Dashboard to facilitate discovery of data sets.
- Ability for data set maintainers to provide metadata.
