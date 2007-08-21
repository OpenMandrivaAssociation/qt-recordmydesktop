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
BuildRequires:	desktop-file-utils ImageMagick
BuildRequires:	python-qt4
BuildRequires:	qt4-devel >= 4.2
%py_requires -d
Requires:	recordmydesktop	>= %{version}
Requires:	python-qt4-gui
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

desktop-file-install --vendor='' \
	--dir=%buildroot%_datadir/applications \
	--add-category='Video' \
	--add-only-show-in='KDE' \
	%buildroot%_datadir/applications/*.desktop

mkdir -p %buildroot%_iconsdir/hicolor/{16x16,32x32,48x48}/hicolor/apps
convert src/%{name}.svg -resize 16x16 %buildroot%_iconsdir/hicolor/16x16/hicolor/apps/%{name}.png
convert src/%{name}.svg -resize 32x32 %buildroot%_iconsdir/hicolor/32x32/hicolor/apps/%{name}.png
convert src/%{name}.svg -resize 48x48 %buildroot%_iconsdir/hicolor/48x48/hicolor/apps/%{name}.png

%find_lang %{qtoname}

%post
%update_menus
%update_icon_cache hicolor

%postun
%clean_menus
%clean_icon_cache hicolor

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{qtoname}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README COPYING
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/qt_%{oname}/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_iconsdir}/hicolor/*/hicolor/apps/*.png
