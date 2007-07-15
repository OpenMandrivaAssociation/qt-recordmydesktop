%define oname recordMyDesktop
%define	qtoname qt-%{oname}

Summary:	Qt4 fronted for recordmydesktop
Name:		qt-recordmydesktop
Version:	0.2
Release:	%mkrel 1
License:	GPL
Group:		Video
URL:		http://recordmydesktop.sourceforge.net
Source0:	http://downloads.sourceforge.net/recordmydesktop/%{name}-%{version}.tar.gz
BuildRequires:	qt4-devel
Requires:	recordmydesktop	>= %{version}
BuildRequires:	desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Qt4 Frontend for recordmydesktop tool.

%prep
%setup -q

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std
desktop-file-install \
	--add-category="Video" \
	--add-category="Qt" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*
			     
%find_lang %{qtoname}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{qtoname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README COPYING
%attr(755,root,root) %{_bindir}/%{gtkoname}
%dir %{py_sitedir}/%{oname}/
%{py_sitedir}/%{oname}/*.py*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
