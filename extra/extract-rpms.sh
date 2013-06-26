#!/bin/sh

mkdir -p client
pushd .
cd client
rpm2cpio ../inSync-Client-Installer-ver-5.1.1-r14802.i386.rpm | cpio --extract --make-directories
popd

mkdir -p server
pushd .
cd server
rpm2cpio ../inSync-Server-Enterprise-Installer-ver-5.1.1-r16050.i386.rpm | cpio --extract --make-directories
popd


