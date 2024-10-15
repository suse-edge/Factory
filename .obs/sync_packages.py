import argparse
import subprocess
import pathlib
from typing import Set
import add_package
import delete_package

from common import PROJECT

def get_obs_packages() -> Set[str]:
    packages = subprocess.run(["osc", "ls", PROJECT], encoding='utf-8' , capture_output=True)
    return set(packages.stdout.splitlines())

def get_local_packages() -> Set[str]:
    p = pathlib.Path('.')
    return {x.name for x in p.iterdir() if x.is_dir() if not x.name.startswith('.')}

def main():
    parser = argparse.ArgumentParser(prog="sync_packages")
    parser.add_argument('--dry-run', action="store_true")

    args = parser.parse_args()

    local_packages = get_local_packages()
    obs_packages = get_obs_packages()

    packages_to_add = local_packages - obs_packages
    packages_to_delete = obs_packages - local_packages

    for p in packages_to_add:
        print(f"Adding {p}")
        if not args.dry_run:
            add_package.add_package(p)
    
    for p in packages_to_delete:
        print(f"Removing {p}")
        if not args.dry_run:
            delete_package.delete_package(p)

    print("Package synced in OBS, you can now push the modified workflow file")


if __name__ == '__main__':
    main()
