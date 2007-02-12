%define	jndi_ver	1.2.1
%define	nis_ver		1.2.1
%define	rmi_ver		1.2.1
%define	fs_ver		1.2
%define	fs_ver2		beta3
%define	cos_ver		1.2.1
%define	ldap_ver	1.2.4
%define	dns_ver		1.2
%define	dsml_ver	1.2
Summary:	Java Naming and Directory Interface
Summary(pl.UTF-8):   Interfejs Javy do usług katalogowych
Name:		jndi
Version:	%{jndi_ver}
Release:	1
License:	restricted, non-distributable (see COPYRIGHT)
Group:		Development/Languages/Java
Source0:	%{name}-%(echo %{jndi_ver} | tr . _).zip
Source1:	nis-%(echo %{nis_ver} | tr . _).zip
Source2:	rmiregistry-%(echo %{rmi_ver} | tr . _).zip
Source3:	fscontext-%(echo %{fs_ver} | tr . _)-%{fs_ver2}.zip
Source4:	cosnaming-%(echo %{cos_ver} | tr . _).zip
Source5:	ldap-%(echo %{ldap_ver} | tr . _).zip
Source6:	dns-%(echo %{dns_ver} | tr . _).zip
Source7:	dsmlv1-%(echo %{dsml_ver} | tr . _).zip
URL:		http://java.sun.com/products/jndi/
NoSource:	0
NoSource:	1
NoSource:	2
NoSource:	3
NoSource:	4
NoSource:	5
NoSource:	6
NoSource:	7
BuildRequires:	unzip
Requires:	jre >= 1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java
# turns off confirmations (but it doesn't work, WHY???)
%define		__unzip		unzip -o -q

%description
Java Naming and Directory Interface.

%description -l pl.UTF-8
Java Naming and Directory Interface - interfejs Javy do usług
katalogowych.

%package provider-nis
Summary:	Java Naming and Directory Interface - NIS Service Provider
Summary(pl.UTF-8):   Interfejs Javy do usług katalogowych - obsługa NIS
Version:	%{nis_ver}
Group:		Development/Languages/Java
Requires:	jndi >= 1.2

%description provider-nis
Java Naming and Directory Interface - NIS Service Provider.

%description provider-nis -l pl.UTF-8
Interfejs Javy do usług katalogowych - obsługa NIS.

%package provider-rmiregistry
Summary:	Java Naming and Directory Interface - RMI Registry Service Provider
Summary(pl.UTF-8):   Interfejs Javy do usług katalogowych - obsługa rejestru RMI
Version:	%{rmi_ver}
Group:		Development/Languages/Java
Requires:	jndi >= 1.2

%description provider-rmiregistry
Java Naming and Directory Interface - Remote Method Invocation
Registry Service Provider.

%description provider-rmiregistry -l pl.UTF-8
Interfejs Javy do usług katalogowych - obsługa rejestru RMI (Remote
Method Invocation).

%package provider-fscontext
Summary:	Java Naming and Directory Interface - File System Service Provider
Summary(pl.UTF-8):   Interfejs Javy do usług katalogowych - obsługa systemu plików
Version:	%{fs_ver}
Group:		Development/Languages/Java
Requires:	jndi >= 1.2

%description provider-fscontext
Java Naming and Directory Interface - File System Service Provider.

%description provider-fscontext -l pl.UTF-8
Interfejs Javy do usług katalogowych - obsługa systemu plików.

%package provider-cosnaming
Summary:	Java Naming and Directory Interface - COS Naming Service Provider
Summary(pl.UTF-8):   Interfejs Javy do usług katalogowych - obsługa COS
Version:	%{cos_ver}
Group:		Development/Languages/Java
Requires:	jndi >= 1.2

%description provider-cosnaming
Java Naming and Directory Interface - COS Naming Service Provider.

%description provider-cosnaming -l pl.UTF-8
Interfejs Javy do usług katalogowych - obsługa COS.

%package provider-ldap
Summary:	Java Naming and Directory Interface - LDAP Service Provider
Summary(pl.UTF-8):   Interfejs Javy do usług katalogowych - obsługa LDAP
Version:	%{ldap_ver}
Group:		Development/Languages/Java
Requires:	jaas >= 1.0
Requires:	jndi >= 1.2
Obsoletes:	ldap

%description provider-ldap
Java Naming and Directory Interface - LDAP Service Provider.

%description provider-ldap -l pl.UTF-8
Interfejs Javy do usług katalogowych - obsługa LDAP.

%package provider-dns
Summary:	Java Naming and Directory Interface - DNS Service Provider
Summary(pl.UTF-8):   Interfejs Javy do usług katalogowych - obsługa DNS
Version:	%{dns_ver}
Group:		Development/Languages/Java
Requires:	jndi >= 1.2
Requires:	jre >= 1.2

%description provider-dns
Java Naming and Directory Interface - DNS Service Provider.

%description provider-dns -l pl.UTF-8
Interfejs Javy do usług katalogowych - obsługa DNS.

%package provider-dsmlv1
Summary:	Java Naming and Directory Interface - DSMLv1 Service Provider
Summary(pl.UTF-8):   Interfejs Javy do usług katalogowych - obsługa DSMLv1
Version:	%{dsml_ver}
Group:		Development/Languages/Java
Requires:	jndi >= 1.2

%description provider-dsmlv1
Java Naming and Directory Interface - DSMLv1 Service Provider.

%description provider-dsmlv1 -l pl.UTF-8
Interfejs Javy do usług katalogowych - obsługa DSMLv1.

%package doc
Summary:	Java Naming and Directory Interface documentation
Summary(pl.UTF-8):   Dokumentacja do Java Naming and Directory Interface
Group:		Development/Languages/Java

%description doc
Java Naming and Directory Interface documentation.

%description doc -l pl.UTF-8
Dokumentacja do Java Naming and Directory Interface.

%prep
# fortunately 7 COPYRIGHT files (except dsml) are the same
%setup -q -c -a1 -a2 -a3 -a4 -a5 -a6
mkdir dsml
%{__unzip} %{SOURCE7} -d dsml
mv -f dsml/doc/providers/* doc/providers
# most recent providerutil.jar is in dsmlv1 package
mv -f dsml/lib/* lib

# this one is in separate package
rm -f lib/jaas.jar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}

install lib/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT README.txt
%{_javalibdir}/jndi.jar
%{_javalibdir}/providerutil.jar

%files provider-nis
%defattr(644,root,root,755)
%doc README-NIS.txt
%{_javalibdir}/nis.jar

%files provider-rmiregistry
%defattr(644,root,root,755)
%doc README-RMIRegistry.txt
%{_javalibdir}/rmiregistry.jar

%files provider-fscontext
%defattr(644,root,root,755)
%doc README-FS.txt
%{_javalibdir}/fscontext.jar

%files provider-cosnaming
%defattr(644,root,root,755)
%doc README-COS.txt
%{_javalibdir}/cosnaming.jar

%files provider-ldap
%defattr(644,root,root,755)
%doc README-LDAP.txt
%{_javalibdir}/ldap*.jar

%files provider-dns
%defattr(644,root,root,755)
%doc README-DNS.txt
%{_javalibdir}/dns.jar

%files provider-dsmlv1
%defattr(644,root,root,755)
%doc dsml/COPYRIGHT dsml/README-DSML.txt
%{_javalibdir}/dsml.jar

%files doc
%defattr(644,root,root,755)
%doc doc examples
