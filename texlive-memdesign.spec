# revision 34157
# category Package
# catalog-ctan /info/memdesign
# catalog-date 2014-05-20 19:24:27 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-memdesign
Version:	20180303
Release:	2
Summary:	Notes on book design
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/memdesign
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/memdesign.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/memdesign.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
"A Few Notes on Book Design" provides an introduction to the
business of book design. It is an extended version of what used
to be the first part of the memoir users' manual. Please note
that the compiled copy, supplied in the package, uses
commercial fonts; the README file contains instructions on how
to compile the document without these fonts.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/fonts/memdesign/README
%doc %{_texmfdistdir}/doc/fonts/memdesign/memdesign.pdf
%doc %{_texmfdistdir}/doc/fonts/memdesign/memdesign.tex
%doc %{_texmfdistdir}/doc/fonts/memdesign/memetc.bib

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
