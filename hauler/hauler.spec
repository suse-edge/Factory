#
# spec file for package hauler 
#
# Copyright (c) 2024 SUSE LLC
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

%define project github.com/hauler-dev/hauler

Name:           hauler-107
Version:        1.0.7
Release:        0
Summary:        Airgap Swiss Army Knife
License:        Apache-2.0
URL:            https://github.com/hauler-dev/hauler
Source:         hauler-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  cosign-223

%description

%prep
%setup -q -n hauler-%{version}

%build
%goprep %{project}

tar -xf %{SOURCE1}

mkdir cmd/hauler/binaries
cp `which cosign` cmd/hauler/binaries/cosign-linux-%{go_arch}

go build -mod=vendor -buildmode=pie -o hauler ./cmd/hauler

%install

install -D -m 0755 hauler %{buildroot}%{_bindir}/hauler

%files
%doc README.md
%{_bindir}/hauler

%changelog



