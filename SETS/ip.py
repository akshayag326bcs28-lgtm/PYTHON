def input_ips(prompt):
    ips = input(prompt)
    # Convert input string to a set of trimmed IP addresses
    return set(ip.strip() for ip in ips.split(','))

# Input sets of IP addresses
L = input_ips("Enter logged in successfully IPs (comma-separated): ")
F = input_ips("Enter failed login attempt IPs (comma-separated): ")
B = input_ips("Enter blacklisted IPs (comma-separated): ")

# 1. IPs that appear in both successful and failed logins but are not blacklisted
ips_both_not_blacklisted = (L.intersection(F)).difference(B)

# 2. IPs that attempted access but never succeeded
ips_attempted_never_succeeded = F.difference(L)

# 3. IPs that are only blacklisted and never attempted login
ips_blacklisted_never_attempted = B.difference(L.union(F))

print("\nIPs with both successful and failed logins but not blacklisted:", ips_both_not_blacklisted)
print("IPs that attempted access but never succeeded:", ips_attempted_never_succeeded)
print("IPs only blacklisted and never attempted login:", ips_blacklisted_never_attempted)
