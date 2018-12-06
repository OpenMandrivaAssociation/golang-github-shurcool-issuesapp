# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/issuesapp
%global commit          048589ce2241c1c07ffb4c5434a21169a100380e

%global common_description %{expand:
Collection of basic HTML components.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Collection of basic HTML components
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/dustin/go-humanize)
BuildRequires: golang(github.com/shurcooL/github_flavored_markdown)
BuildRequires: golang(github.com/shurcooL/github_flavored_markdown/gfmstyle)
BuildRequires: golang(github.com/shurcooL/go/ctxhttp)
BuildRequires: golang(github.com/shurcooL/go/gopherjs_http)
BuildRequires: golang(github.com/shurcooL/htmlg)
BuildRequires: golang(github.com/shurcooL/httperror)
BuildRequires: golang(github.com/shurcooL/httpfs/html/vfstemplate)
BuildRequires: golang(github.com/shurcooL/httpfs/union)
BuildRequires: golang(github.com/shurcooL/httpgzip)
BuildRequires: golang(github.com/shurcooL/issues)
BuildRequires: golang(github.com/shurcooL/notifications)
BuildRequires: golang(github.com/shurcooL/octicon)
BuildRequires: golang(github.com/shurcooL/reactions)
BuildRequires: golang(github.com/shurcooL/reactions/component)
BuildRequires: golang(github.com/shurcooL/users)
BuildRequires: golang(golang.org/x/net/html)
BuildRequires: golang(golang.org/x/net/html/atom)

%if %{with check}
BuildRequires: golang(dmitri.shuralyov.com/html/belt)
BuildRequires: golang(github.com/gorilla/mux)
BuildRequires: golang(github.com/shurcooL/home/httputil)
BuildRequires: golang(github.com/shurcooL/notificationsapp)
BuildRequires: golang(github.com/shurcooL/webdavfs/vfsutil)
BuildRequires: golang(golang.org/x/oauth2)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%build 
%gobuildroot
for cmd in $(ls -1 cmd) ; do
   %gobuild -o _bin/$cmd %{goipath}/cmd/$cmd
done


%install
%goinstall
for cmd in $(ls -1 _bin) ; do
  install -Dpm 0755 _bin/$cmd %{buildroot}%{_bindir}/$cmd
done


%if %{with check}
%check
%gochecks
%endif


%files
%license LICENSE
%{_bindir}/*


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20181026git048589c
- Bump to commit 048589ce2241c1c07ffb4c5434a21169a100380e

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git0f62bfd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180422git0f62bfd
- First package for Fedora

