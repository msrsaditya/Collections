import matplotlib.pyplot as plt
import numpy as np

# Data
distributions = [
    "ChromeOS", "Arch Linux", "Ubuntu", "Tails", "Fedora", 
    "Kali Linux", "Linux Mint", "Debian", "Manjaro Linux", "Red Hat",
    "openSUSE", "Gentoo", "NixOS", "elementary OS", "SteamOS", 
    "CentOS", "Qubes OS", "Void Linux", "EndeavourOS", "Kubuntu",
    "Solus Project", "Whonix", "Asahi Linux", "Rocky Linux", "Zorin OS",
    "MX Linux", "KDE neon", "Linux from Scratch", "Nobara Project", "Lubuntu",
    "AlmaLinux", "Garuda Linux", "Slackware", "Parrot OS", "deepin",
    "Alpine Linux", "Guix", "Bedrock Linux", "HoloISO", "ArcoLinux",
    "Puppy Linux", "Clear Linux", "VanillaOS", "KISS Linux", "Pop!_OS",
    "Peppermint OS", "antiX Linux", "Feren OS", "RedStar OS", "Tiny Core Linux",
    "Oracle Linux", "KaOS"
]

popularity = [
    574563, 257395, 227597, 103558, 97561, 94931, 91955, 79747, 69810, 37632,
    31655, 25850, 24437, 23114, 18691, 16573, 15027, 13422, 13030, 11962,
    11233, 8829, 8778, 8220, 7655, 7539, 6491, 6404, 5819, 5562,
    5393, 5276, 5133, 4325, 3501, 3381, 3316, 1891, 1851, 1542,
    1387, 1031, 1026, 972, 713, 628, 562, 521, 355, 284,
    148, 23
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
