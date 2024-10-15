%global debug_package %{nil}

Name: kubectl-1303
Version: 1.30.3
Release: 0
Summary: Command-line utility for interacting with a Kubernetes cluster

%if "%{_vendor}" == "debbuild"
Group: admin
%endif

Packager: Kubernetes Authors <dev@kubernetes.io>
License: Apache-2.0
URL: https://kubernetes.io
Source0: kubectl_%{version}.orig.tar.gz

%description
%{summary}.

%prep
%setup -q -c

%build
# Nothing to build

%install
# Detect host arch
KUBE_ARCH="$(uname -m)"

# Install binaries
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 ${KUBE_ARCH}/kubectl %{buildroot}%{_bindir}/kubectl

%files
%{_bindir}/kubectl
%license LICENSE
%doc README.md

%changelog
