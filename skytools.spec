Summary:	Database support tools and replication for PostgreSQL
Summary(pl.UTF-8):	Narzędzia wspomagające i replikacja dla baz danych PostgreSQL
Name:		skytools
Version:	2.1.9
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	http://pgfoundry.org/frs/download.php/2129/%{name}-%{version}.tar.gz
# Source0-md5:	bc1a2f05b27d45d93814b892387361dc
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

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia używane przez firmę Skype do zarządzania
klastrem serwerów PostgreSQL.

%prep
%setup -q

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
%{_mandir}/man1/bulk_loader.1*
%{_mandir}/man1/cube_dispatcher.1*
%{_mandir}/man1/londiste.1*
%{_mandir}/man1/pgqadm.1*
%{_mandir}/man1/queue_mover.1*
%{_mandir}/man1/queue_splitter.1*
%{_mandir}/man1/scriptmgr.1*
%{_mandir}/man1/skytools_upgrade.1*
%{_mandir}/man1/table_dispatcher.1*
%{_mandir}/man1/walmgr.1*
%{_mandir}/man5/londiste.5*
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/postgresql/*.so
%dir %{py_sitedir}/londiste
%{py_sitedir}/londiste/*.py[co]
%dir %{py_sitedir}/pgq
%{py_sitedir}/pgq/*.py[co]
%dir %{py_sitedir}/skytools
%{py_sitedir}/skytools/*.py[co]
%{py_sitedir}/skytools/_cquoting.so
%{_datadir}/postgresql/contrib/*
