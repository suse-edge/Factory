#
# spec file for package nmc
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


Name:           nm-configurator-031
Version:        0.3.1
Release:        0
Summary:        NM Configurator
License:        Apache-2.0
URL:            https://github.com/suse-edge/nm-configurator
Source:         nm-configurator-%{version}.tar
Source1:        vendor.tar.xz

BuildRequires:  cargo-packaging

%description

%prep
%autosetup -p1 -a1 -n nm-configurator-%{version}
install -D -m 644 %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/nm-configurator-%{version}/target/release/nmc %{buildroot}%{_bindir}/nmc

%post
%postun

%files
%{_bindir}/nmc

%changelog


