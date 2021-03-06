%global commit0 65ec7644168bb78fe30acea9a219ea263e5b5abe
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:		awesome
Version:	3.5.1.r%{shortcommit0}
Release:	git
Summary:	Highly configurable, framework window manager for X. Fast, light and extensible
Group:		User Interface/Desktops
License:	GPLv2+ and BSD
URL:		http://awesome.naquadah.org


Source0:  https://github.com/awesomeWM/%{name}/archive/%{commit0}.tar.gz

BuildRequires:	cmake >= 2.8.0

BuildRequires:	ImageMagick
BuildRequires:	asciidoc
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	lua-devel >= 5.3
BuildRequires:	lua-ldoc
BuildRequires:	xmlto

BuildRequires:	pkgconfig(xcb) >= 1.6
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xkbcommon-x11)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(xcb-randr)
BuildRequires:	pkgconfig(xcb-xkb)
BuildRequires:	pkgconfig(xcb-xtest)
BuildRequires:	pkgconfig(xcb-xinerama)
BuildRequires:	pkgconfig(xcb-shape)
BuildRequires:	pkgconfig(xcb-xrm)
BuildRequires:	pkgconfig(xcb-util) >= 0.3.8
BuildRequires:	pkgconfig(xcb-keysyms) >= 0.3.4
BuildRequires:	pkgconfig(xcb-icccm) >= 0.3.8
BuildRequires:	pkgconfig(xcb-cursor)
BuildRequires:	pkgconfig(cairo-xcb)
BuildRequires:	pkgconfig(libstartup-notification-1.0) >= 0.10
BuildRequires:	pkgconfig(xproto) >= 7.0.15
BuildRequires:	pkgconfig(libxdg-basedir) >= 1.0.0
BuildRequires:	pkgconfig(dbus-1)

BuildRequires:	lua-lgi
BuildRequires:	pkgconfig(pango) >= 1.19.3
BuildRequires:	pkgconfig(pangocairo) >= 1.19.3
Requires:	lua-lgi
# next two loaded via lgi
Requires:	pango%{?_isa} >= 1.19.3
Requires:	cairo-gobject%{?_isa}

BuildRequires:	desktop-file-utils
Requires:	startup-notification >= 0.10
# terminal used in the default configuration
Requires:	xterm
# optional but useful
Requires:	rlwrap
# default editor
Requires:	nano


%description
Awesome is a highly configurable, next generation framework window
manager for X. It is very fast, light and extensible.

It is primary targeted at power users, developers and any people
dealing with every day computing tasks and want to have fine-grained
control on its graphical environment.


%package	doc
Summary:	API doc files
Group:		Documentation
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description	doc
API doc files for awesome generated by luadoc.


%prep
%autosetup -n %{name}-%{commit0}

%build
mkdir build; pushd build
%cmake -DAWESOME_DOC_PATH=%{_pkgdocdir} \
       -DSYSCONFDIR=%{_sysconfdir} \
       ..
popd
make -C build VERBOSE=1 %{?_smp_mflags} awesome


%install
make -C build DESTDIR="%{buildroot}" INSTALL="install -p" install

# verify desktop file
desktop-file-validate %{buildroot}%{_datadir}/xsessions/%{name}.desktop


%files
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/*
%exclude %{_pkgdocdir}/LICENSE
%license LICENSE
%exclude %{_pkgdocdir}/doc
%dir %{_sysconfdir}/xdg/%{name}
%config(noreplace) %{_sysconfdir}/xdg/%{name}/rc.lua
%{_bindir}/awesome
%{_bindir}/awesome-client
%{_datadir}/%{name}
%{_mandir}/man?/*
%{_mandir}/*/man1/*
%{_mandir}/*/man5/*
%{_datadir}/xsessions/%{name}.desktop


%files doc
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/doc
