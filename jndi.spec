Summary:	Java Nameing and Directory Inteface
Name:		jndi
Version:	1.2.1
Release:	1
License:	Sun Microsystems, Inc. Binary Code License (see COPYRIGHT files!!!)
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Source0:	jndi1_2_1.zip
Source1:	nis1_2_1.zip
Source2:	rmiregistry1_2_1.zip
Source3:	fscontext1_2beta3.zip
Source4:	cosnaming1_2_1.zip
Requires:	ldap >= 1.2.3
URL:		http://java.sun.com/products/jndi/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Java Nameing and Directory Inteface

%package doc
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Summary:	Java Nameing and Directory Inteface documentation

%description doc
Java Nameing and Directory Inteface documentation

%prep
%setup -q -c -n %{name}-%{version}/jndi
%setup -q -c -T -n %{name}-%{version}/nis -a1
%setup -q -c -T -n %{name}-%{version}/rmiregistry -a2
%setup -q -c -T -n %{name}-%{version}/fscontext -a3
%setup -q -c -T -n %{name}-%{version}/cosnaming -a4

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_javalibdir}
cd ..
cp {jndi,nis,rmiregistry,fscontext,cosnaming}/lib/[!p]*.jar \
	$RPM_BUILD_ROOT/%{_javalibdir}

cp jndi/COPYRIGHT jndi/COPYRIGHT.jndi
cp nis/COPYRIGHT nis/COPYRIGHT.nis
cp rmiregistry/COPYRIGHT rmiregistry/COPYRIGHT.rmiregistry
cp fscontext/COPYRIGHT fscontext/COPYRIGHT.fscontext
cp cosnaming/COPYRIGHT cosnaming/COPYRIGHT.cosnaming

gzip -9nf {jndi,nis,rmiregistry,fscontext,cosnaming}/README* 
gzip -9nf {jndi,nis,rmiregistry,fscontext,cosnaming}/COPYRIGHT*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ../{jndi,nis,rmiregistry,fscontext,cosnaming}/*.gz
%dir %{_javalibdir}
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc ../{jndi,nis,rmiregistry,fscontext,cosnaming}/doc ../{jndi,cosnaming}/examples
