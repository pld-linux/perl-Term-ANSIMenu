#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Term
%define		pnam	ANSIMenu
%include	/usr/lib/rpm/macros.perl
Summary:	Term::ANSIMenu - An infrastructure for creating menus in ANSI capable terminals
#Summary(pl.UTF-8):	
Name:		perl-Term-ANSIMenu
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Term/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9d3754d608c119b88e411dfae0c24157
URL:		http://search.cpan.org/dist/Term-ANSIMenu/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I wrote this mainly to make live easy on those staff members to whom I delegate
tasks. Most of them prefer to use a menu instead of having to type complicated 
commands. To them it's a faster and safer way of working (we all know about 
typos don't we...).

By using this module you can create menus with only a few lines of code and 
still have a shipload of features. Need context-sensitive help or a statusbar?
Like to use hotkeys? Want flashy colors and styles? It's all there. Just fill 
in the attributes and you're good to go.

A menu can be made up of a title, a number of selectable items, a status line
and a prompt. Each of those elements can be given a fore- and background color
and a style to give it the appearance wanted. The same goes for the optional 
frames around these elements. It is also possible to align each element 
independently (but the all items together are considered as one element).

Every item in the menu can be selected using definable hotkeys or navigation
keys. To assist users of the menu hints that will be diplayed in the status
line can be associated with itemsi. For situations where a simple hint isn't 
good enough context-sensitive help is available through definable keys (like 
the well-known <F1> and '?').

Finally to get out of the menu without having to explicitly create an entry for
that one or more keys can be assigned that will cause an immediate return from
the menu to the calling program. The exit status reflects the conditions under
which that happened.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT{%{perl_vendorlib}/Term/example.pl,%{_examplesdir}/%{name}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Term/ANSIMenu.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}
