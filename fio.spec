#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fio
Version  : fio
Release  : 8
URL      : https://github.com/axboe/fio/archive/fio-2.10.tar.gz
Source0  : https://github.com/axboe/fio/archive/fio-2.10.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: fio-bin
Requires: fio-data
Requires: fio-doc
BuildRequires : libaio-dev
Patch1: build.patch

%description
fio
---
fio is a tool that will spawn a number of threads or processes doing a
particular type of io action as specified by the user. fio takes a
number of global parameters, each inherited by the thread unless
otherwise parameters given to them overriding that setting is given.
The typical use of fio is to write a job file matching the io load
one wants to simulate.

%package bin
Summary: bin components for the fio package.
Group: Binaries
Requires: fio-data

%description bin
bin components for the fio package.


%package data
Summary: data components for the fio package.
Group: Data

%description data
data components for the fio package.


%package doc
Summary: doc components for the fio package.
Group: Documentation

%description doc
doc components for the fio package.


%prep
%setup -q -n fio-fio-2.10
%patch1 -p1

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fio
/usr/bin/fio-btrace2fio
/usr/bin/fio-dedupe
/usr/bin/fio-genzipf
/usr/bin/fio-verify-state
/usr/bin/fio2gnuplot
/usr/bin/fio_generate_plots
/usr/bin/fiologparser.py
/usr/bin/genfio

%files data
%defattr(-,root,root,-)
/usr/share/fio/graph2D.gpm
/usr/share/fio/graph3D.gpm
/usr/share/fio/math.gpm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
