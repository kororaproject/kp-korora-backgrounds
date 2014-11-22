Name:           korora-backgrounds
Version:        21.0
Release:        1%{?dist}.1
Summary:        Korora desktop backgrounds

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
Summary:        Base images for Korora Backgrounds
Group:          Applications/Multimedia
License:        CC-BY-SA

%description    base
This package contains base images for Korora Backgrounds

%package        animated
Summary:        Time of day images for Korora Backgrounds
Group:          Applications/Multimedia

Requires:       %{name}-base = %{version}-%{release}

%description    animated
This package contains the time of day images for Korora backgrounds

%package        kde
Summary:        Korora Wallpapers for KDE
Group:          Applications/Multimedia

Requires:       %{name}-animated = %{version}-%{release}
Requires:       kde-filesystem

%description    kde
This package contains KDE desktop wallpapers for the Korora
theme.

%package        gnome
Summary:        Korora Wallpapers for Gnome
Group:          Applications/Multimedia

Requires:       %{name}-animated = %{version}-%{release}

%description    gnome
This package contains Gnome/Cinnamon desktop wallpapers for the
Korora theme.

%package        mate
Summary:        Korora Wallpapers for Mate
Group:          Applications/Multimedia

Requires:       %{name}-animated = %{version}-%{release}

%description    mate
This package contains Mate desktop wallpapers for the Korora theme.


%package        xfce
Summary:        Korora Wallpapers for XFCE4
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
#%doc CC-BY-SA-3.0 Attribution
%dir %{_datadir}/backgrounds/korora
%dir %{_datadir}/backgrounds/korora/default
%{_datadir}/backgrounds/korora/default/normalish
%{_datadir}/backgrounds/korora/default/standard
%{_datadir}/backgrounds/korora/default/wide
%{_datadir}/backgrounds/korora/default/tv-wide
%{_datadir}/backgrounds/korora/default/korora.xml

%files animated
%dir %{_datadir}/backgrounds/korora/default-animated
%{_datadir}/backgrounds/korora/default-animated/normalish
%{_datadir}/backgrounds/korora/default-animated/standard
%{_datadir}/backgrounds/korora/default-animated/wide
%{_datadir}/backgrounds/korora/default-animated/tv-wide
%{_datadir}/backgrounds/korora/default-animated/korora.xml

%files kde
%{_kde4_datadir}/wallpapers/Korora/

%files gnome
%{_datadir}/gnome-background-properties/korora-animated.xml

%files mate
%{_datadir}/mate-background-properties/korora-animated.xml

%files xfce
%{_datadir}/xfce4/backdrops/korora.png

%changelog
* Fri Nov  8 2013 Ian Firns <firnsy@kororaproject.org> - 21.0-1
- Updated for 21 release.

* Fri Nov  8 2013 Ian Firns <firnsy@kororaproject.org> - 20.0-1
- Initial RPM release
