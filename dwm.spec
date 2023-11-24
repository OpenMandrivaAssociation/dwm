%define debug_package %{nil}

Summary:	A minimalist window manager for the X Window System
Name:		dwm
Version:	6.4
Release:	1
License:	MIT
Group:		Graphical desktop/Other
Url:		http://dwm.suckless.org
Source0:	http://dl.suckless.org/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.png
BuildRequires:  pkgconfig(xft)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xinerama)
Requires:	dwm-tools
Requires:	xmessage
Requires:	xterm

%description
dwm is a dynamic window manager for X.

It manages windows in tiled and floating layouts. Either layout can be applied
dynamically, optimizing the environment for the application in use and the
task performed. It is the little brother of wmii.

%files
%defattr(-,root,root,755)
%doc LICENSE README
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/40%{name}
%{_bindir}/%{name}
%{_bindir}/start%{name}
%{_mandir}/man1/dwm.1*
%{_datadir}/icons/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%make CC="gcc %{optflags} %{ldflags}"

%install
%makeinstall_std DESTDIR=%{buildroot} PREFIX=%{_prefix}

# startfile
cat > %{buildroot}%{_bindir}/start%{name} << EOF
#!/bin/sh
exec %{_bindir}/%{name}
EOF

chmod 755 %{buildroot}%{_bindir}/start%{name}

# session file
install -d %{buildroot}%{_sysconfdir}/X11/wmsession.d
cat > %{buildroot}%{_sysconfdir}/X11/wmsession.d/40%{name} << EOF
NAME=%{name}
EXEC=%{_bindir}/start%{name}
DESC=%{name} window manager
SCRIPT:
exec %{_bindir}/start%{name}
EOF

mkdir -p %{buildroot}%{_datadir}/icons/
cp -f %{SOURCE1} %{buildroot}%{_datadir}/icons/

