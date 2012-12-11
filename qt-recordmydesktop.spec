%define oname recordMyDesktop
%define	qtoname qt-%{oname}

Summary:	Qt4 frontend for recordmydesktop
Name:		qt-recordmydesktop
Version:	0.3.8
Release:	%mkrel 3
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

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{qtoname}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/qt_%{oname}/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.*g
%{_iconsdir}/hicolor/*/apps/*


%changelog
* Thu Nov 04 2010 Funda Wang <fwang@mandriva.org> 0.3.8-3mdv2011.0
+ Revision: 593100
- rebuild for py 2.7

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 0.3.8-2mdv2011.0
+ Revision: 323383
- rebuild

* Mon Nov 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.8-1mdv2009.1
+ Revision: 306402
- update to new version 0.3.8

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.3.7.2-4mdv2009.0
+ Revision: 259982
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.3.7.2-3mdv2009.0
+ Revision: 247790
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Feb 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.7.2-1mdv2008.1
+ Revision: 173743
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.7-1mdv2008.1
+ Revision: 131924
- new version
- drop patch0, handle this with sed
- spec file clean

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 13 2007 Funda Wang <fwang@mandriva.org> 0.3.6-3mdv2008.0
+ Revision: 84874
- fix desktop icon ext

  + Adam Williamson <awilliamson@mandriva.org>
    - correct spelling error in summary
    - don't package COPYING
    - icon fixes: install to correct directories, convert from png not svg (imagemagick does not convert from svg to png well), install 64x64 and svg icons as well
    - requires python-sip (#33426)
    - Fedora license policy

* Tue Aug 21 2007 Funda Wang <fwang@mandriva.org> 0.3.6-2mdv2008.0
+ Revision: 68191
- Add Qt category
- use hicolor icon theme
- complete spec file
- cp spec file from gtk frontend
- Created package structure for qt-recordmydesktop.

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - new version
    - rework spec file

