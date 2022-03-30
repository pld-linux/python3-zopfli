#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Zopfli module for Python
Summary(pl.UTF-8):	Moduł zopfli dla Pythona
Name:		python3-zopfli
Version:	0.2.1
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/zopfli/
Source0:	https://files.pythonhosted.org/packages/source/z/zopfli/zopfli-%{version}.zip
# Source0-md5:	505ea595d86b8a7fec55620c839a4859
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
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(echo $(pwd)/build-3/lib.*) \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

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
