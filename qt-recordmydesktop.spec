%define oname recordMyDesktop
%define	qtoname qt-%{oname}

Summary:	Qt4 fronted for recordmydesktop
Name:		qt-recordmydesktop
Version:	0.3.6
Release:	%mkrel 1
License:	GPL
Group:		Video
URL:		http://recordmydesktop.sourceforge.net
Source0:	http://downloads.sourceforge.net/recordmydesktop/%{name}-%{version}.tar.bz2
BuildRequires:	python-qt
BuildRequires:	libqt4-devel >= 4.2
Requires:	recordmydesktop	>= %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Qt4 frontend for recordmydesktop tool.

%prep
%setup -q

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{qtoname}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{gtkoname}.lang
%defattr(-,root,root)
#%doc AUTHORS ChangeLog README COPYING
#%attr(755,root,root) %{_bindir}/%{gtkoname}
#%dir %{py_sitedir}/%{oname}/
#%{py_sitedir}/%{oname}/*.py*
#%{_datadir}/applications/%{name}.desktop
#%{_datadir}/pixmaps/%{name}.png
