#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fio
Version  : 3.27
Release  : 57
URL      : https://github.com/axboe/fio/archive/fio-3.27/fio-3.27.tar.gz
Source0  : https://github.com/axboe/fio/archive/fio-3.27/fio-3.27.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: fio-bin = %{version}-%{release}
Requires: fio-data = %{version}-%{release}
Requires: fio-license = %{version}-%{release}
Requires: fio-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : flex
BuildRequires : libaio-dev
BuildRequires : numactl-dev
BuildRequires : pkg-config
BuildRequires : zlib-dev
Patch1: build.patch

%description
Overview and history
--------------------
Fio was originally written to save me the hassle of writing special test case
programs when I wanted to test a specific workload, either for performance
reasons or to find/reproduce a bug. The process of writing such a test app can
be tiresome, especially if you have to do it often.  Hence I needed a tool that
would be able to simulate a given I/O workload without resorting to writing a
tailored test case again and again.

%package bin
Summary: bin components for the fio package.
Group: Binaries
Requires: fio-data = %{version}-%{release}
Requires: fio-license = %{version}-%{release}

%description bin
bin components for the fio package.


%package data
Summary: data components for the fio package.
Group: Data

%description data
data components for the fio package.


%package extras
Summary: extras components for the fio package.
Group: Default

%description extras
extras components for the fio package.


%package license
Summary: license components for the fio package.
Group: Default

%description license
license components for the fio package.


%package man
Summary: man components for the fio package.
Group: Default

%description man
man components for the fio package.


%prep
%setup -q -n fio-fio-3.27
cd %{_builddir}/fio-fio-3.27
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622048844
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static ; \
./configure --disable-native --extra-cflags="$CFLAGS"
make  %{?_smp_mflags}  V=1

%install
export SOURCE_DATE_EPOCH=1622048844
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fio
cp %{_builddir}/fio-fio-3.27/COPYING %{buildroot}/usr/share/package-licenses/fio/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/fio-fio-3.27/MORAL-LICENSE %{buildroot}/usr/share/package-licenses/fio/ffb3881ef6e7ef966b9fce711e1596d92a0e1e58
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fio
/usr/bin/fio-btrace2fio
/usr/bin/fio-dedupe
/usr/bin/fio-genzipf
/usr/bin/fio-histo-log-pctiles.py
/usr/bin/fio-verify-state
/usr/bin/fio_generate_plots
/usr/bin/genfio

%files data
%defattr(-,root,root,-)
/usr/share/fio/graph2D.gpm
/usr/share/fio/graph3D.gpm
/usr/share/fio/math.gpm

%files extras
%defattr(-,root,root,-)
/usr/bin/fio2gnuplot
/usr/bin/fio_jsonplus_clat2csv
/usr/bin/fiologparser.py
/usr/bin/fiologparser_hist.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fio/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/fio/ffb3881ef6e7ef966b9fce711e1596d92a0e1e58

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/fio.1
/usr/share/man/man1/fio2gnuplot.1
/usr/share/man/man1/fio_generate_plots.1
/usr/share/man/man1/fiologparser_hist.py.1
