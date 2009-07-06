#
# $Id$
#
%define perlvendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define srcname	ProjectBuilder

Summary:	Perl module providing support and deal with Linux distributions
Summary(fr):	Module Perl pour le support de diverses distributions Linux

Name:		perl-ProjectBuilder
Version:	0.9.7
Release:	%mkrel 1
License:	GPL
Group:		System/Configuration/Packaging
Url:		http://trac.project-builder.org
Source:		ftp://ftp.project-builder.org/src/%{srcname}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{srcname}-%{version}-%{release}-root-%(id -u -n)
BuildArch:	noarch
Requires:	perl >= 5.8.4,  

%description
perl-ProjectBuilder is a perl module providing set of functions
to help develop perl projects and deal with Linux distributions.

%description -l fr
perl-ProjectBuilder est un ensemble de fonctions pour aider à développer des projets perl 
et à traiter de diverses distributions Linux.

%prep
%setup -q -n %{srcname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor destdir=${RPM_BUILD_ROOT}/ 
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

%{perlvendorlib}/*
%{_bindir}/*
#%{_mandir}/man1/*
%{_mandir}/man3/*

