
def get_ip_range(ip):
    ip_str, prefix_len_str = ip.split('/')
    ip_int = __ip_to_int(ip_str)
    prefix_len = int(prefix_len_str)
    mask_int = (0xFFFFFFFF << (32 - prefix_len)) & 0xFFFFFFFF
    network_int = ip_int & mask_int
    broadcast_int = network_int | (~mask_int & 0xFFFFFFFF)
    if prefix_len < 32:
        first_ip_int = network_int + 1
        last_ip_int = broadcast_int -1
    else:
        first_ip_int = network_int
        last_ip_int = broadcast_int
    total_hosts = max(0, last_ip_int - first_ip_int + 1)
    network_ip = __int_to_ip(network_int)
    broadcast_ip = __int_to_ip(broadcast_int)
    first_ip = __int_to_ip(first_ip_int)
    last_ip = __int_to_ip(last_ip_int)

    return {
        'network_address': network_ip,
        'broadcast_address': broadcast_ip,
        'first_usable_ip': first_ip,
        'last_usable_ip': last_ip,
        'total_usable_hosts': total_hosts
    }


def __ip_to_int(str_ip):
    octets = [int(octet) for octet in str_ip.split('.')]
    ip_int = (octets[0] << 24) | (octets[1] << 16) | (octets[2] << 8) | octets[3]
    return ip_int


def __int_to_ip(ip_int):
    return ".".join(str((ip_int >> (8 * i)) & 0xFF) for i in reversed(range(4)))
