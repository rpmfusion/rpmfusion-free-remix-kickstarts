# Make sure you read /usr/share/doc/rpmfusion-spins-kickstart*/README before
# distributing a linux distribution that is build with this kickstart file
#
%include ../spin-kickstarts/fedora-livecd-desktop.ks
%include rpmfusion-free-live-base.ks

%packages
## RPM Fusion packages normally come via comps.xml, but to fit space
## constraints do some small adjustments:
#
# big, lots of deps:
-gnome-mplayer 
%end
