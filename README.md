# DateDoctor

When analog photos are digitised by a lab, often they will all come back with the same timestamp. This confuses Googe Photos, and they are presented in whichever order they are uploaded (which, unless done one by one is pretty much random).

This script adds date taken metadata which Google Photos can use to order them correctly instead (assuming that the files are named sequentially). Since there is no way to know when the photos were really taken, they are tagged as if taken once per minute after a root timestamp that you choose.

It is reccomened to set the root timestamp in the middle of the night to not end up with other photos mixed in with the batch of analog photos.
