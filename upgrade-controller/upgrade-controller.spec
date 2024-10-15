#
# spec file for package upgrade-controller
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


Name:           upgrade-controller
Version:        0.1.0
Release:        0
Summary:        Upgrade Controller
License:        Apache-2.0 
URL:            https://github.com/suse-edge/upgrade-controller
Source:         upgrade-controller-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) go1.22
BuildRequires:  golang-packaging

%description

Кubernetes operator handling the lifecycle of the SUSE Edge platform

%prep
%autosetup -a1 -n upgrade-controller-%{version}

%build
go build -mod=vendor -buildmode=pie -o upgrade-controller ./cmd

%install
install -D -m 0755 upgrade-controller %{buildroot}%{_bindir}/upgrade-controller

%files
%license LICENSE
%doc README.md
%{_bindir}/upgrade-controller

%changelog


