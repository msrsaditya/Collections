#!/bin/sh

distros=(
    budgie
    CinnamonDE
    CuteFish
    deepin
    gnome
    kde
    LXQt
    mate
    xfce
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
