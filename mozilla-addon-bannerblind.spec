Summary:        Hide advertising banners
Summary(pl):    Ukryj paskudne i denerwuj±ce bannery reklamowe
Name:           mozilla-addon-bannerblind
Version:        1.0rc1
Release:        1
License:        GPL
Group:          X11/Applications/Networking
Source0:        http://downloads.mozdev.org/bannerblind/bannerblind.xpi
Source1:        bannerblind-installed-chrome.txt
URL:            http://bannerblind.mozdev.org
BuildRequires:  unzip
Requires:       mozilla >= 1.0
BuildRoot:      %{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _chromedir      %{_libdir}/mozilla/chrome
%define		_realname	bannerblind

%description
Hide advertising banners
%description -l pl
Ukryj paskudne i denerwuj±ce bannery reklamowe. Mo¿na definiowaæ w³asne
rozmiary banerów do ukrycia.

%prep
%setup -q -c -T
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}
unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_chromedir}
cat %{_realname}-installed-chrome.txt >> installed-chrome.txt

%postun
cd %{_chromedir}
cat installed-chrome.txt |grep -v "bannerblind.jar" > installed-chrome.txt.tmp
cat installed-chrome.txt.tmp > installed-chrome.txt
rm -f installed-chrome.txt.tmp

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
