%define upstream_name    Modem-Vgetty
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Epoch:		1

Summary:	Interface to vgetty(8)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Modem/%{upstream_name}-0.03.tar.gz
Patch0:		Modem-Vgetty-0.03-VOCP.patch

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Modem::Vgetty is an encapsulation object for writing applications for voice
modems using the vgetty(8) or vm(8) package. The answering machines and
sofisticated voice applications can be written using this module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1
# perl path hack
find . -type f | \
    xargs perl -pi -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc examples ChangeLog README
%{perl_vendorlib}/Modem
%{_mandir}/man3*/*


%changelog
* Fri Feb 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.30.0-1mdv2010.1
+ Revision: 504968
- decrement rpm version to match real package version (sigh)

* Sun Aug 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 419930
- new perl version macro

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.04-9mdv2009.0
+ Revision: 241749
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-7mdv2008.0
+ Revision: 86639
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-6mdv2007.0
- Rebuild

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-5mdk
- Fix According to perl Policy
	- add module macro
	- Source URL
	- URL
- use mkrel

* Mon Jul 04 2005 Oden Eriksson <oeriksson@mandriva.com> 0.04-4mdk
- rebuild

* Sat Jun 05 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.04-3mdk
- rebuilt, fix deps
- use macros

