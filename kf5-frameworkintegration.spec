%define		kdeframever	5.91
%define		qtver		5.9.0
%define		kfname		frameworkintegration

Summary:	HTML rendering engine
Name:		kf5-%{kfname}
Version:	5.91.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	d6e68519c97992610722b0a68c563a34
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	fonts-TTF-KDE-Oxygen-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-attica-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-kauth-devel >= %{version}
BuildRequires:	kf5-kbookmarks-devel >= %{version}
BuildRequires:	kf5-kcodecs-devel >= %{version}
BuildRequires:	kf5-kcompletion-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
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
BuildRequires:	kf5-knewstuff-devel >= %{version}
BuildRequires:	kf5-knotifications-devel >= %{version}
BuildRequires:	kf5-kservice-devel >= %{version}
BuildRequires:	kf5-ktextwidgets-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf5-kwindowsystem-devel >= %{version}
BuildRequires:	kf5-kxmlgui-devel >= %{version}
BuildRequires:	kf5-solid-devel >= %{version}
BuildRequires:	kf5-sonnet-devel >= %{version}
BuildRequires:	libxcb-devel
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KHTML is a web rendering engine, based on the KParts technology and
using KJS for JavaScript support.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%ghost %{_libdir}/libKF5Style.so.5
%attr(755,root,root) %{_libdir}/libKF5Style.so.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/FrameworkIntegrationPlugin.so
%{_datadir}/knotifications5/plasma_workspace.notifyrc
%dir %{_prefix}/libexec/kf5/kpackagehandlers
%attr(755,root,root) %{_prefix}/libexec/kf5/kpackagehandlers/knshandler
%dir %{_datadir}/kf5/infopage
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
%{_includedir}/KF5/FrameworkIntegration
%{_libdir}/cmake/KF5FrameworkIntegration
%{_libdir}/libKF5Style.so
