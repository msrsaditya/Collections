#!/bin/sh

distros=(
    "AlmaLinux"
    "AlpineLinux"
    "antiXLinux"
    "archlinux"
    "ArcoLinux"
    "AsahiLinux"
    "bedrocklinux"
    "CentOS"
    "chromeos"
    "ClearLinux"
    "debian"
    "deepin"
    "elementaryos"
    "EndeavourOS"
    "Fedora"
    "FerenOS"
    "GarudaLinux"
    "Gentoo"
    "GUIX"
    "holoiso"
    "kaos"
    "Kalilinux"
    "Kubuntu"
    "kisslinux"
    "kdeneon"
    "Lubuntu"
    "linuxfromscratch"
    "linuxmint"
    "ManjaroLinux"
    "MXLinux"
    "NixOS"
    "NobaraProject"
    "openSUSE"
    "OracleLinux"
    "ParrotOS"
    "PeppermintOS"
    "popos"
    "puppylinux"
    "Qubes"
    "RedStarOS"
    "redhat"
    "RockyLinux"
    "slackware"
    "SolusProject"
    "SteamOS"
    "tails"
    "tinycorelinux"
    "Ubuntu"
    "vanillaos"
    "voidlinux"
    "Whonix"
    "zorinos"
)

printf "\n"
printf "Fetched "

for distro in "${distros[@]}"; do
    curl -s -o "$distro.html" "https://www.reddit.com/r/$distro/?rdt=11111"
    printf "%s, " "$distro"
done

printf "\n\nPopularity is as Follows:\n\n"

for distro in "${distros[@]}"; do
    number=$(grep -m 1 '<faceplate-number number' "$distro.html" | awk -F'"' '{print $2}')
    echo "$distro: $number"
done | sort -t ':' -k2nr

rm -rf *.html
