%global packname  preprocessCore
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.16.0
Release:          1
Summary:          A collection of pre-processing functions
Group:            Sciences/Mathematics
License:          LGPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-methods 
Requires:         R-stats 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
BuildRequires:    R-stats 

%description
A library of core preprocessing routines

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/libs
