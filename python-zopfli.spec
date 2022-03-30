#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Zopfli module for Python
Summary(pl.UTF-8):	Moduł zopfli dla Pythona
Name:		python-zopfli
Version:	0.1.9
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/zopfli/
Source0:	https://files.pythonhosted.org/packages/source/z/zopfli/zopfli-%{version}.zip
# Source0-md5:	f66b6f4132533b9b0ab8b0af757237bf
URL:		https://pypi.org/project/zopfli/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
Requires:	python-modules >= 1:2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyzopfli is a straight forward wrapper around zopfli's ZlibCompress
method.

%description -l pl.UTF-8
pyzopfli to bezpośrednie obudowanie metody ZlibCompress biblioteki
zopfli.

%package -n python3-zopfli
Summary:	Zopfli module for Python
Summary(pl.UTF-8):	Moduł zopfli dla Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-zopfli
pyzopfli is a straight forward wrapper around zopfli's ZlibCompress
method.

%description -n python3-zopfli -l pl.UTF-8
pyzopfli to bezpośrednie obudowanie metody ZlibCompress biblioteki
zopfli.

%prep
%setup -q -n zopfli-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(echo $(pwd)/build-2/lib.*) \
%{__python} tests/tests.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(echo $(pwd)/build-3/lib.*) \
%{__python3} tests/tests.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%dir %{py_sitedir}/zopfli
%attr(755,root,root) %{py_sitedir}/zopfli/zopfli.so
%{py_sitedir}/zopfli/*.py[co]
%{py_sitedir}/zopfli-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-zopfli
%defattr(644,root,root,755)
%dir %{py3_sitedir}/zopfli
%attr(755,root,root) %{py3_sitedir}/zopfli/zopfli.cpython-*.so
%{py3_sitedir}/zopfli/*.py
%{py3_sitedir}/zopfli/__pycache__
%{py3_sitedir}/zopfli-%{version}-py*.egg-info
%endif
