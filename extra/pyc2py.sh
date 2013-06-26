#!/bin/bash
# vim: ts=4 expandtab

for i in `find pyc_orig/ -name "*.pyc"`; do
    echo $i

    o=`echo $i | sed 's/pyc_orig/py/'`
    o=`echo $o | sed 's/\.pyc/\.py/'`
    echo $o
    mkdir -p `dirname $o`
    uncompyle2 -o $o $i

done
