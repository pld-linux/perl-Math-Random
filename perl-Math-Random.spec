#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Random
Summary:	Math::Random - useful routines and packages with Math::Random/Random
Summary(pl):	Math::Random - przydatne funkcje i pakiety oparte o Math::Random/Random
Name:		perl-Math-Random
Version:	0.67
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5: 021006f39529940ae318c7c105d01a44
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Random module contains some routines that may come in handy when
you want to get some random numbers.

%description -l pl
Modu³ Math::Random zawiera trochê procedur, które mog± okazaæ siê pomocne
przy pracy z liczbami losowymi.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL SITEPREFIX=/usr  	INSTALLDIR=%{perl_vendorlib} 

%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README MANIFEST
%{perl_archlib}/Math/Random.pm
%{perl_archlib}/Math/example.pl
%{_mandir}/man3/*
#%dir %{_examplesdir}/%{name}-%{version}
#%{_examplesdir}/%{name}-%{version}/*.txt
#%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
