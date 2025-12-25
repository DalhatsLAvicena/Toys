#!/usr/bin/bash

# display `whatis` of every commands in the system
ls /bin | xargs whatis | less
