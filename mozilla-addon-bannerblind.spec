Summary:        Hide advertising banners
Summary(pl):    Ukryj paskudne i denerwuj±ce bannery reklamowe
Name:           mozilla-addon-bannerblind
%define		_realname	bannerblind
Version:        1.0rc1
Release:        3
License:        GPL
Group:          X11/Applications/Networking
Source0:        http://downloads.us-east1.mozdev.org/bannerblind/%{_realname}.xpi
# Source0-md5:	5d33e45d4b95862841bdf6ae12a02a53
Source1:        %{_realname}-installed-chrome.txt
URL:            http://bannerblind.mozdev.org/
BuildRequires:  unzip
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
BuildArch:	noarch
BuildRoot:      %{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _chromedir      %{_libdir}/mozilla/chrome

%description
Plugin that hides advertising banners. It allows you to define your
own unwanted banner dimensions.

%description -l pl
Ukryj paskudne i denerwuj±ce bannery reklamowe. Mo¿na definiowaæ w³asne
rozmiary banerów do ukrycia.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
