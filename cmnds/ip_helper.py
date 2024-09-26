class IpCalculator:
    def __init__(self, ip):
        self.block = 0xFFFFFFFF
        self.sub_block = 0xFF
        self.ip_size = 32
        self.ip = ip

    def get_ip_range(self):
        ip_str, prefix_len_str = self.ip.split('/')
        ip_int = self.__ip_to_int(ip_str)
        prefix_len = int(prefix_len_str)
        mask_int = (self.block << (self.ip_size - prefix_len)) & self.block
        network_int = ip_int & mask_int
        broadcast_int = network_int | (~mask_int & self.block)
        if prefix_len < self.ip_size:
            first_ip_int = network_int + 1
            last_ip_int = broadcast_int - 1
        else:
            first_ip_int = network_int
            last_ip_int = broadcast_int
        total_hosts = max(0, last_ip_int - first_ip_int + 1)
        network_ip = self.__int_to_ip(network_int)
        broadcast_ip = self.__int_to_ip(broadcast_int)
        first_ip = self.__int_to_ip(first_ip_int)
        last_ip = self.__int_to_ip(last_ip_int)

        return {
            'network_address': network_ip,
            'broadcast_address': broadcast_ip,
            'first_usable_ip': first_ip,
            'last_usable_ip': last_ip,
            'total_usable_hosts': total_hosts
        }

    def __ip_to_int(self, str_ip):
        octets = [int(octet) for octet in str_ip.split('.')]
        ip_int = (octets[0] << 24) | (octets[1] << 16) | (octets[2] << 8) | octets[3]
        return ip_int

    def __int_to_ip(self, ip_int):
        return ".".join(str((ip_int >> (8 * i)) & self.sub_block) for i in reversed(range(4)))
