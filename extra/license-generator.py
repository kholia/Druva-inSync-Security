#!/usr/bin/env python

# license generator for insync 5.2 "Enterprise Edition"
# inSyncLib/inSyncLicense.pyc

# retrieve your "LICENSE" string from inSyncServer.cfg
# and substitute below
LICENSE = 'QlpoOTFBWSZTWfb2bc8AAHGdgAABf/ACAD/93wAgAJIR6qBphGgNAaHqEeomlHpmmpAAAUDY4ODhmdsZsiIoaLrXAWV4+YvMgySGrgwZppS4O3CKvxkLsy4RX57r77N4EjNaIyD2hESWl/KgoNuZrOmau3ptlyue2L8qKPOEdXBtTweyzp1WKRbowPg9+CHC6ysfGHdwRD114fi7kinChIe3s254'

import base64
import hashlib
import bz2
import time
import cPickle as pickle

licensestr = bz2.decompress(base64.decodestring(LICENSE))
# print LICENSE
# print licensestr
tokens = licensestr.split(':')

# 10 years is "Forever"
safe_time = int(time.time() + 316224000)

# patch stuff
for i in range(0, len(tokens)):
    if tokens[i] == "Evaluation":
        tokens[i] = "Enterprise"

cpuid = tokens[0]
version = tokens[1]
salt = tokens[2]
timelimit = float(tokens[3])
print timelimit, "original"
# modify
timelimit = float(safe_time)
print str(timelimit), "new"
clients = int(tokens[4])
# modify
clients = 99999999
storage = int(tokens[5])
type = tokens[6]
edition = tokens[7]
features = tokens[8]
dpstimelimit = float(tokens[9])
# modify
dpstimelimit = float(safe_time)
dpstype = tokens[10]
datainsights_timelimit = float(tokens[11])
# modify
datainsights_timelimit = float(safe_time)
datainsights_type = tokens[12]
mobilebackup_timelimit = float(tokens[13])
# modify
mobilebackup_timelimit = float(safe_time)
mobilebackup_type = tokens[14]
mobilesafepoint_timelimit = float(tokens[15])
# modify
mobilesafepoint_timelimit = float(safe_time)
mobilesafepoint_type = tokens[16]
syncshare_timelimit = float(tokens[17])
# modify
syncshare_timelimit = float(safe_time)
syncshare_type = tokens[18]
systemsettings_timelimit = float(tokens[19])
# modify
systemsettings_timelimit = float(safe_time)
systemsettings_type = tokens[20]
digest = tokens[21]
# print digest, "digest"

licensestr = cpuid
licensestr += ':' + version
licensestr += ':' + salt
licensestr += ':' + str(timelimit)
licensestr += ':' + str(clients)
licensestr += ':' + str(storage)
licensestr += ':' + type
licensestr += ':' + edition
licensestr += ':' + str(features)
licensestr += ':' + str(dpstimelimit)
licensestr += ':' + str(dpstype)
licensestr += ':' + str(datainsights_timelimit)
licensestr += ':' + str(datainsights_type)
licensestr += ':' + str(mobilebackup_timelimit)
licensestr += ':' + str(mobilebackup_type)
licensestr += ':' + str(mobilesafepoint_timelimit)
licensestr += ':' + str(mobilesafepoint_type)
licensestr += ':' + str(syncshare_timelimit)
licensestr += ':' + str(syncshare_type)
licensestr += ':' + str(systemsettings_timelimit)
licensestr += ':' + str(systemsettings_type)

# hashing and encoding stuff
hash =  hashlib.md5(licensestr).hexdigest()
licensestr += ':' + hash
print licensestr
licensestr = base64.b64encode(bz2.compress(licensestr, 9))
print licensestr

# save license
f = open("enterprise_license.isl", 'wb')
pickle.dump(licensestr, f)
f.close()

print "\n[+] license saved to enterprise_license.isl file"
