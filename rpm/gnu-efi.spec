# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       gnu-efi

# >> macros
# << macros

Summary:    EFI development environment
Version:    3.0
Release:    1
Group:      System/Boot
License:    BSD-3-Clause
ExclusiveArch:  %ix86 x86_64
URL:        http://sourceforge.net/projects/gnu-efi/
Source0:    http://download.sourceforge.net/%{name}/%{name}_%{version}v.orig.tar.gz
Source100:  gnu-efi.yaml
Patch0:     stdarg.patch
BuildRequires:  pciutils

%description
gnu-efi is a library for building EFI applications.

%prep
%setup -q -n %{name}-%{version}

# stdarg.patch
%patch0 -p1
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
make install PREFIX=%{_prefix} INSTALLROOT=%{buildroot}
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_includedir}/efi/*
%{_prefix}/lib/*
# >> files
# << files