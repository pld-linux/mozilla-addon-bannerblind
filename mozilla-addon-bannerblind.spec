Summary:	Hide advertising banners
Summary(pl.UTF-8):	Ukrywanie paskudnych i denerwujących bannerów reklamowych
%define		_realname	bannerblind
Name:		mozilla-addon-%{_realname}
Version:	1.0rc1
Release:	5
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/bannerblind/%{_realname}.xpi
# Source0-md5:	5d33e45d4b95862841bdf6ae12a02a53
Source1:	%{_realname}-installed-chrome.txt
URL:		http://bannerblind.mozdev.org/
BuildRequires:	unzip
Requires(post,postun):	mozilla >= 5:1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 2:1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
Plugin that hides advertising banners. It allows you to define your
own unwanted banner dimensions.

%description -l pl.UTF-8
Ukrywa paskudne i denerwujące bannery reklamowe. Można definiować
własne rozmiary banerów do ukrycia.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
	%{_sbindir}/mozilla-chrome+xpcom-generate
fi

%postun
[ ! -x %{_sbindir}/mozilla-chrome+xpcom-generate ] || %{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
