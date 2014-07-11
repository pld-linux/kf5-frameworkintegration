# TODO:
# Not packaged dirs:
# /usr/include/KF5
# /usr/lib/qt5/plugins/kf5
# /usr/share/kf5/infopage

%define         _state          stable
%define		orgname		frameworkintegration

Summary:	HTML rendering engine
Name:		kf5-%{orgname}
Version:	5.0.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/frameworks/%{version}/%{orgname}-%{version}.tar.xz
# Source0-md5:	032d0a08977a457206915dbeeff0ef47
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= 5.2.0
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.3.1
BuildRequires:	Qt5Network-devel >= 5.2.0
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5X11Extras-devel
BuildRequires:	Qt5Xml-devel >= 5.2.0
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-attica-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= 1.0.0
BuildRequires:	kf5-kauth-devel >= %{version}
BuildRequires:	kf5-kbookmarks-devel >= %{version}
BuildRequires:	kf5-kcodecs-devel >= %{version}
BuildRequires:	kf5-kcompletion-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= 5.0.0
BuildRequires:	kf5-kconfigwidgets-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kdbusaddons-devel >= %{version}
BuildRequires:	kf5-kglobalaccel-devel >= %{version}
BuildRequires:	kf5-kguiaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kiconthemes-devel >= %{version}
BuildRequires:	kf5-kio-devel >= %{version}
BuildRequires:	kf5-kitemviews-devel >= %{version}
BuildRequires:	kf5-kjobwidgets-devel >= %{version}
BuildRequires:	kf5-knotifications-devel >= %{version}
BuildRequires:	kf5-kservice-devel >= %{version}
BuildRequires:	kf5-ktextwidgets-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf5-kwindowsystem-devel >= %{version}
BuildRequires:	kf5-kxmlgui-devel >= %{version}
BuildRequires:	kf5-solid-devel >= %{version}
BuildRequires:	kf5-sonnet-devel >= %{version}
BuildRequires:	libxcb-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KHTML is a web rendering engine, based on the KParts technology and
using KJS for JavaScript support.

%package devel
Summary:	Header files for %{orgname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{orgname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{orgname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{orgname}.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DBIN_INSTALL_DIR=%{_bindir} \
	-DKCFG_INSTALL_DIR=%{_datadir}/config.kcfg \
	-DPLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQT_PLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQML_INSTALL_DIR=%{qt5dir}/qml \
	-DIMPORTS_INSTALL_DIR=%{qt5dirs}/imports \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_LIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_INCLUDE_INSTALL_DIR=%{_includedir} \
	-DECM_MKSPECS_INSTALL_DIR=%{qt5dir}/mkspecs/modules \
	-D_IMPORT_PREFIX=%{_prefix} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{orgname}5

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{orgname}5.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %ghost %{_libdir}/libKF5Style.so.5
%attr(755,root,root) %{_libdir}/libKF5Style.so.5.0.0
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/FrameworkIntegrationPlugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/platformthemes/KDEPlatformTheme.so
%{_datadir}/kf5/infopage/bar-bottom-left.png
%{_datadir}/kf5/infopage/bar-bottom-middle.png
%{_datadir}/kf5/infopage/bar-bottom-right.png
%{_datadir}/kf5/infopage/bar-middle-left.png
%{_datadir}/kf5/infopage/bar-middle-right.png
%{_datadir}/kf5/infopage/bar-top-left.png
%{_datadir}/kf5/infopage/bar-top-middle.png
%{_datadir}/kf5/infopage/bar-top-right.png
%{_datadir}/kf5/infopage/body-background.png
%{_datadir}/kf5/infopage/box-bottom-left.png
%{_datadir}/kf5/infopage/box-bottom-middle.png
%{_datadir}/kf5/infopage/box-bottom-right.png
%{_datadir}/kf5/infopage/box-center.png
%{_datadir}/kf5/infopage/box-middle-left.png
%{_datadir}/kf5/infopage/box-middle-right.png
%{_datadir}/kf5/infopage/box-top-left.png
%{_datadir}/kf5/infopage/box-top-middle.png
%{_datadir}/kf5/infopage/box-top-right.png
%{_datadir}/kf5/infopage/kde_infopage.css
%{_datadir}/kf5/infopage/kde_infopage_rtl.css
%{_datadir}/kf5/infopage/top-middle.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KStyle
%{_includedir}/KF5/frameworkintegration_version.h
%{_libdir}/cmake/KF5FrameworkIntegration
%attr(755,root,root) %{_libdir}/libKF5Style.so