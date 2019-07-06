#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-DBI
Version  : 1.0.0
Release  : 74
URL      : https://cran.r-project.org/src/contrib/DBI_1.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/DBI_1.0.0.tar.gz
Summary  : R Database Interface
Group    : Development/Tools
License  : LGPL-2.0+
Requires: R-rlang
BuildRequires : R-backports
BuildRequires : R-cli
BuildRequires : R-knitr
BuildRequires : R-markdown
BuildRequires : R-rlang
BuildRequires : R-rprojroot
BuildRequires : R-withr
BuildRequires : R-xml2
BuildRequires : buildreq-R

%description
# DBI
[![Build Status](https://travis-ci.org/r-dbi/DBI.png?branch=master)](https://travis-ci.org/r-dbi/DBI) [![Coverage Status](https://codecov.io/gh/r-dbi/DBI/branch/master/graph/badge.svg)](https://codecov.io/github/r-dbi/DBI?branch=master) [![CRAN_Status_Badge](http://www.r-pkg.org/badges/version/DBI)](https://cran.r-project.org/package=DBI)

%prep
%setup -q -c -n DBI

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552962865

%install
export SOURCE_DATE_EPOCH=1552962865
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DBI
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DBI
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DBI
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  DBI || :


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
/usr/lib64/R/library/DBI/doc/DBI-proposal.Rmd
/usr/lib64/R/library/DBI/doc/DBI-proposal.html
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
/usr/lib64/R/library/DBI/help/paths.rds
/usr/lib64/R/library/DBI/html/00Index.html
/usr/lib64/R/library/DBI/html/R.css
/usr/lib64/R/library/DBI/tests/testthat.R
/usr/lib64/R/library/DBI/tests/testthat/helper-dummy.R
/usr/lib64/R/library/DBI/tests/testthat/test-data-type.R
/usr/lib64/R/library/DBI/tests/testthat/test-interpolate.R
/usr/lib64/R/library/DBI/tests/testthat/test-methods.R
/usr/lib64/R/library/DBI/tests/testthat/test-quote.R
/usr/lib64/R/library/DBI/tests/testthat/test-quoting.R
/usr/lib64/R/library/DBI/tests/testthat/test-rownames.R
/usr/lib64/R/library/DBI/tests/testthat/test-sql-df.R
