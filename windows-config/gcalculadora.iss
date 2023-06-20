; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "GCalculadora"
#define MyAppVersion "0.6"
#define MyAppPublisher "ArtesGC, Inc."
#define MyAppURL "https://artesgc.home.blog/"
#define MyAppExeName "gcalculadora.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{39521B08-0980-4715-8713-AC452AD6E7F8}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
AppCopyright={#MyAppPublisher}
AppVerName={#MyAppVersion}
VersionInfoCompany={#MyAppPublisher}
VersionInfoCopyright=2019-2021 {#MyAppPublisher}
VersionInfoOriginalFileName={#MyAppExeName}
VersionInfoProductName={#MyAppName}
VersionInfoProductTextVersion={#MyAppVersion}
VersionInfoProductVersion={#MyAppVersion}
VersionInfoVersion={#MyAppVersion}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
; The [Icons] "quicklaunchicon" entry uses {userappdata} but its [Tasks] entry has a proper IsAdminInstallMode Check.
UsedUserAreasWarning=no
LicenseFile=.\LICENSE
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
OutputDir=.\dist\
OutputBaseFilename=GCalculadora_{#MyAppVersion}-082021_amd64
SetupIconFile=.\img\favicons\favicon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "portuguese"; MessagesFile: "compiler:Languages\Portuguese.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 6.1; Check: not IsAdminInstallMode

[Files]
Source: "C:\Users\nurul\Documents\Projectos\GCalculadora\dist\gcalculadora.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\nurul\Documents\Projectos\GCalculadora\dist\fonts\*"; DestDir: "{app}\fonts"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\nurul\Documents\Projectos\GCalculadora\dist\img\*"; DestDir: "{app}\img"; Flags: ignoreversion recursesubdirs createallsubdirs  
Source: "C:\Users\nurul\Documents\Projectos\GCalculadora\dist\img\favicons\*"; DestDir: "{app}\img\favicons"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\nurul\Documents\Projectos\GCalculadora\dist\img\icons\*"; DestDir: "{app}\img\icons"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\nurul\Documents\Projectos\GCalculadora\dist\themes\*"; DestDir: "{app}\themes"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\nurul\Documents\Projectos\GCalculadora\gcalculadora.ini"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\nurul\Documents\Projectos\GCalculadora\LICENSE"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

