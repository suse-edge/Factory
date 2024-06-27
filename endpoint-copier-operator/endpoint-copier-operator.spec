#
# spec file for package endpoint-copier-operator
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


Name:           endpoint-copier-operator-020
Version:        0.2.0
Release:        0.2.0
Summary:        Implements a Kubernetes API for copying endpoint resources
License:        Apache-2.0
URL:            https://github.com/suse-edge/endpoint-copier-operator
Source:         endpoint-copier-operator-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) = 1.20
ExcludeArch:    s390
ExcludeArch:    %{ix86}

%description
This is an Kubernetes operator whose purpose is to create a copy of the default Kubernetes Service (as LoadBalancer type) 
and Endpoint and to keep them synced.

%prep
%autosetup -a1 -n endpoint-copier-operator-%{version}

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -a \
   -o endpoint-copier-operator \
   cmd/main.go

%install
install -D -m0755 endpoint-copier-operator %{buildroot}/manager

%files
%license LICENSE
%doc README.md
/manager

%changelog