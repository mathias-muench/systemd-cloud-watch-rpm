spec=systemd-cloud-watch.spec
outdir=$(shell rpm --eval '%{_srcrpmdir}')
root=fedora-31-x86_64

srpm:
	rpmbuild --undefine=_disable_source_fetch --define='_srcrpmdir $(outdir)' -bs $(spec)

rpm:
	rpmbuild --undefine=_disable_source_fetch --define='_srcrpmdir $(outdir)' -bb $(spec)

mock: srpm
	mock -N --root $(root) --enable-network --rebuild $(outdir)/$(shell rpmspec -q --srpm $(spec) | sed 's/\.[^.]*$$/.src.rpm/')
