Summary:	A QT-based tool for managing CVS
Summary(pl):	Narzêdzie do zarz±dzania CVSem oparte na QT
Name:		lincvs
Version:	0.4.0
Release:	1
License:	GPL
Group:		Development/Version Control
Group(pl):	Programowanie/Zarz±dzanie wersjami
Group(pl):	Programowanie/Zarz±dzanie wersjami
Source0:	http://lincvs.sunsite.dk/download/%{name}-%{version}/%{name}-%{version}-0-generic-src.tgz
URL:		http://www.lincvs.org
Requires:	cvs
BuildRequires:	qt >= 2.0.2
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

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
%configure2_13
%{__make} QTDIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README SSH.txt

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
