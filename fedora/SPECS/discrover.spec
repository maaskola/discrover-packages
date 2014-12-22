Name:		discrover
Version:	1.3.1
Release:	1%{?dist}
Summary:	Binding site pattern discovery from nucleic acid sequences by discriminative learning of hidden Markov models

License:	GPLv3+
URL:		https://github.com/maaskola/discrover
Source:	https://github.com/maaskola/discrover/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++ cmake ctags git boost-devel texlive-collection-latexextra ruby ruby-devel
Requires:	ImageMagick boost ruby texlive-latex-bin texlive-pgf texlive-xcolor texlive-standalone

%description


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
%{_libdir}/*.so
%{_defaultdocdir}/%{name}/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog

