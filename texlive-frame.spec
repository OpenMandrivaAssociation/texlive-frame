# revision 18312
# category Package
# catalog-ctan /macros/generic/frame
# catalog-date 2010-06-06 13:50:32 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-frame
Version:	1.0
Release:	4
Summary:	Framed boxes for Plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/frame
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frame.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frame.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 752093
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718503
- texlive-frame
- texlive-frame
- texlive-frame
- texlive-frame

