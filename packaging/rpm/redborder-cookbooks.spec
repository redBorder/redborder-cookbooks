Name: redborder-cookbooks
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Main package for redborder cookbooks

License: AGPL 3.0
URL: https://github.com/redBorder/redborder-cookbooks
Source0: %{name}-%{version}.tar.gz

Requires: cookbook-rb-manager cookbook-zookeeper cookbook-kafka cookbook-druid cookbook-http2k
Requires: cookbook-memcached cookbook-chef-server cookbook-consul cookbook-hadoop
Requires: cookbook-nginx cookbook-samza cookbook-geoip cookbook-webui cookbook-logstash
Requires: cookbook-snmp cookbook-rb-monitor cookbook-ntp cookbook-f2k cookbook-postgresql
Requires: cookbook-minio cookbook-pmacct
Requires: cookbook-dswatcher cookbook-events-counter
Requires: cookbook-iptables cookbook-rsyslog
Requires: cookbook-rb-social

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
* Thu Dec 2 2021 Vicente Mesa <vimesa@redborder.com> - 0.11-1
- Add rb-social cookbook
* Fri Feb 9 2018 Juan J. Prieto <jjprieto@redborder.com> - 0.11-1
- Add pmacct cookbook
* Wed Jan 31 2018 Alberto Rodriguez <arodriguez@redborder.com> - 0.10-1
- Add minio cookbook
* Mon Jan 29 2018 Juan J. Prieto <jjprieto@redborder.com> - 0.9-1
- Add logstash cookbook
* Fri Jan 20 2017 Carlos J. Mateos <cjmateos@redborder.com> - 0.8-1
- Added f2k cookbooks
* Fri Jan 13 2017 Carlos J. Mateos <cjmateos@redborder.com> - 0.7-1
- Added ntp cookbooks
* Wed Dec 21 2016 Alberto Rodriguez <arodriguez@redborder.com> - 0.6-1
- Added snmp and redborder-monitor cookbooks
* Thu Dec 15 2016 Carlos J. Mateos <cjmateos@redborder.com> - 0.5-1
- Added cookbooks webui
* Fri Dec 02 2016 Carlos J. Mateos <cjmateos@redborder.com> - 0.4-1
- Added cookbooks samza and geoip
* Thu Nov 17 2016 Juan J. Prieto <jjprieto@redborder.com> - 0.3-1
- Added cookbooks nginx
* Tue Oct 18 2016 Juan J. Prieto <jjprieto@redborder.com> - 0.2-1
- Added cookbooks required
* Tue Oct 11 2016 Juan J. Prieto <jjprieto@redborder.com> - 0.1-1
- first spec version
