%ifnarch %{riscv}
# (tpg) optimize it a bit
%global optflags %{optflags} -Oz --rtlib=compiler-rt
%endif

Summary:	Utility to set/show the host name or domain name
Name:		hostname
Version:	3.23
Release:	4
License:	GPLv2+
Group:		System/Configuration/Networking
URL:		http://packages.qa.debian.org/h/hostname.html
Source0:	http://ftp.de.debian.org/debian/pool/main/h/hostname/hostname_%{version}.tar.gz

# Initial changes
Patch1:		hostname-rh.patch
BuildRequires:	pkgconfig(libtirpc)
# net-tools 1.60 provided its own hostname
Conflicts:	net-tools < 2.0

%description
This package provides commands which can be used to display the system's
DNS name, and to display or set its hostname or NIS domain name.

%prep
%autosetup -n %{name} -p1

%build
%set_build_flags
%make_build

%install
make BASEDIR=%{buildroot} BINDIR=%{_bindir} install

%files
%doc COPYRIGHT
%{_bindir}/*
%doc %{_mandir}/man1/*
