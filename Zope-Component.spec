Summary:	Core of the Zope Component Architecture
Summary(pl.UTF-8):	Rdzeń Zope Component Architecture
Name:		Zope-Component
Version:	3.10.0
Release:	1
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/z/zope.component//zope.component-%{version}.tar.gz
# Source0-md5:	8041d92540e701943daed97329012348
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Requires:	Zope-DeferredImport
Requires:	Zope-Deprecation
Requires:	Zope-Event
Requires:	Zope-Interface
Requires:	Zope-Proxy
Requires:	Zope-Testing
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Core of the Zope Component Architecture.

%description -l pl.UTF-8
Rdzeń architektury komponentowej Zope Component Architecture.

%prep
%setup -q -n zope.component-%{version}

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--install-purelib=%{py_sitedir} \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/zope/component
%{py_sitedir}/zope.component-*.egg-info
%{py_sitedir}/zope.component-*-nspkg.pth
