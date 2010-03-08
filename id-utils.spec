%define	name	id-utils
%define	version	4.2
%define	release	%mkrel 1

Summary:	Language-independent identifier database tool 
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2
Group:		Development/C
BuildRequires:	emacs
Source:		ftp://ftp.enst.fr/pub/gnu/gnits/%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-buildroot

%description
mkid is a simple, fast, high-capacity, language-independent
identifier database tool.  Actually, the term `identifier' is too
limiting -- mkid stores tokens, be the program identifiers of any
form, literal numbers, or words of human-readable text.  Database
queries can be issued from the command-line, or from within emacs,
serving as an augmented tags facility.     

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

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
/usr/share/locale/de/LC_MESSAGES/idutils.mo
/usr/share/locale/fr/LC_MESSAGES/idutils.mo
/usr/share/locale/nl/LC_MESSAGES/idutils.mo
/usr/share/locale/pl/LC_MESSAGES/idutils.mo

