#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Alien-Build
Version  : 2.84
Release  : 78
URL      : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-Build-2.84.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-Build-2.84.tar.gz
Summary  : 'Build external dependencies for use in CPAN'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Alien-Build-license = %{version}-%{release}
Requires: perl-Alien-Build-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Capture::Tiny)
BuildRequires : perl(FFI::CheckLib)
BuildRequires : perl(File::Which)
BuildRequires : perl(File::chdir)
BuildRequires : perl(Path::Tiny)
BuildRequires : perl(Term::Table)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Alien::Build - Build external dependencies for use in CPAN
VERSION
version 2.84

%package dev
Summary: dev components for the perl-Alien-Build package.
Group: Development
Provides: perl-Alien-Build-devel = %{version}-%{release}
Requires: perl-Alien-Build = %{version}-%{release}

%description dev
dev components for the perl-Alien-Build package.


%package license
Summary: license components for the perl-Alien-Build package.
Group: Default

%description license
license components for the perl-Alien-Build package.


%package perl
Summary: perl components for the perl-Alien-Build package.
Group: Default
Requires: perl-Alien-Build = %{version}-%{release}

%description perl
perl components for the perl-Alien-Build package.


%prep
%setup -q -n Alien-Build-2.84
cd %{_builddir}/Alien-Build-2.84
pushd ..
cp -a Alien-Build-2.84 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Alien-Build
cp %{_builddir}/Alien-Build-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Alien-Build/21ae9328813972a19be93c9362631cfe02538269 || :
cp %{_builddir}/Alien-Build-%{version}/corpus/cmake-libpalindrome/LICENSE %{buildroot}/usr/share/package-licenses/perl-Alien-Build/f3de9c9b719c6785e72148e6a606dfc96d2d8452 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Alien::Base.3
/usr/share/man/man3/Alien::Base::Authoring.3
/usr/share/man/man3/Alien::Base::FAQ.3
/usr/share/man/man3/Alien::Base::PkgConfig.3
/usr/share/man/man3/Alien::Base::Wrapper.3
/usr/share/man/man3/Alien::Build.3
/usr/share/man/man3/Alien::Build::CommandSequence.3
/usr/share/man/man3/Alien::Build::Interpolate.3
/usr/share/man/man3/Alien::Build::Interpolate::Default.3
/usr/share/man/man3/Alien::Build::Log.3
/usr/share/man/man3/Alien::Build::Log::Abbreviate.3
/usr/share/man/man3/Alien::Build::Log::Default.3
/usr/share/man/man3/Alien::Build::MM.3
/usr/share/man/man3/Alien::Build::Manual.3
/usr/share/man/man3/Alien::Build::Manual::Alien.3
/usr/share/man/man3/Alien::Build::Manual::AlienAuthor.3
/usr/share/man/man3/Alien::Build::Manual::AlienUser.3
/usr/share/man/man3/Alien::Build::Manual::Contributing.3
/usr/share/man/man3/Alien::Build::Manual::FAQ.3
/usr/share/man/man3/Alien::Build::Manual::PluginAuthor.3
/usr/share/man/man3/Alien::Build::Manual::Security.3
/usr/share/man/man3/Alien::Build::Plugin.3
/usr/share/man/man3/Alien::Build::Plugin::Build.3
/usr/share/man/man3/Alien::Build::Plugin::Build::Autoconf.3
/usr/share/man/man3/Alien::Build::Plugin::Build::CMake.3
/usr/share/man/man3/Alien::Build::Plugin::Build::Copy.3
/usr/share/man/man3/Alien::Build::Plugin::Build::MSYS.3
/usr/share/man/man3/Alien::Build::Plugin::Build::Make.3
/usr/share/man/man3/Alien::Build::Plugin::Build::SearchDep.3
/usr/share/man/man3/Alien::Build::Plugin::Core.3
/usr/share/man/man3/Alien::Build::Plugin::Core::CleanInstall.3
/usr/share/man/man3/Alien::Build::Plugin::Core::Download.3
/usr/share/man/man3/Alien::Build::Plugin::Core::FFI.3
/usr/share/man/man3/Alien::Build::Plugin::Core::Gather.3
/usr/share/man/man3/Alien::Build::Plugin::Core::Legacy.3
/usr/share/man/man3/Alien::Build::Plugin::Core::Override.3
/usr/share/man/man3/Alien::Build::Plugin::Core::Setup.3
/usr/share/man/man3/Alien::Build::Plugin::Core::Tail.3
/usr/share/man/man3/Alien::Build::Plugin::Decode.3
/usr/share/man/man3/Alien::Build::Plugin::Decode::DirListing.3
/usr/share/man/man3/Alien::Build::Plugin::Decode::DirListingFtpcopy.3
/usr/share/man/man3/Alien::Build::Plugin::Decode::HTML.3
/usr/share/man/man3/Alien::Build::Plugin::Decode::Mojo.3
/usr/share/man/man3/Alien::Build::Plugin::Digest.3
/usr/share/man/man3/Alien::Build::Plugin::Digest::Negotiate.3
/usr/share/man/man3/Alien::Build::Plugin::Digest::SHA.3
/usr/share/man/man3/Alien::Build::Plugin::Digest::SHAPP.3
/usr/share/man/man3/Alien::Build::Plugin::Download.3
/usr/share/man/man3/Alien::Build::Plugin::Download::Negotiate.3
/usr/share/man/man3/Alien::Build::Plugin::Extract.3
/usr/share/man/man3/Alien::Build::Plugin::Extract::ArchiveTar.3
/usr/share/man/man3/Alien::Build::Plugin::Extract::ArchiveZip.3
/usr/share/man/man3/Alien::Build::Plugin::Extract::CommandLine.3
/usr/share/man/man3/Alien::Build::Plugin::Extract::Directory.3
/usr/share/man/man3/Alien::Build::Plugin::Extract::File.3
/usr/share/man/man3/Alien::Build::Plugin::Extract::Negotiate.3
/usr/share/man/man3/Alien::Build::Plugin::Fetch.3
/usr/share/man/man3/Alien::Build::Plugin::Fetch::CurlCommand.3
/usr/share/man/man3/Alien::Build::Plugin::Fetch::HTTPTiny.3
/usr/share/man/man3/Alien::Build::Plugin::Fetch::LWP.3
/usr/share/man/man3/Alien::Build::Plugin::Fetch::Local.3
/usr/share/man/man3/Alien::Build::Plugin::Fetch::LocalDir.3
/usr/share/man/man3/Alien::Build::Plugin::Fetch::NetFTP.3
/usr/share/man/man3/Alien::Build::Plugin::Fetch::Wget.3
/usr/share/man/man3/Alien::Build::Plugin::Gather.3
/usr/share/man/man3/Alien::Build::Plugin::Gather::IsolateDynamic.3
/usr/share/man/man3/Alien::Build::Plugin::PkgConfig.3
/usr/share/man/man3/Alien::Build::Plugin::PkgConfig::CommandLine.3
/usr/share/man/man3/Alien::Build::Plugin::PkgConfig::LibPkgConf.3
/usr/share/man/man3/Alien::Build::Plugin::PkgConfig::MakeStatic.3
/usr/share/man/man3/Alien::Build::Plugin::PkgConfig::Negotiate.3
/usr/share/man/man3/Alien::Build::Plugin::PkgConfig::PP.3
/usr/share/man/man3/Alien::Build::Plugin::Prefer.3
/usr/share/man/man3/Alien::Build::Plugin::Prefer::BadVersion.3
/usr/share/man/man3/Alien::Build::Plugin::Prefer::GoodVersion.3
/usr/share/man/man3/Alien::Build::Plugin::Prefer::SortVersions.3
/usr/share/man/man3/Alien::Build::Plugin::Probe.3
/usr/share/man/man3/Alien::Build::Plugin::Probe::CBuilder.3
/usr/share/man/man3/Alien::Build::Plugin::Probe::CommandLine.3
/usr/share/man/man3/Alien::Build::Plugin::Probe::Vcpkg.3
/usr/share/man/man3/Alien::Build::Plugin::Test.3
/usr/share/man/man3/Alien::Build::Plugin::Test::Mock.3
/usr/share/man/man3/Alien::Build::Temp.3
/usr/share/man/man3/Alien::Build::Util.3
/usr/share/man/man3/Alien::Build::Version::Basic.3
/usr/share/man/man3/Alien::Build::rc.3
/usr/share/man/man3/Alien::Role.3
/usr/share/man/man3/Alien::Util.3
/usr/share/man/man3/Test::Alien.3
/usr/share/man/man3/Test::Alien::Build.3
/usr/share/man/man3/Test::Alien::CanCompile.3
/usr/share/man/man3/Test::Alien::CanPlatypus.3
/usr/share/man/man3/Test::Alien::Diag.3
/usr/share/man/man3/Test::Alien::Run.3
/usr/share/man/man3/Test::Alien::Synthetic.3
/usr/share/man/man3/alienfile.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Alien-Build/21ae9328813972a19be93c9362631cfe02538269
/usr/share/package-licenses/perl-Alien-Build/f3de9c9b719c6785e72148e6a606dfc96d2d8452

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
