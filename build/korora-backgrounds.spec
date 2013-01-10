%define upstream_package spherical-cow-backgrounds

Name:           korora-backgrounds
Version:        17.92.0
Release:        1%{?dist}
Summary:        Korora desktop backgrounds

Group:          Applications/Multimedia
License:        CC-BY-SA
URL:            https://fedoraproject.org/wiki/F18_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{upstream_package}-%{version}.tar.xz
Source1:        korora-background-normalish.png
Source2:        korora-background-standard.png
Source3:        korora-background-wide.png

Provides:       %{upstream_package}
Obsoletes:      %{upstream_package}

BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires:  kde-filesystem
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}


%description
This package contains desktop backgrounds for the Korora theme.
Pulls in both Gnome and KDE themes.

%package        single
Summary:        Single screen images for Korora Backgrounds
Group:          Applications/Multimedia
License:        CC-BY-SA

%description    single
This package contains single screen images for Korora
Backgrounds.

%package        kde
Summary:        Korora Wallpapers for KDE
Group:          Applications/Multimedia

Requires:       %{name}-single = %{version}-%{release}
Requires:       kde-filesystem

%description    kde
This package contains KDE desktop wallpapers for the Korora
theme.

%package        gnome
Summary:        Korora Wallpapers for Gnome
Group:          Applications/Multimedia

Requires:       %{name}-single = %{version}-%{release}

%description    gnome
This package contains Gnome desktop wallpapers for the Korora
theme.

%package        xfce
Summary:        Korora Wallpapers for XFCE4
Group:          Applications/Multimedia

Requires:       %{name}-single = %{version}-%{release}
Requires:       xfdesktop

%description    xfce
This package contains XFCE4 desktop wallpapers for the Korora
theme.

%package        extras-single
Summary:        Single screen images for Korora Extras Backrounds
Group:          Applications/Multimedia
License:        CC-BY and CC-BY-SA

%description    extras-single
This package contains single screen images for Korora supplemental
wallpapers.

%package        extras-gnome
Summary:        Extra Korora Wallpapers for Gnome
Group:          Applications/Multimedia

Requires:       %{name}-extras-single

%description    extras-gnome
This package contains Korora supplemental wallpapers for Gnome

%package        extras-kde
Summary:        Extra Korora Wallpapers for KDE
Group:          Applications/Multimedia

Requires:       %{name}-extras-single

%description    extras-kde
This package contains Korora supplemental wallpapers for Gnome

%package        extras-xfce
Summary:        Extra Korora Wallpapers for XFCE
Group:          Applications/Multimedia

Requires:       %{name}-extras-single

%description    extras-xfce
This package contains Korora supplemental wallpapers for XFCE


%prep
%setup -q -n %{upstream_package}-%{version}

echo -e "\n\n\n\n\n\n\n"
pwd
echo -e "\n\n\n\n\n\n\n"

cp %{SOURCE1} default/normalish/spherical-cow-02-noon.png
cp %{SOURCE2} default/standard/spherical-cow-02-noon.png
cp %{SOURCE3} default/wide/spherical-cow-02-noon.png

%build
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc

%files single
%doc CC-BY-SA\ 3.0 Attribution
%dir %{_datadir}/backgrounds/spherical-cow
%dir %{_datadir}/backgrounds/spherical-cow/default
%{_datadir}/backgrounds/spherical-cow/default/normalish
%{_datadir}/backgrounds/spherical-cow/default/standard
%{_datadir}/backgrounds/spherical-cow/default/wide

%files kde
%{_kde4_datadir}/wallpapers/Spherical_Cow/

%files gnome
%{_datadir}/backgrounds/spherical-cow/default/spherical-cow.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-spherical-cow.xml

%files xfce
%{_datadir}/xfce4/backdrops/spherical-cow.png

%files extras-single
%doc CC-BY-SA\ 3.0 CC-BY-SA\ 2.0 CC-BY\ 2.0 Attribution-Extras
%{_datadir}/backgrounds/spherical-cow/extras/*.jpg

%files extras-gnome
%{_datadir}/backgrounds/spherical-cow/extras/spherical-cow-extras.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-spherical-cow-extras.xml

%files extras-kde
%{_kde4_datadir}/wallpapers/Spherical_Cow_*/

%files extras-xfce
%{_datadir}/xfce4/backdrops/*.jpg

%changelog
* Tue Sep 25 2012 Martin Sourada <mso@fedoraproject.org> - 17.92.0-1
- Add extras

* Tue Aug 14 2012 Martin Sourada <mso@fedoraproject.org> - 17.91.0-2
- Spec cleanup WRT changes to guideline since we first released
  backgrounds package...

* Sun Aug 12 2012 Martin Sourada <mso@fedoraproject.org> - 17.91.0-1
- Updated design

* Sat Aug 11 2012 Martin Sourada <mso@fedoraproject.org> - 17.90.2-1
- Another iteration

* Fri Aug 10 2012 Martin Sourada <mso@fedoraproject.org> - 17.90.1-1
- First release
