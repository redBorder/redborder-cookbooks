Name: redborder-cookbooks
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Main package for redborder cookbooks

License: AGPL 3.0
URL: https://github.com/redBorder/redborder-cookbooks
Source0: %{name}-%{version}.tar.gz

Requires: cookbook-rb-manager cookbook-zookeeper cookbook-kafka cookbook-druid cookbook-http2k
Requires: cookbook-cron cookbook-memcached cookbook-chef-server cookbook-consul cookbook-hadoop
Requires: cookbook-nginx

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build

%install

%files
%defattr(0644,root,root)
%doc LICENSE
%doc README.md

%changelog
* Thu Nov 17 2016 Juan J. Prieto <jjprieto@redborder.com> - 0.3-1
- Added cookbooks nginx
* Tue Oct 18 2016 Juan J. Prieto <jjprieto@redborder.com> - 0.2-1
- Added cookbooks required
* Tue Oct 11 2016 Juan J. Prieto <jjprieto@redborder.com> - 0.1-1
- first spec version
