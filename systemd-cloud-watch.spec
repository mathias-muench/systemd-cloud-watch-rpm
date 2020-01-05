%global commit             991dfaad1526f2977b9d09cd1e9421f3b9d9e919
%global commitdate         20170224
%global shortcommit        %(c=%{commit}; echo ${c:0:7})

%define debug_package %{nil}

Name: systemd-cloud-watch
Version: 0
Release: 0.4.%{commitdate}git%{shortcommit}%{?dist}
Summary: FIXME
License: FIXME

BuildRequires: golang git systemd-devel

Source0: https://github.com/marcogroppo/%{name}/archive/%{commit}.tar.gz

%description

%prep
%setup -n %{name}-%{commit}

%build
cat >systemd-cloud-watch.service <<'EOF'
[Unit]
Description=systemd-cloud-watch
Wants=basic.target
After=basic.target network-online.target

[Service]
EnvironmentFile=/etc/environment
User=root
Nice=4
OOMScoreAdjust=400
ExecStart=/usr/bin/systemd-cloud-watch /etc/systemd-cloud-watch.conf
KillMode=process
Restart=on-failure
RestartSec=42s

[Install]
WantedBy=multi-user.target
EOF

export GOPATH=$PWD/_build
%{__mkdir_p} $GOPATH/src
%{__ln_s} $PWD/cloud-watch/ $GOPATH/src/cloud-watch
%{__ln_s} $PWD $GOPATH/src/systemd-cloud-watch
cd $GOPATH/src
go get -v ./cloud-watch
go get -v ./systemd-cloud-watch

%install
%{__install} -D -m 755 _build/bin/systemd-cloud-watch %{buildroot}/%{_bindir}/systemd-cloud-watch
%{__install} -D -m 644 _build/systemd-cloud-watch.service %{buildroot}/usr/lib/systemd/system/systemd-cloud-watch.service

%files
%attr(0755,root,root) /%{_bindir}/systemd-cloud-watch
%attr(0644,root,root) /%{_usr}/lib/systemd/system/systemd-cloud-watch.service
