%define upstream_name ProjectBuilder

Summary:	Provides multi-OSes (Linux/Solaris/...) Continuous Packaging
Name:		perl-%{upstream_name}
Version:	0.11.3
Release:	2
License:	GPL
Group:		System/Configuration/Packaging
Url:		http://trac.project-builder.org
Source:		ftp://ftp.project-builder.org/src/%{upstream_name}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
ProjectBuilder is a perl module providing set of functions
to help develop packages for projects and deal
with different Operating systems (Linux distributions, Solaris, ...).
It implements a Continuous Packaging approach.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor CONFDIR=%{_sysconfdir}/pb MANDIR=%{_mandir}
make

%install
%makeinstall_std

%check
make test

%files
%doc NEWS AUTHORS COPYING README
%config(noreplace) %{_sysconfdir}/pb
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man5/*

%changelog
* Fri May 27 2011 Bruno Cornec <bcornec@mandriva.org> 0.11.3-1mdv2011.0
+ Revision: 680266
- Update to upstream 0.11.3 of perl-ProjectBuilder
- Still do not understand the build error msg :-(
- Removes french summary in addition (Bugs !!)
- Removes french desc
- Update to upstream ProjectBuilder 0.11.2
- Force rebuild with newest version
- Update to upstream 0.10.1
- Remove the useless changelog line of the spec file
- Add perl-ProjectBuilder 0.9.9 to Mandriva
- create perl-Project-Builder

