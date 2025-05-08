**CSCI410/CSCI610 Final Project**  
By Cale Voglewede and Nancy Mahlen  

This project showcases an implementation of a file identification system
using file signatures at the beginning of files and hamming distance. It
should be noted that this implementation is experimental and doesn't
cover other valid file identification techniques.

The subdirectories purposes' are the following:

**config**

Holds the supported files and their respective file signature within a JSON file

**src**

Holds the source code to execute the file identification system

The files' main functions are:
* main.py - runs the user interface for the file identification system
* json_config - reads results fom supported_file.json
* file_read - reads test files in binary for identification

**test_files**

Holds a repository of test files to test identifcation system.

&emsp;(see test_files/file_key.txt for file identities)

**Acknowledgements**  

File signatures provided from GCK File Signature Table (https://filesig.search.org/about)

Tux image by Larry Ewing @ lewing@isc.tamu.edu and The GIMP

