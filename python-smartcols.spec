%global debug_package %{nil}

Summary:	Python bindings for the util-linux libsmartcols library
Name:		python-smartcols
Version:	0.3.0
Release:	5
Group:		Development/Python
License:	GPLv2+
Url:		https://github.com/ignatenkobrain/python-smartcols
Source0:	https://github.com/ignatenkobrain/python-smartcols/archive/v%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(smartcols)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(pytest-runner)
BuildRequires:	python3dist(cython)

%description
Python bindings for the util-linux libsmartcols library.

%files
%{py_platsitedir}/smartcols*

%prep
%autosetup -p1

%build
python setup.py build

%install
python setup.py install --root %{buildroot}
