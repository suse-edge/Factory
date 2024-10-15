#
# spec file for package cluster-api
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


Name:           cluster-api
Version:        1.7.5
Release:        0
Summary:        Cluster API Core Controller
License:        Apache-2.0
URL:            https://github.com/kubernetes-sigs/cluster-api
Source:         cluster-api-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) = 1.21
ExcludeArch:    s390
ExcludeArch:    %{ix86}

%description

Cluster API core controller

%prep
%autosetup -a1 -n cluster-api-%{version}

%build
go build \
   -mod=vendor \
   -buildmode=pie \

%install
install -D -m0755 cluster-api %{buildroot}%{_bindir}/cluster-api-controller

%files
%license LICENSE
%doc README.md
%{_bindir}/cluster-api-controller

%changelog
