%define oname recordMyDesktop
%define qtoname qt-%{oname}

Summary:	Qt4 frontend for recordmydesktop
Name:		qt-recordmydesktop
Version:	0.3.8
Release:	4
License:	GPLv2+
Group:		Video
URL:		http://recordmydesktop.sourceforge.net
Source0:	http://downloads.sourceforge.net/recordmydesktop/%{name}-%{version}.tar.bz2
Source1:	qt-recordmydesktop_ru-0.3.8.po
BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	python-qt4
BuildRequires:	qt4-devel
%py_requires -d
Requires:	recordmydesktop >= %{version}
Requires:	python-qt4-gui
Requires:	python-sip
BuildArch:	noarch

%description
Qt4 frontend for recordmydesktop tool.

%prep
%setup -q
cp %{SOURCE1} po/ru.po

%build
%configure2_5x
%make

%install
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

%files -f %{qtoname}.lang
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/qt_%{oname}/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.*g
%{_iconsdir}/hicolor/*/apps/*


