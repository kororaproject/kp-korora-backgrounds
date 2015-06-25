%global bgname korora
%global Bg_Name Korora

Name:           korora-backgrounds
Version:        22.0.1
Release:        1%{?dist}.1
Summary:        Korora default desktop background

Group:          Applications/Multimedia
License:        CC-BY-SA
URL:            https://github.com/kororaproject/kp-korora-backgrounds
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires:  kde-filesystem
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}
Requires:       %{name}-xfce = %{version}-%{release}
Requires:       %{name}-mate = %{version}-%{release}


%description
This package contains desktop backgrounds for the Korora 22 default theme.
Pulls in themes for GNOME, KDE, Mate and Xfce desktops.

%package        base
Summary:        Base images for Korora 22 default background
Group:          Applications/Multimedia
License:        CC-BY-SA

%description    base
This package contains base images for Korora 22 default background.


%package        kde
Summary:        Korora 22 default wallpaper for KDE
Group:          Applications/Multimedia

Requires:       %{name}-base = %{version}-%{release}
Requires:       kde-filesystem

%description    kde
This package contains KDE desktop wallpaper for the Korora 22
default theme.

%package        gnome
Summary:        Korora 22 default wallpaper for Gnome and Cinnamon
Group:          Applications/Multimedia

Requires:       %{name}-base = %{version}-%{release}

%description    gnome
This package contains Gnome/Cinnamon desktop wallpaper for the
Korora 22 default theme.

%package        mate
Summary:        Korora 22 default wallpaper for Mate
Group:          Applications/Multimedia

Requires:       %{name}-base = %{version}-%{release}

%description    mate
This package contains Mate desktop wallpaper for the Korora 22
default theme.

%package        xfce
Summary:        Korora 22 default background for XFCE4
Group:          Applications/Multimedia

Requires:       %{name}-base = %{version}-%{release}
Requires:       xfdesktop

%description    xfce
This package contains XFCE4 desktop background for the Korora 22
default theme.

%if %{with_extras}
%package        extras-base
Summary:        Base images for F22 Extras Backrounds
Group:          Applications/Multimedia
License:        CC-BY and CC-BY-SA

%description    extras-base
This package contains base images for F22 supplemental
wallpapers.

%package        extras-gnome
Summary:        Extra F22 Wallpapers for Gnome and Cinnamon
Group:          Applications/Multimedia

Requires:       %{name}-extras-base

%description    extras-gnome
This package contains F22 supplemental wallpapers for Gnome
and Cinnamon

%package        extras-mate
Summary:        Extra F22 Wallpapers for Mate
Group:          Applications/Multimedia

Requires:       %{name}-extras-base

%description    extras-mate
This package contains F22 supplemental wallpapers for Mate

%package        extras-kde
Summary:        Extra F22 Wallpapers for KDE
Group:          Applications/Multimedia

Requires:       %{name}-extras-base

%description    extras-kde
This package contains F22 supplemental wallpapers for Gnome

%package        extras-xfce
Summary:        Extra F22 Wallpapers for XFCE
Group:          Applications/Multimedia

Requires:       %{name}-extras-base

%description    extras-xfce
This package contains F22 supplemental wallpapers for XFCE
%endif

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc

%files base
%doc CC-BY-SA-3.0 Attribution
%dir %{_datadir}/backgrounds/%{bgname}
%dir %{_datadir}/backgrounds/%{bgname}/default
%{_datadir}/backgrounds/%{bgname}/default/normalish
%{_datadir}/backgrounds/%{bgname}/default/standard
%{_datadir}/backgrounds/%{bgname}/default/wide
%{_datadir}/backgrounds/%{bgname}/default/tv-wide
%{_datadir}/backgrounds/%{bgname}/default/%{bgname}.xml

%files kde
%{_kde4_datadir}/wallpapers/%{Bg_Name}/

%files gnome
%{_datadir}/gnome-background-properties/%{bgname}.xml

%files mate
%{_datadir}/mate-background-properties/%{bgname}.xml

%files xfce
%{_datadir}/xfce4/backdrops/%{bgname}.png

%if %{with_extras}
%files extras-base
%doc CC-BY-SA-3.0 CC-BY-3.0 CC0-1.0 Attribution-Extras
%{_datadir}/backgrounds/%{bgname}/extras/*.jpg
%{_datadir}/backgrounds/%{bgname}/extras/*.png
%{_datadir}/backgrounds/%{bgname}/extras/%{bgname}-extras.xml

%files extras-gnome
%{_datadir}/gnome-background-properties/%{bgname}-extras.xml

%files extras-kde
%{_kde4_datadir}/wallpapers/%{Bg_Name}_*/

%files extras-mate
%{_datadir}/mate-background-properties/%{bgname}-extras.xml

%files extras-xfce
%{_datadir}/xfce4/backdrops/*.jpg
%{_datadir}/xfce4/backdrops/*.png
%endif

%changelog
* Thu Jun 25 2015 Ian Firns <firnsy@kororaproject.org> - 22.0.1-1
- Updates for the 22 release

* Sun Dec 28 2014 Ian Firns <firnsy@kororaproject.org> - 21.0.1-1
- Fixed incorrect backgrounds

* Fri Nov 14 2014 Ian Firns <firnsy@kororaproject.org> - 21.0.0-1
- Updates for the 21 release

* Fri Nov  8 2013 Ian Firns <firnsy@kororaproject.org> - 20.0-1
- Initial RPM release
