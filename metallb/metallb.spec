#
# spec file for package metallb
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


Name:           metallb
Version:        0.14.8
Release:        0.14.8
Summary:        Load Balancer for bare metal Kubernetes clusters
License:        Apache-2.0
URL:            https://github.com/metallb/metallb
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) = 1.22
ExcludeArch:    s390
ExcludeArch:    %{ix86}

%define version_suffix 0148

%description
MetalLB is a load-balancer implementation for bare metal Kubernetes clusters, using standard routing protocols.

%package controller-%{version_suffix}
Summary:        MetalLB controller binary
Group:          System/Management

%description controller-%{version_suffix}
MetalLB is a load-balancer implementation for bare metal Kubernetes clusters, using standard routing protocols.
This package contains the controller binary.

%package speaker-%{version_suffix}
Summary:        MetalLB speaker binary
Group:          System/Management

%description speaker-%{version_suffix}
MetalLB is a load-balancer implementation for bare metal Kubernetes clusters, using standard routing protocols.
This package contains the speaker binary.

%prep
%autosetup -p1 -a1

# Add frr-tools/reloader
cp ./frr-tools/reloader/frr-reloader.sh frr-reloader.sh

%build
go install -v -mod vendor -buildmode=pie ./controller ./speaker ./frr-tools/metrics
mv $HOME/go/bin/metrics $HOME/go/bin/frr-metrics

%install
# Install the binary.
mkdir -p %{buildroot}%{_sbindir}/
install -D -m 0755 $HOME/go/bin/controller %{buildroot}/
install -D -m 0755 $HOME/go/bin/speaker %{buildroot}/
install -D -m 0755 $HOME/go/bin/frr-metrics %{buildroot}/
install -D -m 0755 frr-reloader.sh %{buildroot}/

%files controller-%{version_suffix}
%license LICENSE
/controller

%files speaker-%{version_suffix}
%license LICENSE
/speaker
/frr-metrics
/frr-reloader.sh

%changelog
