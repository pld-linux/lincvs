
%define		_rc	rc2
%define		_srcrel	0

Summary:	A Qt-based tool for managing CVS
Summary(pl):	Narzêdzie do zarz±dzania CVS-em oparte na Qt
Name:		lincvs
Version:	1.4.0
Release:	0.%{_rc}.1
# GPL if linked with GPLed qt (as in PLD), custom otherwise (see LICENSE)
License:	GPL
Group:		Development/Version Control
Source0:	http://lincvs.com/download/%{name}-%{version}-%{_rc}-%{_srcrel}-generic-src.tgz
# Source0-md5:	5154107142d865fa6202164241c4dc5f
Source1:	LinCVS.desktop
URL:		http://www.lincvs.org/
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	qmake
Requires:	cvs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LinCVS acts as a reliable (!) graphical frontend for the CVS-client
supporting both CVS-versions 1.9 and 1.10, perhaps even older ones. It
allows to check out a module from and import of a module to a
repository, to update or retrieve the status of a working directory or
single files and common operations like add, remove and commit, diff
against the repository or view of the log messages in list form. In
contrast to other programs this one is REALLY easy to use ;-).

%description -l pl
LinCVS dzia³a jako niezawodny(!) graficzny frontend dla klienta CVS.
Pozwala na import modu³ów z i do repozytorium oraz wszelkiego typu
inne zwyk³e operacje w CVS-ie. W przeciwieñstwie do wielu innych
programów jest NAPRAWDÊ prosty w u¿yciu ;-)

%prep
%setup -q -n %{name}-%{version}-%{_rc}

%build
export QTDIR=%{_prefix}
export QMAKESPEC="%{_datadir}/qt/mkspecs/linux-g++/"
qmake -o Makefile lincvs.pro
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_pixmapsdir}

install lincvs.bin $RPM_BUILD_ROOT%{_bindir}/lincvs

install LinCVS/AppIcon.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/lincvs.xpm
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS LICENSE doc/{README,SSH-HOWTO.txt,PROXY-HOWTO.txt}
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.xpm
