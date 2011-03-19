#
# $Id$
#
%define perlvendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define srcname ProjectBuilder

Summary:	Perl module providing multi-OSes (Linux/Solaris/...) Continuous Packaging
Summary(fr):	Module Perl pour le support de divers OS (Linux/Solaris/...)

Name:		perl-ProjectBuilder
Version:	0.11.2
Release:	%mkrel 1
License:	GPL
Group:		System/Configuration/Packaging
Url:		http://trac.project-builder.org
Source:		ftp://ftp.project-builder.org/src/%{srcname}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{srcname}-%{version}-%{release}-root-%(id -u -n)
BuildArch:	noarch
Requires:	perl >= 5.8.4, 

%description
ProjectBuilder is a perl module providing set of functions
to help develop packages for projects and deal
with different Operating systems (Linux distributions, Solaris, ...).
It implements a Continuous Packaging approach.

%description -l fr
perl-ProjectBuilder est un ensemble de fonctions pour aider à développer des projets perl 
et à traiter de diverses distributions Linux.

%prep
%setup -q -n %{srcname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor destdir=${RPM_BUILD_ROOT}/  CONFDIR=%{_sysconfdir}/pb MANDIR=%{_mandir}
make

%install
%{__rm} -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install
find ${RPM_BUILD_ROOT} -type f -name perllocal.pod -o -name .packlist -o -name '*.bs' -a -size 0 | xargs rm -f
find ${RPM_BUILD_ROOT} -type d -depth | xargs rmdir --ignore-fail-on-non-empty

%check
make test

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc NEWS AUTHORS
%doc INSTALL COPYING README
%config(noreplace) %{_sysconfdir}/pb

%{perlvendorlib}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man5/*
