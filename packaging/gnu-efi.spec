# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       gnu-efi

# >> macros
# << macros
%define efidir maui

Summary:    EFI development environment
Version:    3.0u
Release:    1
Group:      System/Libraries
License:    BSD-3-Clause
ExclusiveArch:  %ix86 x86_64
URL:        http://sourceforge.net/projects/gnu-efi/
Source0:    http://download.sourceforge.net/%{name}/%{name}_%{version}.orig.tar.gz
Source100:  gnu-efi.yaml
Patch0:     0001-fix-compilation-on-x86_64-without-HAVE_USE_MS_ABI.patch
Patch1:     0002-be-more-pedantic-when-linking.patch
Patch2:     0003-Sample-boot-service-driver.patch
BuildRequires:  pciutils

%description
gnu-efi is a library for building EFI applications.

%package devel
Summary:    Development Libraries and headers for EFI
Group:      Development/System
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains development headers and libraries for developing
applications that run under EFI (Extensible Firmware Interface).


%package utils
Summary:    Utilities for EFI systems
Group:      Applications/System
Requires:   %{name} = %{version}-%{release}

%description utils
This package contains utilties for debugging and developing EFI systems.


%prep
%setup -q -n %{name}-3.0

# 0001-fix-compilation-on-x86_64-without-HAVE_USE_MS_ABI.patch
%patch0 -p1
# 0002-be-more-pedantic-when-linking.patch
%patch1 -p1
# 0003-Sample-boot-service-driver.patch
%patch2 -p1
# >> setup
# << setup

%build
# >> build pre
make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/%{_libdir}
make install PREFIX=%{_prefix} INSTALLROOT=%{buildroot}

mkdir -p %{buildroot}/%{_libdir}/gnuefi
mv %{buildroot}/%{_libdir}/*.lds %{buildroot}/%{_libdir}/*.o %{buildroot}/%{_libdir}/gnuefi

make -C apps clean route80h.efi modelist.efi
mkdir -p %{buildroot}/boot/efi/EFI/%{efidir}/
mv apps/{route80h.efi,modelist.efi} %{buildroot}/boot/efi/EFI/%{efidir}/
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_libdir}/*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%doc README.* ChangeLog
%{_includedir}/efi
# >> files devel
# << files devel

%files utils
%defattr(-,root,root,-)
%dir /boot/efi/EFI/%{efidir}/
%attr(0644,root,root) /boot/efi/EFI/%{efidir}/*.efi
# >> files utils
# << files utils