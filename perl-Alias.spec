#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Alias - aliasing Perl data for convenient access
Summary(pl):	Alias - aliasowanie danych w Perlu dla wygodniejszego dostêpu
Name:		perl-Alias
Version:	2.32
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Alias/Alias-%{version}.tar.gz
# Source0-md5:	74aee28a4a20e643dd7656c6d8096aa8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alias module provides general mechanisms for aliasing Perl data for
convenient access.

%description -l pl
Modu³ Perla Alias udostêpnia ogólne mechanizmy s³u¿±ce do aliasowania
danych w Perlu dla wygodniejszego dostêpu.

%prep
%setup -q -n Alias-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
