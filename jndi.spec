Summary:	Java Naming and Directory Interface
Summary(pl):	Interfejs Javy do us³ug katalogowych
Name:		jndi
Version:	1.2.1
Release:	1
License:	Sun Microsystems, Inc. Binary Code License (see COPYRIGHT files!)
Group:		Development/Languages/Java
Source0:	%{name}1_2_1.zip
Source1:	nis1_2_1.zip
Source2:	rmiregistry1_2_1.zip
Source3:	fscontext1_2beta3.zip
Source4:	cosnaming1_2_1.zip
URL:		http://java.sun.com/products/jndi/
Requires:	ldap >= 1.2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Java Naming and Directory Interface.

%description -l pl
Java Naming and Directory Interface - interfejs Javy do us³ug
katalogowych.

%package doc
Summary:	Java Naming and Directory Interface documentation
Summary(pl):	Dokumentacja do Java Naming and Directory Interface
Group:		Development/Languages/Java

%description doc
Java Naming and Directory Interface documentation.

%description doc -l pl
Dokumentacja do Java Naming and Directory Interface.

%prep
%setup -q -c -n %{name}-%{version}/jndi
%setup -q -c -T -n %{name}-%{version}/nis -a1
%setup -q -c -T -n %{name}-%{version}/rmiregistry -a2
%setup -q -c -T -n %{name}-%{version}/fscontext -a3
%setup -q -c -T -n %{name}-%{version}/cosnaming -a4

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
cd ..
install {jndi,nis,rmiregistry,fscontext,cosnaming}/lib/[!p]*.jar \
	$RPM_BUILD_ROOT%{_javalibdir}

mv -f jndi/COPYRIGHT jndi/COPYRIGHT.jndi
mv -f nis/COPYRIGHT nis/COPYRIGHT.nis
mv -f rmiregistry/COPYRIGHT rmiregistry/COPYRIGHT.rmiregistry
mv -f fscontext/COPYRIGHT fscontext/COPYRIGHT.fscontext
mv -f cosnaming/COPYRIGHT cosnaming/COPYRIGHT.cosnaming

gzip -9nf {jndi,nis,rmiregistry,fscontext,cosnaming}/README*
gzip -9nf {jndi,nis,rmiregistry,fscontext,cosnaming}/COPYRIGHT*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ../{jndi,nis,rmiregistry,fscontext,cosnaming}/*.gz
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc ../{jndi,nis,rmiregistry,fscontext,cosnaming}/doc ../{jndi,cosnaming}/examples
