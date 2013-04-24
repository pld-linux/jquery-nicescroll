%define		plugin	nicescroll
Summary:	jQuery NiceScroll plugin - scrolling for desktop, mobile and touch devices
Name:		jquery-%{plugin}
Version:	3.4.0
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	https://jquery-nicescroll.googlecode.com/files/jquery.nicescroll.340.zip
# Source0-md5:	de8bf8ba21a3fad9517c8bec803d6ab3
URL:		http://areaaperta.com/nicescroll/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
Requires:	jquery >= 1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
This library allows you to create Class-like functions in an very
effective and nice way.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p jquery.%{plugin}.min.js  $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js
cp -p zoomico.png $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README MIT.LICENSE changelog_*.txt
%{_appdir}
