%define snap 20070301
Summary:	Database support tools and replication for PostgreSQL
Name:		skytools
Version:	0.0
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	%{name}-%{snap}.tar.gz
# Source0-md5:	3e0f9b1065203fc16ffc6c1d2e49b2d0
Patch0:	%{name}-contribdir.patch
URL:		https://developer.skype.com/SkypeGarage/DbProjects/SkyTools
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	postgresql-backend-devel
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-libs
Requires:	python-psycopg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is package of tools used at Skype to manage their cluster of
PostgreSQL servers.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%configure
python setup.py build

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/postgresql/*.so
%dir %{py_sitescriptdir}/londiste
%{py_sitescriptdir}/londiste/*.py[co]
%dir %{py_sitescriptdir}/pgq
%{py_sitescriptdir}/pgq/*.py[co]
%dir %{py_sitescriptdir}/skytools
%{py_sitescriptdir}/skytools/*.py[co]
%{_datadir}/postgresql/contrib/*
