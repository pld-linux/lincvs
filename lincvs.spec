Name:		lincvs
Summary:	A QT-based tool for managing CVS
Version:	0.2.5
Release:	1
Source0:	http://ppprs1.phy.tu-dresden.de/~trogisch/lincvs/download/%{name}_%{version}.tar.gz
Group:		Development/Version Control
Group(pl):	Programowanie/Zarz±dzanie wersjami
Group(pl):	Programowanie/Zarz±dzanie wersjami
URL:		http://ppprs1.phy.tu-dresden.de/~trogisch/lincvs/lincvsen.html
License:	GPL
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

%setup -q -n LinCVS-%{version}

%build
%{__make} QTDIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
cp LinCVS $RPM_BUILD_ROOT%{_bindir}

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.TXT
%attr(755,root,root) %{_bindir}/LinCVS
