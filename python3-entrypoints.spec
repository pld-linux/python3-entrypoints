#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Discover and load entry points from installed packages
Summary(pl.UTF-8):	Wykrywanie i wczytywanie punktów wejścia z zainstalowanych pakietów
Name:		python3-entrypoints
Version:	0.4
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/entrypoints/
Source0:	https://files.pythonhosted.org/packages/source/e/entrypoints/entrypoints-%{version}.tar.gz
# Source0-md5:	3acd8b72119a8fb1eac7030c24ac6b49
URL:		https://pypi.org/project/entrypoints/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.5
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Entry points are a way for Python packages to advertise objects with
some common interface. The most common examples are console_scripts
entry points, which define shell commands by identifying a Python
function to run.

Groups of entry points, such as console_scripts, point to objects with
similar interfaces. An application might use a group to find its
plugins, or multiple groups if it has different kinds of plugins.

The entrypoints module contains functions to find and load entry
points.

%description -l pl.UTF-8
Punty wejścia to sposób, w jaki pakiety Pythona udostępniają obiekty z
jakimś wspólnym interfejsem. Najpowszechniejszym przykładem są punkty
wejściowe skryptów konsoli (console_scripts), definiujące polecenia
powłoki poprzez określanie funkcji pythonowych do uruchomienia.

Grupy punktów wejścia, takie jak console_scripts, wskazują na obiekty
z podobnymi interfejsami. Aplikacja może używać grupy do znalezienia
swoich wtyczek, lub wielu grup, jeśli używa wtyczek różnych rodzajów.

Moduł entrypoints zawiera funkcje pomagające znajdować i ładować
punkty wejścia.

%package apidocs
Summary:	API documentation for Python entrypoints module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona entrypoints
Group:		Documentation

%description apidocs
API documentation for Python entrypoints module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona entrypoints.

%prep
%setup -q -n entrypoints-%{version}

%build
%py3_build_pyproject

%if %{with tests}
%{__python3} -m pytest tests
%endif

%if %{with doc}
%{__make} -C doc html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/entrypoints.py
%{py3_sitescriptdir}/__pycache__/entrypoints.cpython-*.py[co]
%{py3_sitescriptdir}/entrypoints-%{version}.dist-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/{_static,*.html,*.js}
%endif
