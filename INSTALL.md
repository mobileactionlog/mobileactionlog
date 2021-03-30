# Installation Instructions

* [Mobile ActionLog Android App](#app)
* [Mobile ActionLog SyncServer](#sync)
    * [Java Development Kit (JDK)](#jdk)
    * [MySQL Server](#mysql)
    * [Install and Configure SyncServer Software](#server)
        * [Security and Admin PIN](#pin)
        * [Database connection](#db)
        * [Logging](#logging)
        * [Authentication](#auth)
        * [Background image map support](#map)
        * [AIS-Grid Mothership MMSI](#mothership)
    
# Mobile ActionLog Android App {#app}

## Prerequisites

Open the Android settings and switch to the "Security" settings menu.
Toggle the settings for "Installation from unknown sources" to allow the
installation of packages not downloaded from the Google Play Store.

## Device Requirements

This Android App was designed for the following devices:

* XSLATE(tm) D10 from XPLORE Technologies with Android 6.0.1 and at least 4GB RAM
* Samsung Galaxy XCover Pro with Android 10 and at least 4 GB RAM
* CAT S52 with Android 9 or 10 and at least 4 GB RAM

# Mobile ActionLog SyncServer {#sync}

## Prerequisites

The SyncServer is a native Java 11 application, and can be run on Windows, MacOS and Linux.
Installation instructions and support is only provided for Windows.

## Java Runtime Environment {#jdk}

The Mobile ActionLog SyncServer should run on all major operating systems 
and requires only a Java Development Kit (JDK) version 11 to run.

To check if a JDK has already been installed on your system,
and if the environment variable `JAVA_HOME` is set, 
run the following command in your console and check its output.

```bash
"%JAVA_HOME%"\bin\java.exe -version
openjdk version "11.0.2" 2019-01-15
OpenJDK Runtime Environment 18.9 (build 11.0.2+9)
OpenJDK 64-Bit Server VM 18.9 (build 11.0.2+9, mixed mode)
```

If Java has not been installed on your system, or if the installed version is not at least 11.0.2,
then please download an up-to-date java JDK, e.g. from this URL:

https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_windows-x64_bin.zip

### Installing the JDK.

Extract the downloaded JDK archive into a folder, e.g.

`C:\Program Files\Java`

and set your `JAVA_HOME` environment variable to the installed Java version as follows

```bash
setx JAVA_HOME "C:\Program Files\Java\jdk-11.0.2"
```

**Note**: Close and re-open your console afterwards, so that the setting becomes active.

It is important to repeat the first check of these instructions 
to verify the successful installation of the new JDK:

```bash
"%JAVA_HOME%"\bin\java.exe -version
openjdk version "11.0.2" 2019-01-15
OpenJDK Runtime Environment 18.9 (build 11.0.2+9)
OpenJDK 64-Bit Server VM 18.9 (build 11.0.2+9, mixed mode)
```


## MySQL Server {#mysql}

The Mobile ActionLog SyncServer requires a connection to a MySQL Server 8 instance.
If a MySQL Server is not installed on the SyncServer machine,
please follow the instructions of section 2.3.4 of the MySQL Server Manual.

* You can find the MySQL Server Manual online at https://dev.mysql.com/doc/.
* The MySQL Server software can be downloaded from https://dev.mysql.com/downloads/mysql/.

## Installing the Mobile ActionLog SyncServer software {#server}

The archive providing the SyncServer part of the software should be included in the deliverable.
The filename of the archive is called `MobileActionLog-SyncServer-Full-<version>.zip`.

### Extract the zip or tar file

Extract the file `MobileActionLog-SyncServer-Full-<version>.zip` into a directory of your choice, e.g.

```
C:\Program Files\MobileActionLog
```

### Configure the database connection and SyncServer settings

The configuration file is located in the following folder, if you followed the instruction in the previous section:
```
C:\Program Files\MobileActionLog\MobileActionLog-SyncServer-<version>\etc\application.yaml
```

The default configuration file included in the archive contains fields that need to be filled to
ensure correct working of the SyncServer:

```bash
mobileactionlog:
    app:
        # Security and admin pin of the Apps. Must adhere to pattern [0-9]{4} (4 digits)
        adminPin: "<insert admin pin here>"
        securityPin: "<insert security pin here>"

        # MMSI of the mothership. Must adhere to pattern [0-9]{9} (9 digits)
        mmsiMothership: "<insert mmsi of the mothership here>"
        maps: "<insert path to folder with maps>"
        writerUsername: "<insert writer username here>"
        writerPassword: "<insert writer password-hash generated with 'htpasswd -nbB username password' here>"
        adminUsername: "<insert admin username here>"
        adminPassword: "<insert admin password-hash generated with 'htpasswd -nbB username password' here>"
    database:
        mysql:
            host: localhost
            port: 3306
            schema: mobileactionlog
            user: "<insert user name>"
            password: "<insert password here>"
logging:
    file:
        path: "<insert absolute path of log directory here>"
```

#### Configure up admin and security PIN {#pin}

The admin view and grid deletion view are protected by two different 4-digit PIN codes.
The codes are configured in the `application.yaml` on the SyncServer.

When syncing the tablet with the SyncServer, 
the PIN codes are updated in the Mobile ActionLog Andoid app.

The admin pin is configured in the field `adminPin` and controls the access to the 
**Note:**
- The initial PIN configured on the FloeNavi app, for both admin and security pin, is **0000**.

#### Configure the database connection {#db}

The Mobile ActionLog SyncServer requires a connection to a MySQL Server.
The connection information is configured in the `application.yaml` on the SyncServer.

In the configuration tree, the fields in the path `mobileactionlog`->`database`->`mysql`:

| Field | Description | Default|
| :---: | --- | :---: |
| `host` | hostname of the MySQL Server | `localhost` |
| `port` | port on the MySQL Server | `3306` |
| `schema` | the DB schema to use | `mobileactionlog`
| `user` | the DB user to use to connect | |
| `password` | the password used by the DB user to connect | |

```bash
mobileactionlog:
    database:
        mysql:
            host: localhost
            port: 3306
            schema: mobileactionlog
            user: "<insert user name>"
            password: "<insert password here>"
```

**Notes**:

* The database user needs full access to the used database and schema,
  to be able to create and alter the database and tables.

* The database user should not be the instance administrator (db root account).

* Using the values for `host` and `port`, it is possible to set up a connection to a database
running on a different machine in a network.

* The SyncServer will create the required database if the user has to corresponding permission.
  In addition, the SyncServer will automatically create all required tables in the database
  during the first run.

### Logging and Logfiles {#logging}

The SyncServer logs errors and events, i.e. synchronization of device operations, into a dedicated log file.

The directory for the log files is configured in the `application.yaml` on the SyncServer host.

The corresponding configuration option is in the tree `logging`->`file`->`path`.
The path must be set to a writable location on the SyncServer host.
It is recommended to set a full path, e.g.

```bash
logging:
    file:
        path: "C:\\Logs\\MobileActionLog"
```

**Notes**:

* Escaping spaces in the filename is tricky. 
  A space in the filename needs to be escaped with a single `\` (backslash).
  On Windows, the directory separator backslash '\' can either be escaped with '\\', or with a forward slash '/'.
  
* The directory needs to be writable without specific administration permissions. The windows
  directory `C:\\Program Files` is protected. The SyncServer is typically not able to create
  directories and log files there.
  
#### Authentication {#auth}

Writing access to the REST endpoints, and the Web UI of the SyncServer is restricted.
Both the Android app and users have to login with `username` and `password` to acquire access to the
SyncServer.

The username and password is configured in the `application.yaml` on the SyncServer host.
Passwords are stored in a hashed format and not in cleartext. Typically, an external tool is used
to create the hashes for the passwords.

For this guide it is assumed that the executable `htpasswd.exe` from the apache web-server tools is available. The
functionality to create hashes is also available online and included in scripting languages such as python.

The SyncServer allows to set up two different roles: `writer` and `admin`.

It is recommended to use the role `writer` for the connection of the Android app, and the role `admin` for
use with the Web UI of the SyncServer.

To create a password hash, use the `htpasswd.exe` executable, 
e.g. for the username `awi` and the password `secret`.

```bash
htpasswd -nbB awi secret
awi:$2y$05$94NXEcMMtJAnxheuTcsLRe0.yXXmpH.NnSqWev71s6iPizkCkELj2
```

The output format corresponds to the `.htpasswd` files used by the apache web-server:
`username:password-hash`. Only copy the hash-part of the output into the `application.yaml`.

```bash
        writerUsername: "awi"
        writerPassword: "$2y$05$94NXEcMMtJAnxheuTcsLRe0.yXXmpH.NnSqWev71s6iPizkCkELj2"
```

#### Background image map support {#map}

When the system is set to work with an AIS-Grid,
the Android app supports displaying an image in the background of the map.

The directory from where the image and metadata files are uploaded to the app is configured
in the `application.yaml` on the SyncServer host.

The field `mobileactionlog`->`app`->`maps` must point to a readably directory on the SyncServer host, e.g.

```bash
mobileactionlog:
    app:
...
        maps: "C:\\Program\ Files\\MobileActionLog\\Maps"
...
```

**Notes**:

* Escaping spaces in the filename is tricky. 
  A space in the filename needs to be escaped with a single `\` (backslash).

* Instructions on how to calibrate the map are included in the [Administrator Guide](ADMIN_GUIDE.html)

#### AIS-Grid Mothership MMSI {#mothership}

When the system is set to work with an AIS-Grid,
the Android app supports displaying the Mothership AIS transponder with a dedicated icon.

For this, the MMSI of the mothership needs to be configured in the `application.yaml` on the SyncServer host,
in the field `mobileactionlog`->`app`->`mmsiMothership`, e.g. `211202460` for Polarstern.


