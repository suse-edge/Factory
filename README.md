# Factory

Contains the definition of the packages built on OBS for the SUSE Edge Solution (WIP)

This repository is linked to an OBS project: <https://build.opensuse.org/project/show/isv:SUSE:Edge:Factory>
Every directory in this repository represents a package in that OBS project, those should be synced automatically from this repository.

## Adding a package

To add a package, first create a directory with your package as you intend it in OBS.

Then run the `.obs/add_package.py` script to create the package in the OBS project and add the required elements to the synchronization workflow.
This script is using the `osc` command behind the scenes, so ensure you have it installed and correctly configured, as well as you have the correct permissions to create a new package in the project.

You will then get asked to push your changes.
