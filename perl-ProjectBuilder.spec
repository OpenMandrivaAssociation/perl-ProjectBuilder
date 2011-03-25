%define upstream_name ProjectBuilder

Name:		perl-%{upstream_name}
Version:	0.11.2
Release:	%mkrel 1
Summary:	Perl module providing multi-OSes (Linux/Solaris/...) Continuous Packaging
License:	GPL
Group:		System/Configuration/Packaging
Url:		http://trac.project-builder.org
Source:		ftp://ftp.project-builder.org/src/%{upstream_name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
ProjectBuilder is a perl module providing set of functions to help develop
packages for projects and deal with different Operating systems (Linux
distributions, Solaris, ...).
It implements a Continuous Packaging approach.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%{__perl} Makefile.PL \
    INSTALLDIRS=vendor \
    CONFDIR=%{_sysconfdir}/pb \
    MANDIR=%{_mandir}

make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%check
make test

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS AUTHORS INSTALL COPYING README
%config(noreplace) %{_sysconfdir}/pb
%{perl_vendorlib}/ProjectBuilder
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man5/*
