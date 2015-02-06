%define upstream_name ProjectBuilder

Summary:	Provides multi-OSes (Linux/Solaris/...) Continuous Packaging
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.12.6
Release:	3
License:	GPL
Group:		System/Configuration/Packaging
Url:		http://trac.project-builder.org
Source:		ftp://ftp.project-builder.org:21/src/%{upstream_name}-%{version}.tar.gz

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
