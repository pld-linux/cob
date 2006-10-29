Summary:	Remake of Sinclair Spectrum painting game
Summary(pl):	Remake gry na Spectruma
Name:		cob
Version:	0.9
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.autismuk.freeserve.co.uk/%{name}-%{version}.tar.gz
# Source0-md5:	ece428dade7d905e644d66e54b93da40
URL:		http://www.autismuk.freeserve.co.uk/
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cruising on Broadway is a painting-type game where you have to roam
the grid avoiding the 'chasers' - a bit like the arcade game Amidar.
It is based on the Sinclair Spectrum game of the same name.

%description -l pl
Cruising on Broadway jest gr±, w której nale¿y poruszaæ siê po siatce
i unikaæ "³apaczy" - przypomina to trochê grê zrêczno¶ciow± Amidar.
Gra oprata jest na grze dla Sinclair Spectrum o tym samym tytule.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/%{name}
