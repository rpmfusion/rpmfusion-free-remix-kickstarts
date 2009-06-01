Name:       rpmfusion-free-remix-kickstarts
# we follow the spin-kickstarts version scheme as the files in this 
# package highly depend on them anyway
Version:    0.11.1
Release:    5%{?dist}
Summary:    Kickstart files for creating distributions with packages RPM Fusion free

Group:      Applications/System
License:    GPLv3+
URL:        http://rpmfusion.org/remix-kickstarts
Source1:    rpmfusion-remix-kickstarts-README
Source2:    rpmfusion-remix-kickstarts-COPYING
Source10:   rpmfusion-free-live-base.ks
Source11:   rpmfusion-free-livecd-desktop.ks
Source12:   rpmfusion-free-livecd-kde.ks
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

Requires:   spin-kickstarts >= %{version}

%description
A number of kickstarts files you can use to create a Linux distribution or 
a Fedora Remix with packages from RPM Fusion. Please remember to read the 
README file if you want to distribute what you made with tools that used
these kickstart files!

%prep
echo "nothing to setup"

%build
echo "nothing to build"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/
install -p -m644 %{SOURCE1} README
install -p -m644 %{SOURCE2} COPYING
install -t $RPM_BUILD_ROOT%{_datadir}/%{name}/ -p -m644 \
  %{SOURCE10}  \
  %{SOURCE11}  \
  %{SOURCE12}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_datadir}/%{name}/

%changelog
* Mon Jun 01 2009 Thorsten Leemhuis <fedora at leemhuis dot info > 0.11.1-5
- add disabled repo definitions for f11 release

* Sun May 17 2009 Thorsten Leemhuis <fedora at leemhuis dot info > 0.11.1-3
- rename to rpmfusion-free-remix-kickstarts and only include free bits

* Wed May 13 2009 Thorsten Leemhuis <fedora at leemhuis dot info > 0.11.1-2
- package is GPLv3, not v2+
- s/remixes/remix/
- add a note about the version scheme

* Fri May 01 2009 Thorsten Leemhuis <fedora at leemhuis dot info > 0.11.1-1
- initial version, based on spin-kickstarts from Fedora
