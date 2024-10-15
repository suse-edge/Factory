#
# spec file for package cosign-rgs
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

%define project https://github.com/hauler-dev/cosign
%define revision 49542360ffb5de63f9d2f5856b658651d5538e40 

Name:           cosign
Version:        0
Release:        0
Summary:        Container Signing, Verification and Storage in an OCI registry
License:        Apache-2.0
URL:            https://github.com/rancher-government-carbide/cosign
Source:         cosign-%{version}.tar.gz
Source1:        vendor.tar.gz         
BuildRequires:  golang-packaging

%description

%prep
%setup -q -a1 -n cosign-%{version}

%build
%goprep %{project}

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

CLI_PKG=sigs.k8s.io/release-utils/version
CLI_LDFLAGS="-X ${CLI_PKG}.gitVersion=%{version} -X ${CLI_PKG}.gitCommit=%{revision} -X ${CLI_PKG}.gitTreeState=release -X ${CLI_PKG}.buildDate=${BUILD_DATE}"

CGO_ENABLED=0 go build -mod=vendor -buildmode=pie -trimpath -ldflags "${CLI_LDFLAGS}" -o cosign ./cmd/cosign

%install
install -D -m 0755 cosign %{buildroot}%{_bindir}/cosign

%files
%license LICENSE
%doc *.md
%{_bindir}/cosign

%changelog
