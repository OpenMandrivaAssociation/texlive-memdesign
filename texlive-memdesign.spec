# revision 20237
# category Package
# catalog-ctan /info/memdesign
# catalog-date 2010-10-28 17:24:15 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-memdesign
Version:	20101028
Release:	1
Summary:	Notes on book design
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/memdesign
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/memdesign.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/memdesign.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
"A Few Notes on Book Design" provides an introduction to the
business of book design. It is an extended version of what used
to be the first part of the memoir users' manual. Please note
that the supplied copy of the document uses commercial fonts;
the README file contains instructions on how to compile the
document without these fonts.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/fonts/memdesign/README
%doc %{_texmfdistdir}/doc/fonts/memdesign/memdesign.pdf
%doc %{_texmfdistdir}/doc/fonts/memdesign/memdesign.tex
%doc %{_texmfdistdir}/doc/fonts/memdesign/memetc.bib
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
