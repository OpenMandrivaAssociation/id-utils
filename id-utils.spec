%define name id-utils
%define version 3.2d
%define release  %mkrel 6

Summary:  Language-independent identifier database tool 
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Development/C
Source: ftp://ftp.enst.fr/pub/gnu/gnits/%{name}-%{version}.tar.bz2

%description
mkid is a simple, fast, high-capacity, language-independent
identifier database tool.  Actually, the term `identifier' is too
limiting -- mkid stores tokens, be the program identifiers of any
form, literal numbers, or words of human-readable text.  Database
queries can be issued from the command-line, or from within emacs,
serving as an augmented tags facility.     

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build

%configure

%make

%install

%makeinstall

%find_lang %name

%clean

%post
%_install_info %name

%preun
%_remove_install_info %name


%files -f %name.lang
%defattr (-,root,root)
%doc README INSTALL COPYING AUTHORS ABOUT-NLS NEWS THANKS TODO 
%{_bindir}/*
%{_infodir}/*
%{_datadir}/emacs/site-lisp/*
%{_datadir}/id-lang.map

