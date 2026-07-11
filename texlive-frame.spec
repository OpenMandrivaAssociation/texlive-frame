%global tl_name frame
%global tl_revision 18312

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Framed boxes for Plain TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/frame
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/frame.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/frame.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A jiffy file (taken from fancybox) for placing a frame around a box of
text. The macros also provide for typesetting an empty box of given
dimensions.

