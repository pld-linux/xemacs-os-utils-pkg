Summary:	Miscellaneous O/S utilities
Summary(pl):	RÛøne narzÍdzia zwi±zane z O/S
Name:		xemacs-os-utils-pkg
%define 	srcname	os-utils
Version:	1.26
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(cs):	Aplikace/Editory/Emacs
Group(de):	Anwendungen/Editoren/Emacs
Group(es):	Aplicaciones/Editores/Emacs
Group(fr):	Applications/Editeurs/Emacs
Group(ja):	•¢•◊•Í•±°º•∑•Á•Û/•®•«•£•ø/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Group(pt):	AplicaÁıes/Editores/Emacs
Group(ru):	“…Ãœ÷≈Œ…—/Ú≈ƒ¡À‘œ“Ÿ/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Miscellaneous O/S utilities.

%description -l pl 
RÛøne narzÍdzia zwi±zane z OS.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

gzip -9nf lisp/os-utils/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/os-utils/ChangeLog.gz 
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
