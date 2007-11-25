#
#### this spec is DEPRECATED - new name is crossvc.spec
#
%define		_srcrel	0

Summary:	A Qt-based tool for managing CVS
Summary(pl.UTF-8):	Narzędzie do zarządzania CVS-em oparte na Qt
Name:		lincvs
Version:	1.4.4
Release:	1
# GPL if linked with GPLed qt (as in PLD), custom otherwise (see LICENSE)
License:	GPL
Group:		Development/Version Control
Source0:	http://lincvs.com/download/%{name}-%{version}-%{_srcrel}-generic-src.tgz
# Source0-md5:	e5bdeeffb2511579b0c9ba3e33f636e8
Source1:	LinCVS.desktop
Patch0:		%{name}-gcc4.patch
URL:		http://www.lincvs.org/
BuildRequires:	libtool
BuildRequires:	qmake
BuildRequires:	qt-devel >= 6:3.3
BuildRequires:	sed >= 4.0
Requires:	cvs >= 1.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LinCVS acts as a reliable (!) graphical frontend for the CVS-client
supporting both CVS-versions 1.9 and 1.10, perhaps even older ones. It
allows to check out a module from and import of a module to a
repository, to update or retrieve the status of a working directory or
single files and common operations like add, remove and commit, diff
against the repository or view of the log messages in list form. In
contrast to other programs this one is REALLY easy to use ;-).

%description -l pl.UTF-8
LinCVS działa jako niezawodny(!) graficzny frontend dla klienta CVS.
Pozwala na import modułów z i do repozytorium oraz wszelkiego typu
inne zwykłe operacje w CVS-ie. W przeciwieństwie do wielu innych
programów jest NAPRAWDĘ prosty w użyciu ;-)

%prep
%setup -q
%patch0 -p0
%{__sed} -i 's,`dirname.*,%{_datadir}/%{name},' LinCVS/AppRun

%build
export QTDIR=%{_prefix}
export QMAKESPEC="%{_datadir}/qt/mkspecs/linux-g++/"
qmake -o Makefile lincvs.pro
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{Messages,Tools}

install LinCVS/AppRun $RPM_BUILD_ROOT%{_bindir}/lincvs
install lincvs.bin $RPM_BUILD_ROOT%{_datadir}/%{name}
install ts/*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/Messages
install contrib/rshwrapper/rshwrapper $RPM_BUILD_ROOT%{_datadir}/%{name}/Tools
install contrib/ssh-askpass/ssh-askpass.bin $RPM_BUILD_ROOT%{_datadir}/%{name}/Tools
install tools/*.sh $RPM_BUILD_ROOT%{_datadir}/%{name}/Tools
install LinCVS/AppIcon.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/lincvs.xpm
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS LICENSE doc/{README,SSH-HOWTO.txt,PROXY-HOWTO.txt}
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/Messages
%attr(755,root,root) %{_datadir}/%{name}/lincvs.bin
%attr(755,root,root) %{_datadir}/%{name}/Tools
%lang(ca) %{_datadir}/%{name}/Messages/ca_ES.qm
%lang(de) %{_datadir}/%{name}/Messages/de.qm
%lang(es) %{_datadir}/%{name}/Messages/es.qm
%lang(fr) %{_datadir}/%{name}/Messages/fr.qm
%lang(it) %{_datadir}/%{name}/Messages/it.qm
%lang(ja) %{_datadir}/%{name}/Messages/ja.qm
%lang(ru) %{_datadir}/%{name}/Messages/ru.qm
%lang(vi) %{_datadir}/%{name}/Messages/vi.qm
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.xpm
