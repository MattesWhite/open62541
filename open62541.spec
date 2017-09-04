Name:     open62541
Version:  0.2
Release:  1%{?dist}
Summary:  OPC UA implementation
License:  MPLv2.0
URL:      http://open62541.org
Source0:  https://github.com/ctron/open62541/archive/%{name}-%{version}.tar.gz

BuildRequires: cmake, python

%description
open62541 is a C-based library (linking with C++ projects is possible)
with all necessary tools to implement dedicated OPC UA clients and servers,
or to integrate OPC UA-based communication into existing applications.

%package  devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version} # double-name prefix by GitHub

%build
%cmake -DUA_ENABLE_AMALGAMATION=ON .
make %{?_smp_mflags}

%install
%make_install

# Remove this from the examples installation
rm examples/CMakeLists.txt

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE LICENSE-CC0
%doc AUTHORS CHANGELOG README.md
%{_libdir}/libopen62541.so.*

%files devel
%{_libdir}/libopen62541.so
%{_includedir}/open62541.h
%doc FEATURES.md
%doc examples/

%changelog
* Thu Aug 31 2017 Jens Reimann <jreimann@redhat.com> - 0.2-1
- Initial version of the package

