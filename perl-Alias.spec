%include	/usr/lib/rpm/macros.perl
Summary:	Alias perl module
Summary(es):	Modulo Perl Alias
Summary(pl):	Modu³ perla Alias
Summary(pt_BR):	Modulo Perl Alias
Name:		perl-Alias
Version:	2.32
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Alias/Alias-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alias module provides general mechanisms for aliasing perl data for
convenient access.

%description -l es
Convenient wrappers for "obscure" perl functionality.

%description -l pl
Modu³ perla Alias.

%description -l pt_BR
Convenient wrappers for "obscure" perl functionality.

%prep
%setup -q -n Alias-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README Todo

%{perl_vendorarch}/Alias.pm

%dir %{perl_vendorarch}/auto/Alias
%{perl_vendorarch}/auto/Alias/Alias.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Alias/Alias.so

%{_mandir}/man3/*
