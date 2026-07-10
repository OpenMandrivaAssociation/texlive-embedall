%global tl_name embedall
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Embed source files into the generated PDF
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/embedall
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/embedall.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/embedall.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/embedall.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a means of storing a project, without losing
anything. It uses the embedfile package to attach to the generated PDF
all files used in creating your project. In particular, it can embed
images, external TeX files, external codes and

