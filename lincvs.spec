Summary:	A QT-based tool for managing CVS
Summary(pl):	Narzêdzie do zarz±dzania CVSem oparte na QT
Name:		lincvs
Version:	0.9.90
Release:	1
License:	GPL
Group:		Development/Version Control
Source0:	http://lincvs.sunsite.dk/download/%{name}-%{version}/%{name}-%{version}-0-generic-src.tgz
Source1:	LinCVS.desktop
URL:		http://www.lincvs.org
Requires:	cvs
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	qt-devel >= 2.2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix	/usr/X11R6

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

%build
libtoolize --copy --force
%configure2_13
%{__make} QTDIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Development

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Development

gzip -9nf AUTHORS ChangeLog NEWS README SSH.txt

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_applnkdir}/Development/*
