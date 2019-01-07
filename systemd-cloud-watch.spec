%global commit             991dfaad1526f2977b9d09cd1e9421f3b9d9e919
%global commitdate         20170224
%global shortcommit        %(c=%{commit}; echo ${c:0:7})

Name: systemd-cloud-watch
Version: 0
Release: 0.3.%{commitdate}git%{shortcommit}%{?dist}
Summary: FIXME
License: FIXME

BuildRequires: golang git systemd-devel

Source0: https://github.com/marcogroppo/%{name}/archive/%{commit}.tar.gz

%description

%prep
%setup -n %{name}-%{commit}

%build
export GOPATH=$PWD/_build
%{__mkdir_p} $GOPATH/src
%{__ln_s} $PWD/cloud-watch/ $GOPATH/src/cloud-watch
%{__ln_s} $PWD $GOPATH/src/systemd-cloud-watch
cd $GOPATH/src
go get -v ./cloud-watch
go get -v ./systemd-cloud-watch

%install
%{__install} -D -m 755 _build/bin/systemd-cloud-watch %{buildroot}/%{_bindir}/systemd-cloud-watch

%files
%attr(0755,root,root) /%{_bindir}/systemd-cloud-watch
