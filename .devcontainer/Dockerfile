FROM archlinux

RUN patched_glibc=glibc-linux4-2.33-4-x86_64.pkg.tar.zst && \
    curl -LO "https://repo.archlinuxcn.org/x86_64/$patched_glibc" && \
    bsdtar -C / -xvf "$patched_glibc"
RUN pacman --noconfirm -Sy base-devel git
RUN useradd -Um vscode

RUN pacman --noconfirm -S python python-pip

USER vscode
