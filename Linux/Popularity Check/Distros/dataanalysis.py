import matplotlib.pyplot as plt
import numpy as np

# Data
distributions = [
    "ChromeOS", "Arch Linux", "Ubuntu", "Tails", "Fedora", 
    "Kali Linux", "Linux Mint", "Debian", "Pop!_OS", "Manjaro Linux",
    "Red Hat", "openSUSE", "Gentoo", "NixOS", "elementary OS", 
    "SteamOS", "CentOS", "Qubes OS", "Void Linux", "EndeavourOS", 
    "Kubuntu", "Solus Project", "Whonix", "Asahi Linux", "Rocky Linux",
    "Zorin OS", "MX Linux", "KDE neon", "Linux from Scratch", 
    "Nobara Project", "Lubuntu", "AlmaLinux", "Xubuntu", "Garuda Linux",
    "Slackware", "Parrot OS", "deepin", "Alpine Linux", "Guix",
    "CrunchBang", "Bedrock Linux", "HoloISO", "ArcoLinux", "Antergos",
    "CrunchBangplusplus", "Puppy Linux", "Raspbian", "BlackArch Official",
    "Clear Linux", "VanillaOS", "KISS Linux", "CachyOS", "Peppermint OS",
    "Mageia", "Parabola", "antiX Linux", "Bodhi Linux", "Feren OS",
    "Linux Lite", "Official Arch Labs Linux", "RedStar OS", "Tiny Core Linux",
    "GeckoLinux", "Sabayon", "Q4OS", "RhinoLinux", "BackBox", "ArchBang",
    "Oracle Linux", "OpenMandriva", "Crux Linux", "Exherbo", "Kinoite",
    "Scientific Linux", "Venom Linux", "Anarchy Linux", "RLXOS Dev",
    "KaOS", "Alt Linux"
]

popularity = [
    574558, 257468, 227640, 103580, 97604, 94980, 92018, 79775, 70207, 69815,
    37646, 31677, 25855, 24463, 23115, 18698, 16571, 15037, 13426, 13038,
    11966, 11234, 8834, 8784, 8222, 7662, 7541, 6489, 6406, 5830, 5561,
    5395, 5391, 5276, 5134, 4328, 3502, 3390, 3317, 2046, 1891, 1853,
    1540, 1491, 1487, 1390, 1215, 1092, 1031, 1028, 972, 642, 628,
    612, 577, 563, 543, 521, 435, 392, 356, 285, 202, 201,
    196, 165, 160, 156, 148, 147, 137, 102, 90, 58, 53,
    40, 35, 23, 15
]

# Bar Plot
plt.figure(figsize=(12, 8))
plt.barh(distributions, popularity, color='skyblue')
plt.xlabel('Popularity')
plt.ylabel('Linux Distributions')
plt.title('Popularity of Linux Distributions')
plt.tight_layout()
plt.show()

# Pie Chart
plt.figure(figsize=(10, 10))
plt.pie(popularity, labels=distributions, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Distribution of Popularity Among Linux Distributions')
plt.tight_layout()
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(popularity, bins=20, color='lightgreen', edgecolor='black')
plt.xlabel('Popularity')
plt.ylabel('Frequency')
plt.title('Distribution of Popularity Scores')
plt.tight_layout()
plt.show()

# Ranking
sorted_indices = np.argsort(popularity)[::-1]
sorted_distributions = [distributions[i] for i in sorted_indices]
sorted_popularity = [popularity[i] for i in sorted_indices]

print("\nRanking of Linux Distributions:")
for i, dist in enumerate(sorted_distributions):
    print(f"{i+1}. {dist}: {sorted_popularity[i]}")
