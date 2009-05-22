# Make sure you read /usr/share/doc/rpmfusion-spins-kickstart*/README before
# distributing a linux distribution that is build with this kickstart file

# enable and use RPM Fusion free
repo --name=rpmfusion-free-rawhide --mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-rawhide&arch=$basearch

%packages
# unbrand:
-fedora-release
-fedora-logos
-fedora-release-notes
generic-release
generic-logos
generic-release-notes

## RPM Fusion packages normally come via comps.xml, some adjustments below this line
#
# "best hardware support by default" would be nice, but space is limited:
-foo2hiperc
-foo2hp
-foo2lava
-foo2qpdl
-foo2slx
-foo2xqx
-foo2zjs
%end

%post
echo "== RPM Fusion Free: Base section =="
echo "Importing RPM Fusion keys"
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-*-primary
echo "List of packages from RPM Fusion Free:"
rpm -qa --qf '%{NAME} %{SIGGPG:pgpsig} %{SIGPGP:pgpsig} \n' | grep -e 855099b249c8885a -e ad2708448fcff4da | awk ' { print $1 } ' | sort
echo "List of incuded RPM Fusion packages with their size:"
rpm -q --qf '%{SIZE} %{NAME}\n' $(rpm -qa --qf '%{NAME} %{SIGGPG:pgpsig} %{SIGPGP:pgpsig} \n' | grep -e 855099b249c8885a -e ad2708448fcff4da | awk ' { print $1 } ') | sort -n
echo
%end

