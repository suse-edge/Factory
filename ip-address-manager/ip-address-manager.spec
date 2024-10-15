#
# spec file for package ip-address-manager
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


Name:           ip-address-manager
Version:        1.7.1
Release:        0
Summary:        Metal3 IPAM controller
License:        Apache-2.0
URL:            https://github.com/metal3-io/ip-address-manager
Source:         ip-address-manager-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) = 1.21
ExcludeArch:    s390
ExcludeArch:    %{ix86}

%description

Metal3 IPAM controller

%prep
%autosetup -a1 -n ip-address-manager-%{version}

%build
go build \
   -mod=vendor \
   -buildmode=pie \

%install
install -D -m0755 ip-address-manager %{buildroot}%{_bindir}/ip-address-manager

%files
%license LICENSE
%doc README.md
%{_bindir}/ip-address-manager

%changelog
