%define snap r73807
Summary:	Core of the Zope Component Architecture
Summary(pl.UTF-8):	Rdzeń Zope Component Architecture
Name:		Zope-Component
Version:	3.4
Release:	0.%{snap}.2
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	http://download.zope.org/distribution/zope.component-%{version}dev-%{snap}.tar.gz
# Source0-md5:	d91d7c64259a1a2f8e56860a1326725e
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Requires:	Zope-DeferredImport
Requires:	Zope-Deprecation
Requires:	Zope-Event
Requires:	Zope-Interface
Requires:	Zope-Proxy
Requires:	Zope-Testing
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Core of the Zope Component Architecture.

%description -l pl.UTF-8
Rdzeń architektury komponentowej Zope Component Architecture.

%prep
%setup -q -n zope.component-%{version}dev-%{snap}

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
