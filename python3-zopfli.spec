#
# Conditional build:
%bcond_without	tests		# unit tests
%bcond_without	system_zopfli	# system zopfli libraries

Summary:	Zopfli module for Python
Summary(pl.UTF-8):	Moduł zopfli dla Pythona
Name:		python3-zopfli
Version:	0.2.2
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/zopfli/
Source0:	https://files.pythonhosted.org/packages/source/z/zopfli/zopfli-%{version}.zip
# Source0-md5:	0c1e41e5403524e0180f3ed9aaa356ec
URL:		https://pypi.org/project/zopfli/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
%if %{with system_zopfli}
BuildRequires:	zopfli-devel
BuildRequires:	zopfli-png-devel
%endif
Requires:	python3-modules >= 1:3.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyzopfli is a straight forward wrapper around zopfli's ZlibCompress
method.

%description -l pl.UTF-8
pyzopfli to bezpośrednie obudowanie metody ZlibCompress biblioteki
zopfli.

%prep
%setup -q -n zopfli-%{version}

%build
%if %{with system_zopfli}
export USE_SYSTEM_ZOPFLI=1
%endif

%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(echo $(pwd)/build-3/lib.*) \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with system_zopfli}
export USE_SYSTEM_ZOPFLI=1
%endif

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%dir %{py3_sitedir}/zopfli
%attr(755,root,root) %{py3_sitedir}/zopfli/zopfli.cpython-*.so
%{py3_sitedir}/zopfli/*.py
%{py3_sitedir}/zopfli/__pycache__
%{py3_sitedir}/zopfli-%{version}-py*.egg-info
