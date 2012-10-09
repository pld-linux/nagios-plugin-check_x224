%define		plugin	check_x224
Summary:	Nagios plugin to check basic Remote Desktop connection success
Name:		nagios-plugin-%{plugin}
Version:	0.1
Release:	1
License:	BSD
Group:		Networking
Source0:	http://troels.arvin.dk/code/nagios/%{plugin}
# Source0-md5:	54852b2cfea127816743102404638b5f
Source1:	%{plugin}.cfg
URL:		http://exchange.nagios.org/directory/Plugins/Remote-Access/check_x224/details
BuildRequires:	rpm-pythonprov
Requires:	nagios-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
This plugin checks that the initial and most basic parts of a Remote
Desktop connection - the part which is specified by x224 - succeeds.
I.e., it does a bit more than a TCP connection test at port 3389.

%prep
%setup -qcT
%{__sed} -e '1s,^#!.*python,#!%{__python},' %{SOURCE0} > %{plugin}.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin}.py $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
