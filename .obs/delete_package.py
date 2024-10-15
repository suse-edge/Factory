#!/usr/bin/env python3
import yaml
import subprocess
import argparse
import os
import os.path

from common import PROJECT


def delete_package_from_workflow(name: str):
    with open(".obs/workflows.yml", "r") as wf_file:
        workflows = yaml.safe_load(wf_file)
    workflows["staging_build"]["steps"] = [
        x
        for x in workflows["staging_build"]["steps"]
        if x["branch_package"]["source_package"] != name
    ]
    workflows["refresh_factory"]["steps"] = [
        x
        for x in workflows["refresh_factory"]["steps"]
        if x["trigger_services"]["package"] != name
    ]
    with open(".obs/workflows.yml", "w") as wf_file:
        yaml.dump(workflows, wf_file)


def delete_package_from_project(name: str):
    p = subprocess.run(["osc", "rdelete", PROJECT, name], stdout=subprocess.PIPE)
    print(p.stdout)
    print(p.stderr)
    p.check_returncode()


def delete_package(package_name: str):
    if "/" in package_name:
        print("invalid package name")
        os.exit(1)

    delete_package_from_project(package_name)
    delete_package_from_workflow(package_name)


def main():
    parser = argparse.ArgumentParser(prog="delete_package")
    parser.add_argument("package")

    args = parser.parse_args()

    delete_package(args.package)

    print("Package deleted in OBS, you can now push the modified workflow file")


if __name__ == '__main__':
    main()
