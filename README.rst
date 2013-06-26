Hello
=====

You probably want to see `Inside Druva inSync.pdf`

Versions 5.1 and 5.2 were analyzed.

Resources
=========

* http://www.druva.com/documents/Druva-inSync-Security-Overview.pdf

* http://www.druva.com/documents/Druva-inSync-Security.pdf

* http://www.druva.com/insync/downloads/server/enterprise/

* http://www.druva.com/insync/downloads/client/

* https://github.com/Mysterie/uncompyle2

Notes
=====

Some claims,

::

  The Blackbird storage engine stores the backed up data in 1024 ISD (InSync
  Data) files. It uses data deduplication to break the user backup files into
  small (8KB or less) blocks and store them in different ISD files. This makes
  it nearly impossible for anyone to assemble the user files again, without the
  complete knowledge of file’s original construct and Blackbird’s proprietary
  file format.

Security through obscurity?

