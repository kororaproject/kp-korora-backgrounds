%define u_name schroedinger-cat
%define u_package schroedinger-cat-backgrounds

Name:           korora-backgrounds
Version:        18.90.0
Release:        1%{?dist}
Summary:        Korora desktop backgrounds

Group:          Applications/Multimedia
License:        CC-BY-SA
URL:            https://fedoraproject.org/wiki/F19_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{u_package}-%{version}.tar.xz
Source1:        korora-background-dawn-normalish.jpg
Source2:        korora-background-dawn-standard.jpg
Source3:        korora-background-dawn-wide.jpg
Source4:        korora-background-day-normalish.jpg
Source5:        korora-background-day-standard.jpg
Source6:        korora-background-day-wide.jpg
Source7:        korora-background-dusk-normalish.jpg
Source8:        korora-background-dusk-standard.jpg
Source9:        korora-background-dusk-wide.jpg
Source10:       korora-background-night-normalish.jpg
Source11:       korora-background-night-standard.jpg
Source12:       korora-background-night-wide.jpg

Provides:       %{u_package}
Obsoletes:      %{u_package}

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
Provides:       %{u_package}-base
Obsoletes:      %{u_package}-base

%description    base
This package contains base images for Schrödinger's Cat Backgrounds.

%package        animated
Summary:        Time of day images for Schrödinger's Cat Backgrounds
Group:          Applications/Multimedia
Provides:       %{u_package}-animated
Obsoletes:      %{u_package}-animated

Requires:       %{name}-base = %{version}-%{release}

%description    animated
This package contains the time of day images for Korora backgrounds

%package        kde
Summary:        Korora Wallpapers for KDE
Group:          Applications/Multimedia
Provides:       %{u_package}-kde
Obsoletes:      %{u_package}-kde

Requires:       %{name}-base = %{version}-%{release}
Requires:       kde-filesystem

%description    kde
This package contains KDE desktop wallpapers for the Korora
theme.

%package        gnome
Summary:        Korora Wallpapers for Gnome
Group:          Applications/Multimedia
Provides:       %{u_package}-gnome
Obsoletes:      %{u_package}-gnome

Requires:       %{name}-animated = %{version}-%{release}

%description    gnome
This package contains Gnome desktop wallpapers for the Korora
theme.

%package        mate
Summary:        Schrödinger's Cat Wallpapers for Mate
Group:          Applications/Multimedia
Provides:       %{u_package}-mate
Obsoletes:      %{u_package}-mate

Requires:       %{name}-animated = %{version}-%{release}

%description    mate
This package contains Mate desktop wallpapers for the Korora theme.


%package        xfce
Summary:        Schrödinger's Cat Wallpapers for XFCE4
Group:          Applications/Multimedia
Provides:       %{u_package}-xfce
Obsoletes:      %{u_package}-xfce

Requires:       %{name}-base = %{version}-%{release}

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
%setup -q -n %{u_package}-%{version}

cp %{SOURCE1} default/normalish/%{u_name}-00-dawn.jpg
cp %{SOURCE2} default/standard/%{u_name}-00-dawn.jpg
cp %{SOURCE3} default/wide/%{u_name}-00-dawn.jpg

cp %{SOURCE4} default/normalish/%{u_name}-01-day.jpg
cp %{SOURCE5} default/standard/%{u_name}-01-day.jpg
cp %{SOURCE6} default/wide/%{u_name}-01-day.jpg

cp %{SOURCE7} default/normalish/%{u_name}-02-dusk.jpg
cp %{SOURCE8} default/standard/%{u_name}-02-dusk.jpg
cp %{SOURCE9} default/wide/%{u_name}-02-dusk.jpg

cp %{SOURCE10} default/normalish/%{u_name}-03-night.jpg
cp %{SOURCE11} default/standard/%{u_name}-03-night.jpg
cp %{SOURCE12} default/wide/%{u_name}-03-night.jpg


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
