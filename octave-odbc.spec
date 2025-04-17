%global octpkg odbc

Summary:	Basic Octave implementation of the ODBC toolkit
Name:		octave-odbc
Version:	0.0.3
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/odbc/
Url:		https://github.com/gnu-octave/octave-odbc/
Source0:	https://github.com/gnu-octave/octave-odbc/releases/download/v%{version}/octave-odbc-%{version}.tar.gz

BuildRequires:  octave-devel >= 6.0.0
BuildRequires:  pkgconfig(odbc)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Basic Octave implementation of the ODBC toolkit

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

