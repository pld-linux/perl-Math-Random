#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Random
Summary:	Math::Random - random number generators
Summary(pl.UTF-8):	Math::Random - generatory liczb losowych
Name:		perl-Math-Random
Version:	0.71
Release:	5
# same as perl except some C code
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	55d7579c670ecd180f71fd157a2d2070
URL:		http://search.cpan.org/dist/Math-Random/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Random is a Perl port of the C version of randlib, which is
a suite of routines for generating random deviates.

%description -l pl.UTF-8
Math::Random jest perlowym portem napisanej w C biblioteki randlib,
będącej zbiorem procedur do generowania liczb losowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
mkdir examples
mv example.pl examples

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALLDIRS=vendor

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -r examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README MANIFEST
%{perl_vendorarch}/Math/*.pm
%dir %{perl_vendorarch}/auto/Math/Random
%attr(755,root,root) %{perl_vendorarch}/auto/Math/Random/*.so
%{perl_vendorarch}/auto/Math/Random/*.ix
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_mandir}/man3/*
