Summary:	Utility to set/show the host name or domain name
Name:		hostname
Version:	3.17
Release:	1
License:	GPLv2+
Group:		System/Configuration/Networking
URL:		http://packages.qa.debian.org/h/hostname.html
Source0:	http://ftp.de.debian.org/debian/pool/main/h/hostname/hostname_%{version}.tar.gz

# Initial changes
Patch1:		hostname-rh.patch
BuildRequires:	pkgconfig(libtirpc)

%description
This package provides commands which can be used to display the system's
DNS name, and to display or set its hostname or NIS domain name.

%prep
%setup -qn %{name}
%apply_patches

%build
%setup_compile_flags
%make

%install
make BASEDIR=%{buildroot} install

%files
%doc COPYRIGHT
/bin/*
%{_mandir}/man1/*
