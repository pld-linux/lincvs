Summary:	A QT-based tool for managing CVS
Summary(pl):	Narzêdzie do zarz±dzania CVSem oparte na QT
Name:		lincvs
Version:	1.1.6
Release:	1
License:	GPL
Group:		Development/Version Control
Source0:	http://lincvs.sunsite.dk/download/%{name}-%{version}/%{name}-%{version}-0-generic-src.tgz
Source1:	LinCVS.desktop
Patch0:		%{name}-config.patch
URL:		http://www.lincvs.org/
Requires:	cvs
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	qt-devel >= 3.0.5
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
LinCVS dzia³a jako wiarygodny (!) graficzny frontend dla klienta CVS.
Pozwala na import modu³ów z i do respozytorium oraz wszelkiego typu
inne zwyk³e operacje w CVS'ie. W przeciwieñstwie do wielu innych
programów jest NAPRAWDÊ prosty w u¿yciu ;-)

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%patch0 -p1 

%build
export QTDIR=%{_prefix}
export QMAKESPEC="%{_datadir}/qt/mkspecs/linux-g++/"
qmake -o Makefile lincvs.pro
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Development

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Development

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README SSH.txt
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_applnkdir}/Development/*
