Here you will find routines to generate [Discrover](https://github.com/maaskola/discrover) packages for different Linux distributions.

Linux distributions for which package generation routines are currently available include:

 * [Arch Linux](https://www.archlinux.org/)
 * [Debian](https://www.debian.org/)
 * [Gentoo](https://www.gentoo.org/)
 * [Fedora](https://fedoraproject.org/)
 * [Ubuntu](https://www.ubuntu.com/)

Note that the Gentoo ebuilds are also contained in the [gentoo-science overlay](https://github.com/gentoo-science/sci).
You can add this overlay, accept unstable versions of Discrover, and emerge it with the following commands:
```sh
layman -a science
echo "=sci-biology/discrover-X.Y.Z ~amd64" >> /etc/portage/package.keywords
emerge -av discrover
```
