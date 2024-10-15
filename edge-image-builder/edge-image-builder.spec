#
# spec file for package edge-image-builder
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           edge-image-builder-110
Version:        1.1.0
Release:        0
Summary:        Edge Image Builder
License:        Apache-2.0
URL:            https://github.com/suse-edge/edge-image-builder
Source:         edge-image-builder-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) go1.22
BuildRequires:  golang-packaging
BuildRequires:  gpgme-devel
BuildRequires:  device-mapper-devel
BuildRequires:  libbtrfs-devel

Requires: xorriso
Requires: squashfs
Requires: libguestfs
Requires: kernel-default
Requires: e2fsprogs
Requires: parted
Requires: gptfdisk
Requires: btrfsprogs
Requires: guestfs-tools
Requires: lvm2
Requires: podman
Requires: createrepo_c
Requires: helm
Requires: hauler
Requires: nm-configurator
Requires: ca-certificates-suse

%description

Tool for creating and configuring a set of images to automate the deployment of Edge environments

%prep
%autosetup -a1 -n edge-image-builder-%{version}

%build
tar -xf %{SOURCE1}

MODULE=github.com/suse-edge/edge-image-builder

go build \
-mod=vendor \
-buildmode=pie \
-ldflags \
"-X $MODULE/pkg/version.version=v%{version}" \
-o eib ./cmd/eib

%install

install -D -m 0755 eib %{buildroot}%{_bindir}/eib

%files
%license LICENSE
%doc README.md
%{_bindir}/eib

%changelog

