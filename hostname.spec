Summary:	Utility to set/show the host name or domain name
Name:		hostname
Version:	3.25
Release:	1
License:	GPLv2+
Group:		System/Configuration/Networking
URL:		https://packages.qa.debian.org/h/hostname.html
Source0:	https://salsa.debian.org/meskes/hostname/-/archive/debian/%{version}/hostname-debian-%{version}.tar.bz2

# Initial changes
Patch1:		hostname-rh.patch
BuildRequires:	make
BuildRequires:	pkgconfig(libtirpc)
# net-tools 1.60 provided its own hostname
Conflicts:	net-tools < 2.0

%description
This package provides commands which can be used to display the system's
DNS name, and to display or set its hostname or NIS domain name.

%prep
%autosetup -n %{name}-debian-%{version} -p1

%build
%set_build_flags
%make_build

%install
%make_install

%files
%doc COPYRIGHT
%{_bindir}/*
%doc %{_mandir}/man1/*
