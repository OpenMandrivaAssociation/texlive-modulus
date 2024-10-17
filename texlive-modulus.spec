Name:		texlive-modulus
Version:	47599
Release:	2
Summary:	A non-destructive modulus and integer quotient operator for TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/modulus
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modulus.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modulus.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modulus.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an easy way to take the remainder of a
division operation without destroying the values of the
counters containing the dividend and divisor. Also provides a
way to take the integer quotient of a division operation
without destroying the values of the counters containing the
dividend and divisor. A tiny but occasionally useful package,
when doing heavy TeX programming.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/modulus
%{_texmfdistdir}/tex/generic/modulus
%doc %{_texmfdistdir}/doc/generic/modulus

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
