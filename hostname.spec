Summary:	Utility to set/show the host name or domain name
Name:		hostname
Version:	3.21
Release:	1
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
%setup_compile_flags
%make_build

%install
make BASEDIR=%{buildroot} install
mkdir -p %{buildroot}%{_bindir}
for i in dnsdomainname domainname hostname nisdomainname ypdomainname; do
    ln -sf /bin/$i %{buildroot}%{_bindir}/$i
done

%files
%doc COPYRIGHT
/bin/*
%{_bindir}/*
%{_mandir}/man1/*
