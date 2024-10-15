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


Name:           frr-k8s
Version:        0.0.14
Release:        0.0.14
Summary:        A kubernetes based daemonset that exposes a subset of the FRR API in a kubernetes compliant manner.
License:        Apache-2.0
URL:            https://github.com/metallb/frr-k8s
Source:         frr-k8s-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) = 1.22
ExcludeArch:    s390
ExcludeArch:    %{ix86}

%description
A kubernetes based daemonset that exposes a subset of the FRR API in a kubernetes compliant manner.

The rationale behind the creation of this project is to allow multiple actors to share a single FRR instance running on kubernetes nodes.

%prep
%autosetup -a1 -n frr-k8s-%{version}

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -a \
   -o frr-metrics \
   frr-tools/metrics/exporter.go
   
go build \
   -mod=vendor \
   -buildmode=pie \
   -a \
   -o frr-k8s \
   cmd/main.go

%install
install -D -m0755 frr-tools/reloader/frr-reloader.sh %{buildroot}/frr-reloader.sh
install -D -m0755 frr-metrics %{buildroot}/frr-metrics
install -D -m0755 frr-k8s %{buildroot}/frr-k8s

%files
%license LICENSE
%doc README.md
/frr-reloader.sh
/frr-metrics
/frr-k8s

%changelog