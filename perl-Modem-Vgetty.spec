%define module  Modem-Vgetty
%define name	perl-Modem-Vgetty
%define version	0.04
%define release %mkrel 9

Summary:	%{module} module for perl 
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp.perl.org/pub/CPAN/modules/by-module/Modem/%{module}-0.03.tar.bz2
Patch0:		Modem-Vgetty-0.04-VOCP.patch
URL:		http://www.cpan.org/dist/%{module}
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
%{module} module for perl

%prep

%setup -q -n %{module}-0.03
%patch0 -p1
# perl path hack
find . -type f | xargs %{__perl} -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor </dev/null
%{__make}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

%makeinstall_std

%clean 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc examples ChangeLog README
%{perl_vendorlib}/Modem/*.pm
%{_mandir}/man3*/*

