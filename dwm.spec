Name:		dwm
Version:	6.0
Release:	%mkrel 1
URL:		http://dwm.suckless.org
Source0:	http://dl.suckless.org/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.png
License:	MIT
Group:		Graphical desktop/Other
Summary:	A minimalist window manager for the X Window System
Requires:	xterm
Requires:	xmessage
Requires:	dwm-tools
BuildRequires:	libx11-devel
BuildRequires:	libxinerama-devel

%description
dwm is a dynamic window manager for X.

It manages windows in tiled and floating layouts.
Either layout can be applied dynamically, optimizing
the environment for the application in use and the
task performed. It is the little brother of wmii.

%prep
%setup -q

%build
%make CC="gcc %{optflags} %{ldflags}"

%install
%__rm -rf %{buildroot}
%makeinstall_std DESTDIR=%{buildroot} PREFIX=%{_prefix}

# startfile
%__cat > %{buildroot}%{_bindir}/start%{name} << EOF
#!/bin/sh
exec %{_bindir}/%{name}
EOF

%__chmod 755 %{buildroot}%{_bindir}/start%{name}

# session file
%__install -d %{buildroot}%{_sysconfdir}/X11/wmsession.d
%__cat > %{buildroot}%{_sysconfdir}/X11/wmsession.d/40%{name} << EOF
NAME=%{name}
EXEC=%{_bindir}/start%{name}
DESC=%{name} window manager
SCRIPT:
exec %{_bindir}/start%{name}
EOF

%__mkdir_p %{buildroot}%{_datadir}/icons/
%__cp -f %{SOURCE1} %{buildroot}%{_datadir}/icons/

%clean
%__rm -rf %{buildroot}

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


%changelog
* Thu Feb 09 2012 Andrey Bondrov <abondrov@mandriva.org> 6.0-1mdv2012.0
+ Revision: 772260
- New version 6.0

* Tue Nov 29 2011 Andrey Bondrov <abondrov@mandriva.org> 5.9-1
+ Revision: 735403
- New version 5.9

* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 5.8.2-2
+ Revision: 635319
- simplify BR

* Wed Jul 28 2010 Rémy Clouard <shikamaru@mandriva.org> 5.8.2-1mdv2011.0
+ Revision: 562814
- bump release, fix URL and Source
- clean spec to avoid an rpmlint warning
- add shebang to startdwm script

* Tue Jan 12 2010 Rémy Clouard <shikamaru@mandriva.org> 5.7.2-1mdv2010.1
+ Revision: 490027
- bump release (5.7.2)
- fix licence

* Sun Sep 27 2009 Frederik Himpe <fhimpe@mandriva.org> 5.7.1-1mdv2010.0
+ Revision: 449726
- update to new version 5.7.1

* Mon Jul 27 2009 Frederik Himpe <fhimpe@mandriva.org> 5.6.1-1mdv2010.0
+ Revision: 400631
- update to new version 5.6.1

* Tue Jul 14 2009 Frederik Himpe <fhimpe@mandriva.org> 5.6-1mdv2010.0
+ Revision: 396039
- update to new version 5.6

* Mon May 18 2009 Frederik Himpe <fhimpe@mandriva.org> 5.5-1mdv2010.0
+ Revision: 377334
- Update to new version 5.5

* Wed Feb 18 2009 Jérôme Soyer <saispo@mandriva.org> 5.4-1mdv2009.1
+ Revision: 342494
- New upstream release

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 5.3.1-1mdv2009.1
+ Revision: 324243
- New upstream release

* Wed Dec 03 2008 Jérôme Soyer <saispo@mandriva.org> 5.2-1mdv2009.1
+ Revision: 309671
- New Release 5.2

* Wed Jul 30 2008 Jérôme Soyer <saispo@mandriva.org> 5.1-1mdv2009.0
+ Revision: 254725
- New release 5.1

* Tue Jan 08 2008 Jérôme Soyer <saispo@mandriva.org> 4.7-3mdv2008.1
+ Revision: 146908
- Add Requires

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 13 2007 Jérôme Soyer <saispo@mandriva.org> 4.7-2mdv2008.1
+ Revision: 119225
- Add macro for creating session

* Thu Dec 06 2007 Jérôme Soyer <saispo@mandriva.org> 4.7-1mdv2008.1
+ Revision: 116082
- import dwm


