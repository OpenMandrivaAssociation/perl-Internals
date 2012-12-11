%define upstream_name    Internals
%define upstream_version 1.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    Write-protect variables, manipulate refcounts
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This module allows you to write-protect and write-enable your Perl
variables, objects and data structures.

Moreover, the reference count of any Perl variable can be read and set.

You can never pass the object directly on which to perform the desired
action, you always have to pass a reference to the variable or data
structure in question.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.txt Artistic.txt GNU_GPL.txt CHANGES.txt
%{_mandir}/man3/*
%perl_vendorarch/Internals.pm
%perl_vendorarch/auto/Internals


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.100.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.100.0-2mdv2011.0
+ Revision: 555272
- rebuild

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2010.1
+ Revision: 504935
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1-3mdv2010.0
+ Revision: 430471
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.1-2mdv2009.0
+ Revision: 268535
- rebuild early 2009.0 package (before pixel changes)

* Sun Jun 01 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-1mdv2009.0
+ Revision: 214061
- import perl-Internals


* Sun Jun 01 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-1mdv2009.0
- first mdv release  
