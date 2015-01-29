#!/bin/bash
# A script to generate a Debian .deb package.
# Run it from the root directory of the Discrover package.
# It uses the current branch to generate a source archive.

die () {
    echo >&2 "$@"
    exit 1
}

[ "$#" -eq 1 ] || die "One argument required, $# provided"
echo $1 | grep -E -q '^[0-9]+$' || die "Numeric argument required, $1 provided"


DIR=$( cd "$( dirname "$0" )" && pwd )/..
export VERSION=`git describe | sed -e "s/-/./g"`
echo $VERSION
export PACKAGE_VERSION=$VERSION-$1

ruby $DIR/scripts/make-source-release.rb $DIR/deb/discrover_$VERSION.tar.gz

cd $DIR/deb
cp discrover_$VERSION.tar.gz discrover_$VERSION.orig.tar.gz
tar xf discrover_$VERSION.orig.tar.gz 

# the debian directory contains some necessary files
cp -r debian/ discrover-$VERSION/
cd discrover-$VERSION/
dch --create -v $PACKAGE_VERSION -M --package discrover
debuild -us -uc
