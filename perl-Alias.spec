%include	/usr/lib/rpm/macros.perl
Summary:	Alias perl module
Summary(pl):	Modu³ perla Alias
Name:		perl-Alias
Version:	2.32
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Alias/Alias-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Alias module provides general mechanisms for aliasing perl data for convenient
access.

%description -l pl
Modu³ perla Alias.

%prep
%setup -q -n Alias-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Alias/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Alias
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README Todo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,Todo}.gz

%{perl_sitearch}/Alias.pm

%dir %{perl_sitearch}/auto/Alias
%{perl_sitearch}/auto/Alias/.packlist
%{perl_sitearch}/auto/Alias/Alias.bs
%attr(755,root,root) %{perl_sitearch}/auto/Alias/Alias.so

%{_mandir}/man3/*
