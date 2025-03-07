#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : R-DBI
Version  : 1.2.3
Release  : 113
URL      : https://cran.r-project.org/src/contrib/DBI_1.2.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/DBI_1.2.3.tar.gz
Summary  : R Database Interface
Group    : Development/Tools
License  : LGPL-2.1+
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
and relational database management systems.  All classes in this
    package are virtual and need to be extended by the various R/DBMS
    implementations.

%prep
%setup -q -n DBI
pushd ..
cp -a DBI buildavx2
popd
pushd ..
cp -a DBI buildavx512
popd
pushd ..
cp -a DBI buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1740090641

%install
export SOURCE_DATE_EPOCH=1740090641
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/DBI/DESCRIPTION
/usr/lib64/R/library/DBI/INDEX
/usr/lib64/R/library/DBI/Meta/Rd.rds
/usr/lib64/R/library/DBI/Meta/features.rds
/usr/lib64/R/library/DBI/Meta/hsearch.rds
/usr/lib64/R/library/DBI/Meta/links.rds
/usr/lib64/R/library/DBI/Meta/nsInfo.rds
/usr/lib64/R/library/DBI/Meta/package.rds
/usr/lib64/R/library/DBI/Meta/vignette.rds
/usr/lib64/R/library/DBI/NAMESPACE
/usr/lib64/R/library/DBI/NEWS.md
/usr/lib64/R/library/DBI/R/DBI
/usr/lib64/R/library/DBI/R/DBI.rdb
/usr/lib64/R/library/DBI/R/DBI.rdx
/usr/lib64/R/library/DBI/doc/DBI-1.Rmd
/usr/lib64/R/library/DBI/doc/DBI-1.html
/usr/lib64/R/library/DBI/doc/DBI-advanced.R
/usr/lib64/R/library/DBI/doc/DBI-advanced.Rmd
/usr/lib64/R/library/DBI/doc/DBI-advanced.html
/usr/lib64/R/library/DBI/doc/DBI-arrow.R
/usr/lib64/R/library/DBI/doc/DBI-arrow.Rmd
/usr/lib64/R/library/DBI/doc/DBI-arrow.html
/usr/lib64/R/library/DBI/doc/DBI-history.Rmd
/usr/lib64/R/library/DBI/doc/DBI-history.html
/usr/lib64/R/library/DBI/doc/DBI-proposal.Rmd
/usr/lib64/R/library/DBI/doc/DBI-proposal.html
/usr/lib64/R/library/DBI/doc/DBI.R
/usr/lib64/R/library/DBI/doc/DBI.Rmd
/usr/lib64/R/library/DBI/doc/DBI.html
/usr/lib64/R/library/DBI/doc/backend.R
/usr/lib64/R/library/DBI/doc/backend.Rmd
/usr/lib64/R/library/DBI/doc/backend.html
/usr/lib64/R/library/DBI/doc/index.html
/usr/lib64/R/library/DBI/doc/spec.R
/usr/lib64/R/library/DBI/doc/spec.Rmd
/usr/lib64/R/library/DBI/doc/spec.html
/usr/lib64/R/library/DBI/help/AnIndex
/usr/lib64/R/library/DBI/help/DBI.rdb
/usr/lib64/R/library/DBI/help/DBI.rdx
/usr/lib64/R/library/DBI/help/aliases.rds
/usr/lib64/R/library/DBI/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/DBI/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/DBI/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/DBI/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/DBI/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/DBI/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/DBI/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/DBI/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/DBI/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/DBI/help/paths.rds
/usr/lib64/R/library/DBI/html/00Index.html
/usr/lib64/R/library/DBI/html/R.css
/usr/lib64/R/library/DBI/tests/testthat.R
/usr/lib64/R/library/DBI/tests/testthat/_snaps/00-Id.md
/usr/lib64/R/library/DBI/tests/testthat/helper-dummy.R
/usr/lib64/R/library/DBI/tests/testthat/setup.R
/usr/lib64/R/library/DBI/tests/testthat/test-00-Id.R
/usr/lib64/R/library/DBI/tests/testthat/test-DBItest.R
/usr/lib64/R/library/DBI/tests/testthat/test-arrow.R
/usr/lib64/R/library/DBI/tests/testthat/test-data-type.R
/usr/lib64/R/library/DBI/tests/testthat/test-dbUnquoteIdentifier_DBIConnection.R
/usr/lib64/R/library/DBI/tests/testthat/test-interpolate.R
/usr/lib64/R/library/DBI/tests/testthat/test-methods.R
/usr/lib64/R/library/DBI/tests/testthat/test-quote.R
/usr/lib64/R/library/DBI/tests/testthat/test-quoting.R
/usr/lib64/R/library/DBI/tests/testthat/test-rownames.R
/usr/lib64/R/library/DBI/tests/testthat/test-sql-df.R
/usr/lib64/R/library/DBI/tests/testthat/test-table-insert.R
