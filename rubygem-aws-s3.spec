%define oname aws-s3

Name:       rubygem-%{oname}
Version:    0.6.3
Release:    1
Summary:    Client library for Amazon's Simple Storage Service's REST API
Group:      Development/Ruby
License:    MIT
URL:        http://amazon.rubyforge.org
Source0:    http://rubygems.org/gems/aws-s3-0.6.3.gem
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
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

%clean

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
