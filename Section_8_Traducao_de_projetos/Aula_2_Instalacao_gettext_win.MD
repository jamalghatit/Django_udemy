# Instalando e configurando o gettext - Windows

- Habilitar o shell do linux no windows
Para saber sobre o brew = https://brew.sh/index_pt-br

Linuxbrew is a clone of homebrew, the MacOS package manager, for Linux, which allows users to install software to their home directory.

It’s feature set includes:

- Allowing installation of packages to a home directory without root access.
- Supports installing of third-party software (not packaged on the native distributions).
- Supports installing of up-to-date versions of packages when the one provided in the distro repositories is old.
- In addition, brew allows you to manage packages on both your Mac and Linux machines.

Para instalar:

```bash

\$ sudo apt-get install build-essential procps curl file git
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
$ test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)
$ test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
$ test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.bash_profile
$ echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile

$ brew update

$ brew upgrade

$ brew install gettext

$ brew link gettext --force
```

Instalar o poedit, por meio de download no site
O gettext é necessário para que o django consiga alternar entre as traduções.
O poedit é um editor de traduções.

Poedit provides translators and developers with a powerful and intuitive editor for gettext. It helps save time on mundane translation tasks with a lightweight and easy-to-use interface and smart features like pre-translation and machine translation.