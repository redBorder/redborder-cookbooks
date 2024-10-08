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
Requires: cookbook-snmp cookbook-rb-monitor cookbook-f2k cookbook-postgresql
Requires: cookbook-mongodb cookbook-rb-scanner
Requires: cookbook-minio cookbook-pmacct
Requires: cookbook-rb-dswatcher cookbook-rb-events-counter
Requires: cookbook-rsyslog cookbook-rb-cep
Requires: cookbook-rb-nmsp cookbook-n2klocd cookbook-rb-ale
Requires: cookbook-freeradius
Requires: cookbook-rb-proxy
Requires: cookbook-k2http
Requires: cookbook-rb-ips cookbook-snort cookbook-barnyard2
#Requires: cookbook-ohai
Requires: cookbook-cron
Requires: cookbook-rb-aioutliers
Requires: cookbook-rb-selinux
Requires: cookbook-rb-cgroup
Requires: cookbook-rb-logstatter
Requires: cookbook-rb-arubacentral
Requires: cookbook-rb-exporter
Requires: cookbook-rb-postfix
Requires: cookbook-rb-common
Requires: cookbook-keepalived
Requires: cookbook-rb-clamav
Requires: cookbook-rb-chrony
Requires: cookbook-mem2incident
Requires: cookbook-rb-ai
Requires: cookbook-rb-firewall

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build

%install

%post
case "$1" in
  1)
    # This is an initial install.
    :
  ;;
  2)
    # run the rb_upload_cookbooks script to avoid conflicts
    su - -s /bin/bash -c 'touch /root/.upload-cookbooks'
  ;;
esac

%files
%defattr(0644,root,root)
%doc LICENSE
%doc README.md

%changelog
* Tue Oct 08 2024 Nils Verschaeve <nverschaeve@redborder.com>
- Add firewall
* Tue Aug 27 2024 Miguel Álvarez <malvarez@redborder.com>
- Add chrony
* Wed Jul 24 2024 Pablo Pérez <pperez@redborder.com>
- Add rb-ai
* Tue Jul 16 2024 Miguel Negrón <manegron@redborder.com>
- Add mem2incident
* Tue Jun 18 2024 Miguel Álvarez <malvarez@redborder.com>
- Add clamav
* Mon Jun 10 2024 David Vanhoucke <dvanhoucke@redborder.com>
- Add keepalived
* Thu May 21 2024 Miguel Negrón <manegron@redborder.com>
- Add rb-common
* Mon May 20 2024 David Vanhoucke <dvanhoucke@redborder.com> - 1.1.0-1
- Add rb-postfix
* Fri Jan 19 2023 David Vanhoucke <dvanhoucke@redborder.com> - 1.0.7-1
- Add rb-arubacentral
* Mon Dec 18 2023 Miguel Álvarez <malvarez@redborder.com> - 1.0.6-1
- Add rb-logstatter
* Fri Dec 01 2023 David Vanhoucke <dvanhoucke@redborder.com> - 1.0.5-1
- Add selinux
* Wed Nov 29 2023 Miguel Álvarez <malvarez@redborder.com> - 1.0.4-1
- Add cgroup
* Wed Sep 27 2023 Miguel Álvarez <malvarez@redborder.com> - 1.0.3-1
- Added rbaioutliers cookbook
* Tue Apr 19 2022 Eduardo Reyes <eareyes@redborder.com> - 1.0.2-1
- Added cron cookbook
* Wed Mar 23 2022 Miguel Negron <manegrong@redborder.com> - 0.24-1
- Added rb-proxy cookbook
* Wed Feb 16 2022 Javier Rodriguez <javiercrg@redborder.com> - 0.12-1
- Added rb-nmsp cookbook
* Mon Jan 17 2022 Vicente Mesa <vimesa@redborder.com> - 0.12-1
- Added rb-nmsp cookbook
* Tue Dec 28 2021 Eduardo Reyes <eareyes@redborder.com> - 0.12-1
- Added rb-ale cookbook
* Fri Dec 17 2021 Eduardo Reyes <eareyes@redborder.com> - 0.12-1
- Added rb-nmsp cookbook
* Mon Dec 13 2021 Javier Rodriguez <javiercrg@redborder.com> - 0.12-1
- Added rb-scanner & mongodb cookbooks
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
