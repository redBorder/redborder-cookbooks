Name: redborder-cookbooks
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Main package for redborder cookbooks

License: AGPL 3.0
URL: https://github.com/redBorder/redborder-cookbooks
Source0: %{name}-%{version}.tar.gz

Requires: cookbook-rb-manager cookbook-zookeeper cookbook-kafka cookbook-druid cookbook-http2k
Requires: cookbook-memcached cookbook-chef-server cookbook-consul
Requires: cookbook-nginx cookbook-geoip cookbook-webui cookbook-logstash
Requires: cookbook-snmp cookbook-rb-monitor cookbook-f2k cookbook-postgresql
Requires: cookbook-mongodb cookbook-rb-scanner
Requires: cookbook-minio cookbook-pmacct
Requires: cookbook-rb-dswatcher cookbook-rb-events-counter
Requires: cookbook-rsyslog cookbook-rb-cep
Requires: cookbook-rb-nmsp cookbook-n2klocd cookbook-rb-ale
Requires: cookbook-freeradius
Requires: cookbook-rb-proxy
Requires: cookbook-k2http
Requires: cookbook-rb-ips cookbook-rb-intrusion cookbook-snort3 cookbook-snort cookbook-barnyard2
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
* Fri Oct 11 2024 Miguel Negrón <manegron@redborder.com>
- Remove hadoop and samza

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

* Mon May 20 2024 David Vanhoucke <dvanhoucke@redborder.com>
- Add rb-postfix

* Fri Jan 19 2023 David Vanhoucke <dvanhoucke@redborder.com>
- Add rb-arubacentral

* Mon Dec 18 2023 Miguel Álvarez <malvarez@redborder.com>
- Add rb-logstatter

* Fri Dec 01 2023 David Vanhoucke <dvanhoucke@redborder.com>
- Add selinux

* Wed Nov 29 2023 Miguel Álvarez <malvarez@redborder.com>
- Add cgroup

* Wed Sep 27 2023 Miguel Álvarez <malvarez@redborder.com>
- Added rbaioutliers cookbook

* Tue Apr 19 2022 Eduardo Reyes <eareyes@redborder.com>
- Added cron cookbook

* Wed Mar 23 2022 Miguel Negron <manegrong@redborder.com>
- Added rb-proxy cookbook

* Wed Feb 16 2022 Javier Rodriguez <javiercrg@redborder.com>
- Added rb-nmsp cookbook

* Mon Jan 17 2022 Vicente Mesa <vimesa@redborder.com>
- Added rb-nmsp cookbook

* Tue Dec 28 2021 Eduardo Reyes <eareyes@redborder.com>
- Added rb-ale cookbook

* Fri Dec 17 2021 Eduardo Reyes <eareyes@redborder.com>
- Added rb-nmsp cookbook

* Mon Dec 13 2021 Javier Rodriguez <javiercrg@redborder.com>
- Added rb-scanner & mongodb cookbooks

* Thu Dec 2 2021 Vicente Mesa <vimesa@redborder.com>
- Add rb-social cookbook

* Fri Feb 9 2018 Juan J. Prieto <jjprieto@redborder.com>
- Add pmacct cookbook

* Wed Jan 31 2018 Alberto Rodriguez <arodriguez@redborder.com>
- Add minio cookbook

* Mon Jan 29 2018 Juan J. Prieto <jjprieto@redborder.com>
- Add logstash cookbook

* Fri Jan 20 2017 Carlos J. Mateos <cjmateos@redborder.com>
- Added f2k cookbooks

* Fri Jan 13 2017 Carlos J. Mateos <cjmateos@redborder.com>
- Added ntp cookbooks

* Wed Dec 21 2016 Alberto Rodriguez <arodriguez@redborder.com>
- Added snmp and redborder-monitor cookbook

* Thu Dec 15 2016 Carlos J. Mateos <cjmateos@redborder.com>
- Added cookbooks webui

* Fri Dec 02 2016 Carlos J. Mateos <cjmateos@redborder.com>
- Added cookbooks samza and geoip

* Thu Nov 17 2016 Juan J. Prieto <jjprieto@redborder.com>
- Added cookbooks nginx

* Tue Oct 18 2016 Juan J. Prieto <jjprieto@redborder.com>
- Added cookbooks required

* Tue Oct 11 2016 Juan J. Prieto <jjprieto@redborder.com>
- first spec version
