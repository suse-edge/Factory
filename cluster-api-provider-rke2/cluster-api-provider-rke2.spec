#
# spec file for package cluster-api-provider-rke2
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


Name:           cluster-api-provider-rke2
Version:        0.7.0
Release:        0
Summary:        Cluster API provider for RKE2
License:        Apache-2.0
URL:            https://github.com/rancher-sandbox/cluster-api-provider-rke2
Source:         cluster-api-provider-rke2-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) = 1.21
ExcludeArch:    s390
ExcludeArch:    %{ix86}

%description

Cluster API provider for RKE2

%package bootstrap
Summary: Cluster API bootstrap controller for RKE2
%description bootstrap
Cluster API bootstrap controller for RKE2

%package control-plane
Summary: Cluster API control-plane controller for RKE2
%description control-plane
Cluster API control-plane controller for RKE2

%prep
%autosetup -a1 -n cluster-api-provider-rke2-%{version}

%build
make managers

%install
install -D -m0755 bin/rke2-bootstrap-manager %{buildroot}%{_bindir}/rke2-bootstrap-manager
install -D -m0755 bin/rke2-control-plane-manager %{buildroot}%{_bindir}/rke2-control-plane-manager

%files bootstrap
%{_bindir}/rke2-bootstrap-manager

%files control-plane
%{_bindir}/rke2-control-plane-manager

%changelog
