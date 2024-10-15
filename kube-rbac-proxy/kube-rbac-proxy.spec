#
# spec file for package kube-rbac-proxy
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


Name:           kube-rbac-proxy
Version:        0.18.0
Release:        0.18.0
Summary:        The kube-rbac-proxy is a small HTTP proxy for a single upstream
License:        Apache-2.0
URL:            https://github.com/brancz/kube-rbac-proxy
Source:         kube-rbac-proxy-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) = 1.22
ExcludeArch:    s390
ExcludeArch:    %{ix86}

%description
The kube-rbac-proxy is a small HTTP proxy for a single upstream, 
that can perform RBAC authorization against the Kubernetes API using SubjectAccessReview.

%prep
%autosetup -a1 -n kube-rbac-proxy-%{version}

%build
CGO_ENABLED=0\ 
  go build \
    --installsuffix cgo \
    -mod=vendor \
    -buildmode=pie \
    -a \
    -o $HOME/go/bin/kube-rbac-proxy \
    github.com/brancz/kube-rbac-proxy/cmd/kube-rbac-proxy

%install
install -D -m 0755 $HOME/go/bin/kube-rbac-proxy %{buildroot}/

%files
%license LICENSE
%doc README.md
/kube-rbac-proxy

%changelog
