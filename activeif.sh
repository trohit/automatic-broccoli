#!/bin/sh
/sbin/route -n | grep "^0.0.0.0" | awk {'print $8'}

