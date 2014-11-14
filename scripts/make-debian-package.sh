#!/bin/bash
# A script to generate a Debian .deb package.
# Run it from the root directory of the Discrover package.
# It uses the current branch to generate a source archive.

DIR=$( cd "$( dirname "$0" )" && pwd )/..
export VERSION=`git describe | sed -e "s/-/./g"`
echo $VERSION

ruby scripts/make-source-release.rb $DIR/deb/discrover_$VERSION.tar.gz

cd $DIR/deb
cp discrover_$VERSION.tar.gz discrover_$VERSION.orig.tar.gz
tar xf discrover_$VERSION.orig.tar.gz 

# the debian directory contains some necessary files
cp -r debian/ discrover-$VERSION/
cd discrover-$VERSION/
dch --create -v $VERSION -M --package discrover
debuild -us -uc
