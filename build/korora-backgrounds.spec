%define u_name heisenbug
%define U_name Heisenbug
%define u_package heisenbug-backgrounds

Name:           korora-backgrounds
Version:        19.90.0
Release:        1%{?dist}
Summary:        Korora desktop backgrounds

Group:          Applications/Multimedia
License:        CC-BY-SA
URL:            https://fedoraproject.org/wiki/F19_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{u_package}-%{version}.tar.xz
Source1:        korora-background-dawn-normalish.png
Source2:        korora-background-dawn-standard.png
Source3:        korora-background-dawn-wide.png
Source4:        korora-background-dawn-tv-wide.png
Source5:        korora-background-day-normalish.png
Source6:        korora-background-day-standard.png
Source7:        korora-background-day-wide.png
Source8:        korora-background-day-tv-wide.png
Source9:        korora-background-dusk-normalish.png
Source10:       korora-background-dusk-standard.png
Source11:       korora-background-dusk-wide.png
Source12:       korora-background-dusk-tv-wide.png
Source13:       korora-background-night-normalish.png
Source14:       korora-background-night-standard.png
Source15:       korora-background-night-wide.png
Source16:       korora-background-night-tv-wide.png
Patch0:         korora-uses-day-as-default.patch

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
Pulls in themes for GNOME, KDE, Mate and Xfce desktops.

%package        base
Summary:        Base images for Korora Backgrounds
Group:          Applications/Multimedia
License:        CC-BY-SA
Provides:       %{u_package}-base
Obsoletes:      %{u_package}-base

%description    base
This package contains base images for Korora Backgrounds

#%package        animated
#Summary:        Time of day images for Korora Backgrounds
#Group:          Applications/Multimedia
#Provides:       %{u_package}-animated
#Obsoletes:      %{u_package}-animated
#
#Requires:       %{name}-base = %{version}-%{release}
#
#%description    animated
#This package contains the time of day images for Korora backgrounds

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

Requires:       %{name}-base = %{version}-%{release}

%description    gnome
This package contains Gnome/Cinnamon desktop wallpapers for the
Korora theme.

%package        mate
Summary:        Korora Wallpapers for Mate
Group:          Applications/Multimedia
Provides:       %{u_package}-mate
Obsoletes:      %{u_package}-mate

Requires:       %{name}-base = %{version}-%{release}

%description    mate
This package contains Mate desktop wallpapers for the Korora theme.


%package        xfce
Summary:        Korora Wallpapers for XFCE4
Group:          Applications/Multimedia
Provides:       %{u_package}-xfce
Obsoletes:      %{u_package}-xfce

Requires:       %{name}-base = %{version}-%{release}
Requires:       xfdesktop

%description    xfce
This package contains XFCE4 desktop wallpapers for the Korora
theme.

#%package        extras-base
#Summary:        Base images for Korora Extras Backrounds
#Group:          Applications/Multimedia
#License:        CC-BY and CC-BY-SA
#Provides:       %{u_package}-extras-base
#Obsoletes:      %{u_package}-extras-base
#
#%description    extras-base
#This package contains base images for Korora supplemental
#wallpapers.
#
#%package        extras-gnome
#Summary:        Extra Korora Wallpapers for Gnome and Cinnamon
#Group:          Applications/Multimedia
#Provides:       %{u_package}-extras-gnome
#Obsoletes:      %{u_package}-extras-gnome
#
#Requires:       %{name}-extras-base
#
#%description    extras-gnome
#This package contains Korora supplemental wallpapers for Gnome
#and Cinnamon
#
#%package        extras-mate
#Summary:        Extra Korora Wallpapers for Mate
#Group:          Applications/Multimedia
#Provides:       %{u_package}-extras-mate
#Obsoletes:      %{u_package}-extras-mate
#
#Requires:       %{name}-extras-base
#
#%description    extras-mate
#This package contains Korora supplemental wallpapers for Mate
#
#%package        extras-kde
#Summary:        Extra Korora Wallpapers for KDE
#Group:          Applications/Multimedia
#Provides:       %{u_package}-extras-kde
#Obsoletes:      %{u_package}-extras-kde
#
#Requires:       %{name}-extras-base
#
#%description    extras-kde
#This package contains Korora supplemental wallpapers for Gnome
#
#%package        extras-xfce
#Summary:        Extra Korora Wallpapers for XFCE
#Group:          Applications/Multimedia
#Provides:       %{u_package}-extras-xfce
#Obsoletes:      %{u_package}-extras-xfce
#
#Requires:       %{name}-extras-base
#
#%description    extras-xfce
#This package contains Korora supplemental wallpapers for XFCE
#

%prep
%setup -q -n %{u_package}-%{version}

cp %{SOURCE5}  default/normalish/%{u_name}.png
cp %{SOURCE6}  default/standard/%{u_name}.png
cp %{SOURCE7}  default/wide/%{u_name}.png
cp %{SOURCE8}  default/tv-wide/%{u_name}.png

cp %{SOURCE1}  default/normalish/%{u_name}-00-dawn.png
cp %{SOURCE2}  default/standard/%{u_name}-00-dawn.png
cp %{SOURCE3}  default/wide/%{u_name}-00-dawn.png
cp %{SOURCE4}  default/tv-wide/%{u_name}.png

cp %{SOURCE5}  default/normalish/%{u_name}-01-day.png
cp %{SOURCE6}  default/standard/%{u_name}-01-day.png
cp %{SOURCE7}  default/wide/%{u_name}-01-day.png
cp %{SOURCE8}  default/tv-wide/%{u_name}.png

cp %{SOURCE9}  default/normalish/%{u_name}-02-dusk.png
cp %{SOURCE10} default/standard/%{u_name}-02-dusk.png
cp %{SOURCE11} default/wide/%{u_name}-02-dusk.png
cp %{SOURCE12} default/tv-wide/%{u_name}.png

cp %{SOURCE13} default/normalish/%{u_name}-03-night.png
cp %{SOURCE14} default/standard/%{u_name}-03-night.png
cp %{SOURCE15} default/wide/%{u_name}-03-night.png
cp %{SOURCE16} default/tv-wide/%{u_name}-03-night.png

#%patch0 -p1


%build
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc

%files base
%doc CC-BY-SA-3.0 Attribution
%dir %{_datadir}/backgrounds/%{u_name}
%dir %{_datadir}/backgrounds/%{u_name}/default
%{_datadir}/backgrounds/%{u_name}/default/normalish
%{_datadir}/backgrounds/%{u_name}/default/standard
%{_datadir}/backgrounds/%{u_name}/default/wide
%{_datadir}/backgrounds/%{u_name}/default/tv-wide
%{_datadir}/backgrounds/%{u_name}/default/%{u_name}.xml

#%files animated
#%dir %{_datadir}/backgrounds/%{u_name}/default-animated
#%{_datadir}/backgrounds/%{u_name}/default-animated/normalish
#%{_datadir}/backgrounds/%{u_name}/default-animated/standard
#%{_datadir}/backgrounds/%{u_name}/default-animated/wide
#%{_datadir}/backgrounds/%{u_name}/default-animated/%{u_name}.xml

%files kde
%{_kde4_datadir}/wallpapers/%{U_name}/

%files gnome
%{_datadir}/gnome-background-properties/%{u_name}.xml

%files mate
%{_datadir}/mate-background-properties/%{u_name}.xml

%files xfce
%{_datadir}/xfce4/backdrops/%{u_name}.png

#%files extras-base
#%doc CC-BY-SA-3.0 CC-BY-3.0 Attribution-Extras
#%{_datadir}/backgrounds/%{u_name}/extras/*.jpg
#%{_datadir}/backgrounds/%{u_name}/extras/*.png
#%{_datadir}/backgrounds/%{u_name}/extras/%{u_name}-extras.xml
#
#%files extras-gnome
#%{_datadir}/gnome-background-properties/%{u_name}-extras.xml
#
#%files extras-kde
#%{_kde4_datadir}/wallpapers/%{U_name}_*/
#
#%files extras-mate
#%{_datadir}/mate-background-properties/%{u_name}-extras.xml
#
#%files extras-xfce
#%{_datadir}/xfce4/backdrops/*.jpg
#%{_datadir}/xfce4/backdrops/*.png
#
%changelog
* Mon Sep 09 2013 Martin Sourada <mso@fedoraproject.org> - 19.90.0-1
- Initial rpm release
