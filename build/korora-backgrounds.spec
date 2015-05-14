%global bgname korora
%global Bg_Name Korora

Name:           korora-backgrounds
Version:        21.0.1
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
This package contains desktop backgrounds for the Korora theme.
Pulls in themes for GNOME, KDE, Mate and Xfce desktops.

%package        base
Summary:        Base images for Korora default background
Group:          Applications/Multimedia
License:        CC-BY-SA

%description    base
This package contains base images for Korora default background.

%package        animated
Summary:        Time of day images for Korora default background
Group:          Applications/Multimedia

Requires:       %{name}-base = %{version}-%{release}

%description    animated
This package contains the time of day images for Korora backgrounds.

%package        kde
Summary:        Korora default wallpaper for KDE
Group:          Applications/Multimedia

Requires:       %{name}-animated = %{version}-%{release}
Requires:       kde-filesystem

%description    kde
This package contains KDE desktop wallpaper for the Korora
default theme.

%package        gnome
Summary:        Korora default wallpaper for Gnome and Cinnamon
Group:          Applications/Multimedia

Requires:       %{name}-animated = %{version}-%{release}

%description    gnome
This package contains Gnome/Cinnamon desktop wallpaper for the
Korora default theme.

%package        mate
Summary:        Korora default wallpaper for Mate
Group:          Applications/Multimedia

Requires:       %{name}-animated = %{version}-%{release}

%description    mate
This package contains Mate desktop wallpaper for the Korora default theme.

%package        xfce
Summary:        Korora default background for XFCE4
Group:          Applications/Multimedia

Requires:       %{name}-base = %{version}-%{release}
Requires:       xfdesktop

%description    xfce
This package contains XFCE4 desktop wallpapers for the Korora
theme.

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

%files animated
%dir %{_datadir}/backgrounds/%{bgname}/default-animated
%{_datadir}/backgrounds/%{bgname}/default-animated/normalish
%{_datadir}/backgrounds/%{bgname}/default-animated/standard
%{_datadir}/backgrounds/%{bgname}/default-animated/wide
%{_datadir}/backgrounds/%{bgname}/default-animated/tv-wide
%{_datadir}/backgrounds/%{bgname}/default-animated/%{bgname}.xml

%files kde
%{_kde4_datadir}/wallpapers/%{Bg_Name}/

%files gnome
%{_datadir}/gnome-background-properties/korora-animated.xml

%files mate
%{_datadir}/mate-background-properties/korora-animated.xml

%files xfce
%{_datadir}/xfce4/backdrops/%{bgname}.png

%changelog
* Sun Dec 28 2014 Ian Firns <firnsy@kororaproject.org> - 21.0.1-1
- Fixed incorrect backgrounds

* Fri Nov 14 2014 Ian Firns <firnsy@kororaproject.org> - 21.0.0-1
- Updates for the 21 release

* Fri Nov  8 2013 Ian Firns <firnsy@kororaproject.org> - 20.0-1
- Initial RPM release
