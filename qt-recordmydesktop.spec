%define oname recordMyDesktop
%define	qtoname qt-%{oname}

Summary:	Qt4 frontend for recordmydesktop
Name:		qt-recordmydesktop
Version:	0.3.7
Release:	%mkrel 1
License:	GPLv2+
Group:		Video
URL:		http://recordmydesktop.sourceforge.net
Source0:	http://downloads.sourceforge.net/recordmydesktop/%{name}-%{version}.tar.bz2
BuildRequires:	desktop-file-utils 
BuildRequires:	imagemagick
BuildRequires:	python-qt4
BuildRequires:	qt4-devel >= 4.2
%py_requires -d
Requires:	recordmydesktop	>= %{version}
Requires:	python-qt4-gui
Requires:	python-sip
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

#(tpg) drop icon extension
sed -i -e 's/^Icon=%{name}.png$/Icon=%{name}/g' %{buildroot}%{_datadir}/applications/*

desktop-file-install \
	--add-category='Video;Qt' \
	--add-only-show-in='KDE' \
	--dir=%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*.desktop

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48,64x64,scalable}/apps
convert src/%{name}.png -scale 16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
convert src/%{name}.png -scale 32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert src/%{name}.png -scale 48 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install -m 644 src/%{name}.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
install -m 644 src/%{name}.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg



%find_lang %{qtoname}

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{qtoname}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/qt_%{oname}/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_iconsdir}/hicolor/*/apps/*
