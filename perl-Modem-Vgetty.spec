%define upstream_name       Modem-Vgetty
%define upstream_version    0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:	Interface to vgetty(8)
License:	GPL or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Modem/%{upstream_name}-0.03.tar.gz
Patch0:		Modem-Vgetty-0.04-VOCP.patch
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Modem::Vgetty is an encapsulation object for writing applications for voice
modems using the vgetty(8) or vm(8) package. The answering machines and
sofisticated voice applications can be written using this module.

%prep
%setup -q -n %{upstream_name}-0.03
%patch0 -p1
# perl path hack
find . -type f | \
    xargs %{__perl} -pi -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc examples ChangeLog README
%{perl_vendorlib}/Modem
%{_mandir}/man3*/*
