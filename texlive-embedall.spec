# revision 31903
# category Package
# catalog-ctan /macros/latex/contrib/embedall
# catalog-date 2013-10-14 16:22:06 +0200
# catalog-license lppl1.2
# catalog-version 1.0
Name:		texlive-embedall
Version:	1.0
Release:	8
Summary:	Embed source files into the generated PDF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/embedall
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/embedall.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/embedall.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/embedall.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a means of storing a project, without
losing anything. It uses the embedfile package to attach to the
generated PDF all files used in creating your project. In
particular, it can embed images, external TeX files, external
codes and.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/embedall/embedall.sty
%doc %{_texmfdistdir}/doc/latex/embedall/embedall.pdf
#- source
%doc %{_texmfdistdir}/source/latex/embedall/embedall.dtx
%doc %{_texmfdistdir}/source/latex/embedall/embedall.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
