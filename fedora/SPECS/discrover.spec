Name:		discrover
Version:	1.1.1
Release:	1%{?dist}
Summary:	Binding site pattern discovery from nucleic acid sequences by discriminative learning of hidden Markov models

# Group:		
License:	GPLv3+
URL:		https://github.com/maaskola/discrover
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++ cmake ctags git boost-devel texlive-collection-latexextra
Requires:	ImageMagick boost

%description


%prep
%autosetup


%build
%cmake .
make %{?_smp_mflags}


%install
%make_install
# rm -rf $RPM_BUILD_ROOT
# make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc
/usr/bin/dinucleotide_shuffle
/usr/bin/discrover
/usr/bin/hmm.rb
/usr/bin/hmm2meme
/usr/bin/plasma
/usr/bin/reldistplot.r
/usr/bin/sl
/usr/bin/tikzlogo
/usr/lib/libdiscrover.so
/usr/lib/libdiscroverplasma.so
/usr/lib/libdiscrovershuffle.so
/usr/lib/libdiscroverstats.so
/usr/share/doc/discrover/AUTHORS
/usr/share/doc/discrover/COPYING
/usr/share/doc/discrover/FAQ
/usr/share/doc/discrover/README.md
/usr/share/doc/discrover/TODO
/usr/share/doc/discrover/discrover-manual.pdf

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog

