#!/usr/bin/env python3
import yaml
import subprocess
import argparse
import os
import os.path

from common import PROJECT, REPOSITORY, BRANCH

def add_package_to_workflow(name: str):
    modified = False
    with open(".obs/workflows.yml", "r") as wf_file:
        workflows = yaml.safe_load(wf_file)
    if not any(
        x
        for x in workflows["staging_build"]["steps"]
        if x["branch_package"]["source_package"] == name
    ):
        workflows["staging_build"]["steps"].append(
            {
                "branch_package": {
                    "source_project": PROJECT,
                    "target_project": f"{PROJECT}:Staging",
                    "source_package": name,
                }
            }
        )
        modified = True
    if not any(
        x
        for x in workflows["refresh_factory"]["steps"]
        if x["trigger_services"]["package"] == name
    ):
        workflows["refresh_factory"]["steps"].append(
            {
                "trigger_services": {
                    "project": PROJECT,
                    "package": name,
                }
            }
        )
        modified = True
    if modified:
        with open(".obs/workflows.yml", "w") as wf_file:
            yaml.dump(workflows, wf_file)


def add_package_to_project(name: str):
    package_meta = f"""<package name="{name}" project="{PROJECT}">
  <title/>
  <description/>
  <scmsync>{REPOSITORY}?subdir={name}#{BRANCH}</scmsync>
</package>"""
    p = subprocess.run(["osc", "meta", "pkg", "-F", "-", PROJECT, name], input=package_meta, encoding='utf-8' , stdout=subprocess.PIPE)
    print(p.stdout)
    print(p.stderr)
    p.check_returncode()


def main():
    parser = argparse.ArgumentParser(prog="add_package")
    parser.add_argument("package")

    args = parser.parse_args()

    package_name = args.package
    if "/" in package_name:
        print("invalid package name")
        os.exit(1)

    if not os.path.isdir(package_name):
        print("package doesn't exist in this directory")
        os.exit(1)

    add_package_to_project(package_name)
    add_package_to_workflow(package_name)

    print("Package created in OBS, you can now push the modified workflow file")


if __name__ == '__main__':
    main()
