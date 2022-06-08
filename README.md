# docker-python
Using docker and python, conduct data crawling and ETL process.

# dev spec
window 10 home
x64
RAM 8GB
WSL2를 기반으로 Docker Desktop 사용

# dev env setup
1. WSL2 (Windows Subsystem for Linux 2) install
@powershell (관리자 권한으로 하기 커맨드 2 line 실행 후 윈도우 재부팅 > 개발 IDE로 활용한 VDCode를 관리자 권한으로 실행하여 처리함)
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

2. WSL2 Linux 커널 업데이트 패키지 설치
https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi

3. WSL 버전 세팅
wsl --set-default-version 2

4. Docker Desktop 설치
https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=header

5. 