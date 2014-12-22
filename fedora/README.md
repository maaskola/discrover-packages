*How to create RPMs for Discrover*

First, you need to [prepare your system](https://fedoraproject.org/wiki/How_to_create_an_RPM_package#Preparing_your_system) for creating RPM packages.

Then, you want to place a copy of the [SPEC file](https://github.com/maaskola/discrover-packages/raw/master/fedora/SPECS/discrover.spec) into the SPECS directory created in the above step.

You can use ``spectool`` to retrieve the source code specified in the SPEC file: ``spectool -g SPECS/discrover.spec -C SOURCES/``.

Finally, with ``rpmbuild -ba SPECS/discrover.spec`` you can proceed to build an RPM of Discrover.

The [Fedora Packager's Guide](http://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/Packagers_Guide/index.html) provides information on [how to create packages](http://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/Packagers_Guide/chap-Packagers_Guide-Creating_and_Building_Packages.html) and [how to build RPMs](http://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/Packagers_Guide/sect-Packagers_Guide-Building_a_Package.html).
