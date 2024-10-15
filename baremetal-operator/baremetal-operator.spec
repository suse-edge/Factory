#
# spec file for package baremetal-operator
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


Name:           baremetal-operator
Version:        0.6.1
Release:        0.6.1
Summary:        Implements a Kubernetes API for managing bare metal hosts
License:        Apache-2.0
URL:            https://github.com/metal3-io/baremetal-operator
Source:         baremetal-operator-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) = 1.21
ExcludeArch:    s390
ExcludeArch:    %{ix86}

%description
The Bare Metal Operator implements a Kubernetes API for managing bare metal hosts. 
It maintains an inventory of available hosts as instances of the BareMetalHost Custom Resource Definition. 
The Bare Metal Operator knows how to:

Inspect the host’s hardware details and report them on the corresponding BareMetalHost. 
This includes information about CPUs, RAM, disks, NICs, and more.
Provision hosts with a desired image.
Clean a host’s disk contents before or after provisioning.
More capabilities are being added regularly. See open issues and pull requests for more information on work in progress.

For more information about Metal³, the Bare Metal Operator, and other related components, see the Metal³ docs.

%prep
%autosetup -a1 -n baremetal-operator-%{version} -p1

%build   
%define buildtime %(date +%%Y-%%m-%%dT%%H:%%M:%%S%%z)
%define buildcommit %%SOURCE_COMMIT%%
%define buildflags "-X github.com/metal3-io/baremetal-operator/pkg/version.Raw=%{version}\
 -X github.com/metal3-io/baremetal-operator/pkg/version.BuildTime=%{buildtime}\
 -X github.com/metal3-io/baremetal-operator/pkg/version.Commit=%{buildcommit}"

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags %{buildflags}

%install
install -D -m0755 baremetal-operator %{buildroot}%{_bindir}/baremetal-operator

%files
%license LICENSE
%doc README.md
%{_bindir}/baremetal-operator

%changelog
