#
# spec file for package cluster-api-operator
#
# Copyright (c) 2023 SUSE LLC
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


Name:           cluster-api-operator
Version:        0.12.0
Release:        0
Summary:        Cluster API Core Controller
License:        Apache-2.0
URL:            https://github.com/kubernetes-sigs/cluster-api-operator
Source:         cluster-api-operator-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) = 1.21
ExcludeArch:    s390
ExcludeArch:    %{ix86}

%description

Cluster API operator

%prep
%autosetup -a1 -n cluster-api-operator-%{version}

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -o cluster-api-operator cmd/main.go

%install
install -D -m0755 cluster-api-operator %{buildroot}%{_bindir}/cluster-api-operator-controller

%files
%license LICENSE
%doc README.md
%{_bindir}/cluster-api-operator-controller

%changelog
