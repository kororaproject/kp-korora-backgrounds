%define upstream_package schrodinger-cat-backgrounds

Name:           korora-backgrounds
Version:        18.90.0
Release:        1%{?dist}
Summary:        Korora desktop backgrounds

Group:          Applications/Multimedia
License:        CC-BY-SA
URL:            https://fedoraproject.org/wiki/F19_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{upstream_package}-%{version}.tar.xz
Source1:        korora-background-normalish.jpg
Source2:        korora-background-standard.jpg
Source3:        korora-background-wide.jpg

Provides:       %{upstream_package}
Obsoletes:      %{upstream_package}

BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires:  kde-filesystem
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}
Requires:       %{name}-xfce = %{version}-%{release}
Requires:       %{name}-mate = %{version}-%{release}


%description
This package contains desktop backgrounds for the Korora theme.
Pulls in both Gnome, KDE, MATE and XFCE themes.

%package        base
Summary:        Base images for Korora Backgrounds
Group:          Applications/Multimedia
License:        CC-BY-SA
Provides:       %{upstream_package}-base
Obsoletes:      %{upstream_package}-base

%description    base
This package contains base images for Schrödinger's Cat Backgrounds.

%package        animated
Summary:        Time of day images for Schrödinger's Cat Backgrounds
Group:          Applications/Multimedia
Provides:       %{upstream_package}-animated
Obsoletes:      %{upstream_package}-animated

Requires:       %{name}-base = %{version}-%{release}

%description    animated
This package contains the time of day images for Korora backgrounds

%package        kde
Summary:        Korora Wallpapers for KDE
Group:          Applications/Multimedia
Provides:       %{upstream_package}-kde
Obsoletes:      %{upstream_package}-kde

Requires:       %{name}-base = %{version}-%{release}
Requires:       kde-filesystem

%description    kde
This package contains KDE desktop wallpapers for the Korora
theme.

%package        gnome
Summary:        Korora Wallpapers for Gnome
Group:          Applications/Multimedia
Provides:       %{upstream_package}-gnome
Obsoletes:      %{upstream_package}-gnome

Requires:       %{name}-animated = %{version}-%{release}

%description    gnome
This package contains Gnome desktop wallpapers for the Korora
theme.

%package        mate
Summary:        Schrödinger's Cat Wallpapers for Mate
Group:          Applications/Multimedia
Provides:       %{upstream_package}-mate
Obsoletes:      %{upstream_package}-mate

Requires:       %{name}-animated = %{version}-%{release}

%description    mate
This package contains Mate desktop wallpapers for the Korora theme.


%package        xfce
Summary:        Schrödinger's Cat Wallpapers for XFCE4
Group:          Applications/Multimedia
Provides:       %{upstream_package}-xfce
Obsoletes:      %{upstream_package}-xfce

Requires:       %{name}-base = %{version}-%{release}
Requires:       xfdesktop

%description    xfce
This package contains XFCE4 desktop wallpapers for the Schrödinger's Cat
theme.

# Extras will be enabled later
#~ %package        extras-base
#~ Summary:        Base images for Schrödinger's Cat Extras Backrounds
#~ Group:          Applications/Multimedia
#~ License:        CC-BY and CC-BY-SA
#~
#~ %description    extras-base
#~ This package contains base images for Schrödinger's Cat supplemental
#~ wallpapers.
#~
#~ %package        extras-gnome
#~ Summary:        Extra Schrödinger's Cat Wallpapers for Gnome and Cinnamon
#~ Group:          Applications/Multimedia
#~
#~ Requires:       %{name}-extras-base
#~
#~ %description    extras-gnome
#~ This package contains Schrödinger's Cat supplemental wallpapers for Gnome
#~ and Cinnamon
#~
#~ %package        extras-mate
#~ Summary:        Extra Schrödinger's Cat Wallpapers for Mate
#~ Group:          Applications/Multimedia
#~
#~ Requires:       %{name}-extras-base
#~
#~ %description    extras-mate
#~ This package contains Schrödinger's Cat supplemental wallpapers for Mate
#~
#~ %package        extras-kde
#~ Summary:        Extra Schrödinger's Cat Wallpapers for KDE
#~ Group:          Applications/Multimedia
#~
#~ Requires:       %{name}-extras-base
#~
#~ %description    extras-kde
#~ This package contains Schrödinger's Cat supplemental wallpapers for Gnome
#~
#~ %package        extras-xfce
#~ Summary:        Extra Schrödinger's Cat Wallpapers for XFCE
#~ Group:          Applications/Multimedia
#~
#~ Requires:       %{name}-extras-base
#~
#~ %description    extras-xfce
#~ This package contains Schrödinger's Cat supplemental wallpapers for XFCE


%prep
%setup -q -n %{upstream_package}-%{version}

cp %{SOURCE1} default/normalish/schroedinger-cat-01-day.jpg
cp %{SOURCE2} default/standard/schroedinger-cat-01-day.jpg
cp %{SOURCE3} default/wide/schroedinger-cat-01-day.jpg

%build
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc

%files base
%doc CC-BY-SA-3.0 Attribution
%dir %{_datadir}/backgrounds/schroedinger-cat
%dir %{_datadir}/backgrounds/schroedinger-cat/default
%{_datadir}/backgrounds/schroedinger-cat/default/normalish
%{_datadir}/backgrounds/schroedinger-cat/default/standard
%{_datadir}/backgrounds/schroedinger-cat/default/wide
%{_datadir}/backgrounds/schroedinger-cat/default/schroedinger-cat.xml

%files animated
%dir %{_datadir}/backgrounds/schroedinger-cat/default-animated
%{_datadir}/backgrounds/schroedinger-cat/default-animated/normalish
%{_datadir}/backgrounds/schroedinger-cat/default-animated/standard
%{_datadir}/backgrounds/schroedinger-cat/default-animated/wide
%{_datadir}/backgrounds/schroedinger-cat/default-animated/schroedinger-cat.xml

%files kde
%{_kde4_datadir}/wallpapers/Schroedinger_Cat/

%files gnome
%{_datadir}/gnome-background-properties/schroedinger-cat-animated.xml

%files mate
%{_datadir}/mate-background-properties/schroedinger-cat-animated.xml

%files xfce
%{_datadir}/xfce4/backdrops/schroedinger-cat.jpg

#~ %files extras-base
#~ %doc CC-BY-SA-3.0 Attribution-Extras
#~ %{_datadir}/backgrounds/schroedinger-cat/extras/*.jpg
#~ %{_datadir}/backgrounds/schroedinger-cat/extras/schroedinger-cat-extras.xml
#~
#~ %files extras-gnome
#~ %{_datadir}/gnome-background-properties/schroedinger-cat-extras.xml
#~
#~ %files extras-kde
#~ %{_kde4_datadir}/wallpapers/Schroedinger_Cat_*/
#~
#~ %files extras-mate
#~ %{_datadir}/mate-background-properties/schroedinger-cat-extras.xml
#~
#~ %files extras-xfce
#~ %{_datadir}/xfce4/backdrops/*.jpg

%changelog
* Sun Mar 03 2013 Martin Sourada <mso@fedoraproject.org> - 18.90.0-1
- Initial rpm release
