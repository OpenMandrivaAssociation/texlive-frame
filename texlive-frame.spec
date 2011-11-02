Name:		texlive-frame
Version:	1.0
Release:	1
Summary:	Framed boxes for Plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/frame
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frame.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frame.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A jiffy file (taken from fancybox) for placing a frame around a
box of text. The macros also provide for typesetting an empty
box of given dimensions.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/frame/frame.sty
%{_texmfdistdir}/tex/generic/frame/frame.tex
%doc %{_texmfdistdir}/doc/generic/frame/Changes
%doc %{_texmfdistdir}/doc/generic/frame/Makefile
%doc %{_texmfdistdir}/doc/generic/frame/README
%doc %{_texmfdistdir}/doc/generic/frame/frame-doc.pdf
%doc %{_texmfdistdir}/doc/generic/frame/frame-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
