%define	name	dwm
%define	version	5.6
%define	rel	1
%define	release	%mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.suckless.org/wiki/dwm
Source0:	http://code.suckless.org/dl/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.png
License:	GPL
Group:		Graphical desktop/Other
Summary:	A minimalist window manager for the X Window System
Requires:	xterm xmessage dwm-tools
BuildRequires:	X11-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
dwm is a dynamic window manager for X.

It manages windows in tiled and floating layouts.
Either layout can be applied dynamically, optimizing
the environment for the application in use and the
task performed. It is the little brother of wmii.

%prep
%setup -q

%build
%make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall_std DESTDIR=%{buildroot} PREFIX=/usr

# startfile
%{__cat} > $RPM_BUILD_ROOT%{_bindir}/start%{name} << EOF
exec %{_bindir}/%{name}
EOF

chmod 755 $RPM_BUILD_ROOT%{_bindir}/start%{name}

# session file
%{__install} -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmsession.d
%{__cat} > $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmsession.d/40%{name} << EOF
NAME=%{name}
EXEC=%{_bindir}/start%{name}
DESC=%{name} window manager
SCRIPT:
exec %{_bindir}/start%{name}
EOF

mkdir -p %{buildroot}/%{_datadir}/icons/
cp -f %{SOURCE1} %{buildroot}/%{_datadir}/icons/

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post
%make_session

%postun
%make_session

%files
%defattr(-,root,root,755)
%doc LICENSE README
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/40%{name}
%{_bindir}/%{name}
%{_bindir}/start%{name}
%{_mandir}/man1/dwm.1*
%{_datadir}/icons/%{name}.png
