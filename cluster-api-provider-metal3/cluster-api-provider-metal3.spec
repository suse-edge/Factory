#
# spec file for package cluster-api-provider-metal3
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


Name:           cluster-api-provider-metal3
Version:        1.7.1
Release:        0
Summary:        Cluster API Infrastructure Provider for Metal3
License:        Apache-2.0
URL:            https://github.com/metal3-io/cluster-api-provider-metal3
Source:         cluster-api-provider-metal3-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) = 1.21
ExcludeArch:    s390
ExcludeArch:    %{ix86}

%description

Cluster API Provider Metal3 is one of the providers for Cluster API and enables
users to deploy a Cluster API based cluster on top of bare metal infrastructure
using Metal3.

%prep
%autosetup -a1 -n cluster-api-provider-metal3-%{version}

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -a -ldflags '-extldflags "-static"'

%install
install -D -m0755 cluster-api-provider-metal3 %{buildroot}%{_bindir}/cluster-api-provider-metal3

%files
%license LICENSE
%doc README.md
%{_bindir}/cluster-api-provider-metal3

%changelog
