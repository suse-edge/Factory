Name:           akri
Version:        0
Release:        0
Summary:	A Kubernetes Resource Interface for the Edge 
License:        Apache-2.0
URL:            https://github.com/project-akri/akri
Source0:        %{name}.tar
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging openssl-devel systemd-devel rust >= 1.68.1 protobuf-devel >= 3.19.1 libv4l-devel obs-service-set_version >= 0.5.14

%description
A Kubernetes Resource Interface for the Edge

%package agent
Summary: Device plugin agent for akri
Requires: cri-tools
%description agent
Device plugin agent for akri.

%package controller
Summary: akri controller
%description controller
akri controller

%package webhook-configuration
Summary: Admission webhook for akri.
%description webhook-configuration
Admission webhook for akri.

%package udev-discovery-handler
Summary: udev discovery handler for akri
%description udev-discovery-handler

%package opcua-discovery-handler
Summary: opcua discovery handler for akri
%description opcua-discovery-handler

%package onvif-discovery-handler
Summary: onvif discovery handler for akri
%description onvif-discovery-handler

%package debug-echo-discovery-handler
Summary: debug-echo discovery handler for akri
%description debug-echo-discovery-handler

%package metadata
Summary: Version metadata only for Akri
%description metadata
This package is empty and only serve as dummy package to
correctly get the version in image builds

%prep
%autosetup -n %{name} -a1
# Remove exec bits to prevent an issue in fedora shebang checking. Uncomment only if required.
# find vendor -type f -name \*.rs -exec chmod -x '{}' \;

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}/target/release/agent %{buildroot}%{_bindir}/agent
install -m 0755 %{_builddir}/%{name}/target/release/controller %{buildroot}%{_bindir}/controller
install -m 0755 %{_builddir}/%{name}/target/release/webhook-configuration %{buildroot}%{_bindir}/webhook-configuration
install -m 0755 %{_builddir}/%{name}/target/release/debug-echo-discovery-handler %{buildroot}%{_bindir}/debug-echo-discovery-handler
install -m 0755 %{_builddir}/%{name}/target/release/onvif-discovery-handler %{buildroot}%{_bindir}/onvif-discovery-handler
install -m 0755 %{_builddir}/%{name}/target/release/opcua-discovery-handler %{buildroot}%{_bindir}/opcua-discovery-handler
install -m 0755 %{_builddir}/%{name}/target/release/udev-discovery-handler %{buildroot}%{_bindir}/udev-discovery-handler

%files agent
%{_bindir}/agent

%files controller
%{_bindir}/controller

%files webhook-configuration
%{_bindir}/webhook-configuration

%files udev-discovery-handler
%{_bindir}/udev-discovery-handler

%files opcua-discovery-handler
%{_bindir}/opcua-discovery-handler

%files onvif-discovery-handler
%{_bindir}/onvif-discovery-handler

%files debug-echo-discovery-handler
%{_bindir}/debug-echo-discovery-handler

%files metadata

%changelog

