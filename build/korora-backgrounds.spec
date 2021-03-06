%global relnum 27
%global Bg_Name Korora
%global bgname korora

# Enable Animation
%global with_animated 0

# Enable Extras
%global with_extras 1

Name:           %{bgname}-backgrounds
Version:        %{relnum}.0.0
Release:        1%{?dist}
Summary:        Korora default desktop background

License:        CC-BY-SA
URL:            https://github.com/kororaproject/kp-korora-backgrounds
Source0:        %{name}-%{version}.tar.gz
# Plasma desktoptheme
# This is in the source tarball
#Source1:        metadata.desktop

BuildArch:	noarch

# for %%_kde4_* macros
BuildRequires:	kde-filesystem

Requires:	%{name}-gnome = %{version}-%{release}
Requires:	%{name}-kde = %{version}-%{release}
Requires:	%{name}-xfce = %{version}-%{release}
Requires:	%{name}-mate = %{version}-%{release}

Provides:       f%{relnum}-backgrounds
Obsoletes:      f%{relnum}-backgrounds

%description
This package contains desktop backgrounds for the Korora %{relnum} default
theme. Pulls in themes for GNOME, KDE, Mate and Xfce desktops.

%package	base
Summary:	Base images for Korora %{relnum} default background
License:	CC-BY-SA

Provides:       f%{relnum}-backgrounds-base
Obsoletes:      f%{relnum}-backgrounds-base

%description	base
This package contains base images for Korora %{relnum} default background.

%if %{with_animated}
%package	animated
Summary:	Time of day images for Fedora %{relnum} backgrounds

Requires:	%{name}-base = %{version}-%{release}

%description	animated
This package contains the time of day images for Fedora %{relnum}
Backgrounds.
%endif

%package	kde
Summary:	Korora %{relnum} default wallpaper for KDE

Requires:	%{name}-base = %{version}-%{release}
Requires:	kde-filesystem
Supplements:	%{name}-animated = %{version}-%{release}

Provides:       f%{relnum}-backgrounds-kde
Obsoletes:      f%{relnum}-backgrounds-kde

%description    kde
This package contains KDE desktop wallpaper for the Korora %{relnum}
default theme.

%package	gnome
Summary:	Korora %{relnum} default wallpaper for Gnome and Cinnamon

Requires:	%{name}-base = %{version}-%{release}
Supplements:	%{name}-animated = %{version}-%{release}

Provides:       f%{relnum}-backgrounds-gnome
Obsoletes:      f%{relnum}-backgrounds-gnome

%description	gnome
This package contains GNOME/Cinnamon desktop wallpaper for the
Korora %{relnum} default theme.

%package	mate
Summary:	Korora %{relnum} default wallpaper for Mate

Requires:	%{name}-base = %{version}-%{release}
Supplements:	%{name}-animated = %{version}-%{release}

Provides:       f%{relnum}-backgrounds-mate
Obsoletes:      f%{relnum}-backgrounds-mate

%description	mate
This package contains MATE desktop wallpaper for the Korora %{relnum}
default theme.

%package	xfce
Summary:	Korora 22 default background for Xfce4

Requires:	%{name}-base = %{version}-%{release}
Requires:	xfdesktop

Provides:       f%{relnum}-backgrounds-xfce
Obsoletes:      f%{relnum}-backgrounds-xfce

%description	xfce
This package contains Xfce4 desktop background for the Korora 22
default theme.

%if %{with_extras}
%package	extras-base
Summary:	Base images for Korora Extras Backrounds
License:	CC-BY and CC-BY-SA
Provides:       f%{relnum}-backgrounds-extras-base
Obsoletes:      f%{relnum}-backgrounds-extras-base

%description	extras-base
This package contains base images for Korora supplemental
wallpapers.

%package	extras-gnome
Summary:	Extra Korora Wallpapers for GNOME and Cinnamon

Requires:	%{name}-extras-base

Provides:       f%{relnum}-backgrounds-extras-gnome
Obsoletes:      f%{relnum}-backgrounds-extras-gnome

%description	extras-gnome
This package contains Korora supplemental wallpapers for GNOME
and Cinnamon

%package	extras-mate
Summary:	Extra Korora Wallpapers for MATE

Requires:	%{name}-extras-base = %{version}-%{release}

Provides:       f%{relnum}-backgrounds-extras-mate
Obsoletes:      f%{relnum}-backgrounds-extras-mate

%description    extras-mate
This package contains Korora supplemental wallpapers for MATE

%package	extras-kde
Summary:	Extra Korora Wallpapers for KDE

Requires:	%{name}-extras-base

Provides:       f%{relnum}-backgrounds-extras-kde
Obsoletes:      f%{relnum}-backgrounds-extras-kde

%description	extras-kde
This package contains Korora supplemental wallpapers for GNOME

%package	extras-xfce
Summary:	Extra Korora Wallpapers for Xfce

Requires:	%{name}-extras-base = %{version}-%{release}

Provides:       f%{relnum}-backgrounds-extras-xfce
Obsoletes:      f%{relnum}-backgrounds-extras-xfce

%description	extras-xfce
This package contains Korora supplemental wallpapers for Xfce
%endif

%prep
%autosetup


%build
%make_build


%install
%make_install

install -D -p -m644 metadata.desktop \
%{buildroot}%{_datadir}/plasma/desktoptheme/%{Bg_Name}/metadata.desktop

%files
%doc

%files base
%license CC-BY-SA-4.0 Attribution
%dir %{_datadir}/backgrounds/%{bgname}
%dir %{_datadir}/backgrounds/%{bgname}/default
%{_datadir}/backgrounds/%{bgname}/default/normalish
%{_datadir}/backgrounds/%{bgname}/default/standard
%{_datadir}/backgrounds/%{bgname}/default/wide
%{_datadir}/backgrounds/%{bgname}/default/tv-wide
%{_datadir}/backgrounds/%{bgname}/default/%{bgname}.xml

%if %{with_animated}
%files animated
%dir %{_datadir}/backgrounds/%{bgname}/default-animated
%{_datadir}/backgrounds/%{bgname}/default-animated/normalish
%{_datadir}/backgrounds/%{bgname}/default-animated/standard
%{_datadir}/backgrounds/%{bgname}/default-animated/wide
%{_datadir}/backgrounds/%{bgname}/default-animated/tv-wide
%{_datadir}/backgrounds/%{bgname}/default-animated/%{bgname}.xml
%endif

%files kde
%{_kde4_datadir}/wallpapers/%{Bg_Name}/
%dir %{_datadir}/plasma/
%dir %{_datadir}/plasma/desktoptheme/
%{_datadir}/plasma/desktoptheme/%{Bg_Name}/

%files gnome
%{_datadir}/gnome-background-properties/%{bgname}.xml
%if %{with_animated}
%{_datadir}/gnome-background-properties/%{bgname}-animated.xml
%endif

%files mate
%{_datadir}/mate-background-properties/%{bgname}.xml
%if %{with_animated}
%{_datadir}/mate-background-properties/%{bgname}-animated.xml
%endif

%files xfce
%{_datadir}/xfce4/backdrops/%{bgname}.png

%if %{with_extras}
%files extras-base
%license CC-BY-SA-4.0 CC-BY-4.0 CC0-1.0 Attribution-Extras
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
* Tue Oct 10 2017 Ian Firns <firnsy@kororaproject.org> - 27.0-1
- Update for Korora 27

* Fri Nov 11 2016 Chris Smart <csmart@kororaproject.org> - 25.0-1
- Update for Korora 25

* Thu Jul 14 2016 Ian Firns <firnsy@kororaproject.org> - 24.0-3
- Fixed version

* Wed Jul 13 2016 Ian Firns <firnsy@kororaproject.org> - 24.0-2
- Updated images including community contributions.

* Thu May 12 2016 Chris Smart <csmart@kororaproject.org> - 24.0-1
- Update for Korora 24

* Wed Dec 30 2015 Chris Smart <csmart@kororaproject.org> - 23.1-3
- Don't provide and replace Fedora's backgrounds, dnf doesn't like it bz#1096506

* Thu Nov 5 2015 Chris Smart <csmart@kororaproject.org> - 23.1-2
- Provide and replace Fedora's backgrounds

* Wed Nov 4 2015 Chris Smart <csmart@kororaproject.org> - 23.1-1
- Update for Korora 23

* Sat Jul 25 2015 Ian Firns <firnsy@kororaproject.org> - 22.1-1
- Added extras based on f21

* Thu Jun 25 2015 Ian Firns <firnsy@kororaproject.org> - 22.0.1-1
- Updates for the 22 release

* Sun Dec 28 2014 Ian Firns <firnsy@kororaproject.org> - 21.0.1-1
- Fixed incorrect backgrounds

* Fri Nov 14 2014 Ian Firns <firnsy@kororaproject.org> - 21.0.0-1
- Updates for the 21 release

* Fri Nov  8 2013 Ian Firns <firnsy@kororaproject.org> - 20.0-1
- Initial RPM release
