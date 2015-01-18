Name:		discrover
Version:	1.5.0
Release:	1%{?dist}
Summary:	Discriminative motif finder

License:	GPLv3+
URL:		https://github.com/maaskola/discrover
Source:	https://github.com/maaskola/discrover/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++ cmake git boost-devel texlive-collection-latexextra cairo-devel
Requires:	boost cairo

%description
A discriminative motif discovery method to find binding site pattern discovery
from nucleic acid sequences.

The method is described in this open-access article:
Jonas Maaskola and Nikolaus Rajewsky. Binding site discovery from nucleic acid
sequences by discriminative learning of hidden Markov models.
Nucleic Acid Research, 42(21):12995-13011, Dec 2014. doi:10.1093/nar/gku1083


%prep
%autosetup


%build
%cmake .
make %{?_smp_mflags}


%install
%make_install


%files
%doc
%{_bindir}/*
%{_libdir}/*
%{_defaultdocdir}/%{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog

