#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

Summary:	Alias - aliasing Perl data for convenient access
Summary(pl.UTF-8):	Alias - aliasowanie danych w Perlu dla wygodniejszego dostępu
Name:		perl-Alias
Version:	2.32
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Alias/Alias-%{version}.tar.gz
# Source0-md5:	74aee28a4a20e643dd7656c6d8096aa8
URL:		http://search.cpan.org/dist/Alias/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alias module provides general mechanisms for aliasing Perl data for
convenient access.

%description -l pl.UTF-8
Moduł Perla Alias udostępnia ogólne mechanizmy służące do aliasowania
danych w Perlu dla wygodniejszego dostępu.

%prep
%setup -q -n Alias-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%attr(755,root,root) %{perl_vendorarch}/auto/Alias/Alias.so

%{_mandir}/man3/*
