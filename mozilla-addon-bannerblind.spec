Summary:        Hide advertising banners
Summary(pl):    Ukryj paskudne i denerwuj±ce bannery reklamowe
Name:           mozilla-addon-bannerblind
%define		_realname	bannerblind
Version:        1.0rc1
Release:        2
License:        GPL
Group:          X11/Applications/Networking
Source0:        http://downloads.mozdev.org/bannerblind/%{_realname}.xpi
Source1:        %{_realname}-installed-chrome.txt
URL:            http://bannerblind.mozdev.org/
BuildRequires:  unzip
BuildArch:	noarch
Requires:	mozilla >= 1.0-7
BuildRoot:      %{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
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

%post
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
