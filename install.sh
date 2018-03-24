#!/bin/bash

# guess user package directory
packagesDir=~/.config/sublime-text-3/Packages

if $(test -d $packagesDir)
then
    echo "Found Package Directory: $packagesDir"
else
    echo "Package Directory could not be found. Looked for: $packagesDir"
    exit 1
fi

base64DecodePopupPackageDir=$packagesDir/base64-decode-popup

if $(test -d $base64DecodePopupPackageDir)
then
    echo "base64-decode-popup package already installed. Removing old version."
    rm -rf $base64DecodePopupPackageDir

    if [ $? -ne 0 ]
    then
        echo "Could not remove old version."
        exit $?
    fi
fi

echo "Copying package contents to Package Directory..."
cp -a . "$packagesDir/base64-decode-popup"

if [ $? -eq 0 ]
then
  echo "Install successful."
else
  echo "Install failed."
fi
