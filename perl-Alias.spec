%include	/usr/lib/rpm/macros.perl
Summary:	Alias perl module
Summary(pl):	Modu³ perla Alias
Name:		perl-Alias
Version:	2.32
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Alias/Alias-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alias module provides general mechanisms for aliasing perl data for
convenient access.

%description -l pl
Modu³ perla Alias.

%prep
%setup -q -n Alias-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README Todo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%{perl_sitearch}/Alias.pm

%dir %{perl_sitearch}/auto/Alias
%{perl_sitearch}/auto/Alias/Alias.bs
%attr(755,root,root) %{perl_sitearch}/auto/Alias/Alias.so

%{_mandir}/man3/*
