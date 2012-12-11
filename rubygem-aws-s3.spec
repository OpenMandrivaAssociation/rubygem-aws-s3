%define oname aws-s3

Name:       rubygem-%{oname}
Version:    0.6.2
Release:    %mkrel 1
Summary:    Client library for Amazon's Simple Storage Service's REST API
Group:      Development/Ruby
License:    MIT
URL:        http://amazon.rubyforge.org
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Requires:   rubygem(xml-simple)
Requires:   rubygem(builder)
Requires:   rubygem(mime-types)
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Client library for Amazon's Simple Storage Service's REST API


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/s3sh
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/support/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/COPYING
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/INSTALL
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Fri Dec 10 2010 Rémy Clouard <shikamaru@mandriva.org> 0.6.2-1mdv2011.0
+ Revision: 620456
- import rubygem-aws-s3

