#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-coveralls
Version  : 0.8.13
Release  : 11
URL      : https://rubygems.org/downloads/coveralls-0.8.13.gem
Source0  : https://rubygems.org/downloads/coveralls-0.8.13.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-coveralls-bin
BuildRequires : ruby
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-tins

%description
# [Coveralls](http://coveralls.io) for Ruby [![Test Coverage](https://coveralls.io/repos/lemurheavy/coveralls-ruby/badge.svg?branch=master)](https://coveralls.io/r/lemurheavy/coveralls-ruby) [![Build Status](https://secure.travis-ci.org/lemurheavy/coveralls-ruby.svg?branch=master)](https://travis-ci.org/lemurheavy/coveralls-ruby) [![Gem Version](https://badge.fury.io/rb/coveralls.svg)](http://badge.fury.io/rb/coveralls)

%package bin
Summary: bin components for the rubygem-coveralls package.
Group: Binaries

%description bin
bin components for the rubygem-coveralls package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n coveralls-0.8.13
gem spec %{SOURCE0} -l --ruby > rubygem-coveralls.gemspec

%build
gem build rubygem-coveralls.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
coveralls-0.8.13.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/coveralls-0.8.13.gem
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/README.md
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/bin/coveralls
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/coveralls-ruby.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/lib/coveralls.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/lib/coveralls/api.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/lib/coveralls/command.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/lib/coveralls/configuration.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/lib/coveralls/output.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/lib/coveralls/rake/task.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/lib/coveralls/simplecov.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/lib/coveralls/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/spec/coveralls/configuration_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/spec/coveralls/coveralls_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/spec/coveralls/fixtures/app/controllers/sample.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/spec/coveralls/fixtures/app/models/airplane.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/spec/coveralls/fixtures/app/models/dog.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/spec/coveralls/fixtures/app/models/house.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/spec/coveralls/fixtures/app/models/robot.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/spec/coveralls/fixtures/app/models/user.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/spec/coveralls/fixtures/app/vendor/vendored_gem.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/spec/coveralls/fixtures/sample.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/spec/coveralls/output_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/spec/coveralls/simplecov_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/coveralls-0.8.13/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/specifications/coveralls-0.8.13.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/coveralls
