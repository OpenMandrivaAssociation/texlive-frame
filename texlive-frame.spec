Name:		texlive-frame
Version:	18312
Release:	2
Summary:	Framed boxes for Plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/frame
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frame.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frame.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A jiffy file (taken from fancybox) for placing a frame around a
box of text. The macros also provide for typesetting an empty
box of given dimensions.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
