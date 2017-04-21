#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-DBI
Version  : 0.6.1
Release  : 36
URL      : http://cran.r-project.org/src/contrib/DBI_0.6-1.tar.gz
Source0  : http://cran.r-project.org/src/contrib/DBI_0.6-1.tar.gz
Summary  : R Database Interface
Group    : Development/Tools
License  : LGPL-2.0+
Requires: R-hms
Requires: R-markdown
BuildRequires : R-hms
BuildRequires : R-knitr
BuildRequires : R-markdown
BuildRequires : clr-R-helpers

%description
# DBI
[![Build Status](https://travis-ci.org/rstats-db/DBI.png?branch=master)](https://travis-ci.org/rstats-db/DBI) [![Coverage Status](https://img.shields.io/codecov/c/github/rstats-db/DBI/master.svg)](https://codecov.io/github/rstats-db/DBI?branch=master) [![CRAN_Status_Badge](http://www.r-pkg.org/badges/version/DBI)](https://cran.r-project.org/package=DBI)

%prep
%setup -q -c -n DBI

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491148714

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1491148714
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DBI
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library DBI


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/DBI/DESCRIPTION
/usr/lib64/R/library/DBI/INDEX
/usr/lib64/R/library/DBI/Meta/Rd.rds
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
