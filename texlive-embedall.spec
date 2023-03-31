Name:		texlive-embedall
Version:	51177
Release:	2
Summary:	Embed source files into the generated PDF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/embedall
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/embedall.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/embedall.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/embedall.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/embedall
%doc %{_texmfdistdir}/doc/latex/embedall
#- source
%doc %{_texmfdistdir}/source/latex/embedall

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
