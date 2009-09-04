%define module   Internals
%define version  1.1
%define release  %mkrel 3

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Write-protect variables, manipulate refcounts
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module//%{module}-%{version}.tar.gz
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
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

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

