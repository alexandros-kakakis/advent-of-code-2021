import math

def hex_to_binary(hex):
    expected_len = len(hex) * 4
    return bin(int(hex, 16))[2:].zfill(expected_len)

def binary_to_int(binary):
    return int(binary, 2)

def parse_packet(binary, i=0, total=None):
    global version_sum

    version_sum += binary_to_int( binary[i:i+3] )
    i += 3
    
    type_id = binary_to_int( binary[i:i+3] )
    i += 3

    if type_id == 4:
        binary, i, total = parse_literal(binary, i, total)
    else:
        if type_id == 0:
            operation = lambda x: sum(x)
        elif type_id == 1:
            operation = lambda x: math.prod(x)
        elif type_id == 2:
            operation = lambda x: min(x)
        elif type_id == 3:
            operation = lambda x: max(x)
        elif type_id == 5:
            operation = lambda x: 1 if x[0] > x[1] else 0
        elif type_id == 6:
            operation = lambda x: 1 if x[0] < x[1] else 0
        elif type_id == 7:
            operation = lambda x: 1 if x[0] == x[1] else 0
        
        binary, i, total = parse_operator(binary, i, total, operation)

    return binary, i, total

def parse_literal(binary, i, total):
    literal_value = ''
    while True:
        if binary[i] == '1':
            literal_value += binary[i+1:i+5]
            i += 5
        else:
            literal_value += binary[i+1:i+5]
            i += 5
            break
    
    literal_value = binary_to_int( literal_value )
    return binary, i, literal_value


def parse_operator(binary, i, total, operation):
    length_type_id = binary[i]
    subpackets = []
    i += 1

    if length_type_id == '0':
        n_bits = binary_to_int( binary[i:i+15] )
        i += 15

        n_bits += i
        while i < n_bits:
            binary, i, total = parse_packet(binary, i)
            subpackets.append(total)

    else:
        n_packets = binary_to_int( binary[i:i+11] )
        i += 11

        for _ in range(n_packets):
            binary, i, total = parse_packet(binary, i)
            subpackets.append(total)

    value = operation(subpackets)
    return binary, i, value

version_sum = 0
HEX = "420D50000B318100415919B24E72D6509AE67F87195A3CCC518CC01197D538C3E00BC9A349A09802D258CC16FC016100660DC4283200087C6485F1C8C015A00A5A5FB19C363F2FD8CE1B1B99DE81D00C9D3002100B58002AB5400D50038008DA2020A9C00F300248065A4016B4C00810028003D9600CA4C0084007B8400A0002AA6F68440274080331D20C4300004323CC32830200D42A85D1BE4F1C1440072E4630F2CCD624206008CC5B3E3AB00580010E8710862F0803D06E10C65000946442A631EC2EC30926A600D2A583653BE2D98BFE3820975787C600A680252AC9354FFE8CD23BE1E180253548D057002429794BD4759794BD4709AEDAFF0530043003511006E24C4685A00087C428811EE7FD8BBC1805D28C73C93262526CB36AC600DCB9649334A23900AA9257963FEF17D8028200DC608A71B80010A8D50C23E9802B37AA40EA801CD96EDA25B39593BB002A33F72D9AD959802525BCD6D36CC00D580010A86D1761F080311AE32C73500224E3BCD6D0AE5600024F92F654E5F6132B49979802129DC6593401591389CA62A4840101C9064A34499E4A1B180276008CDEFA0D37BE834F6F11B13900923E008CF6611BC65BCB2CB46B3A779D4C998A848DED30F0014288010A8451062B980311C21BC7C20042A2846782A400834916CFA5B8013374F6A33973C532F071000B565F47F15A526273BB129B6D9985680680111C728FD339BDBD8F03980230A6C0119774999A09001093E34600A60052B2B1D7EF60C958EBF7B074D7AF4928CD6BA5A40208E002F935E855AE68EE56F3ED271E6B44460084AB55002572F3289B78600A6647D1E5F6871BE5E598099006512207600BCDCBCFD23CE463678100467680D27BAE920804119DBFA96E05F00431269D255DDA528D83A577285B91BCCB4802AB95A5C9B001299793FCD24C5D600BC652523D82D3FCB56EF737F045008E0FCDC7DAE40B64F7F799F3981F2490"
binary, i, total = parse_packet(hex_to_binary(HEX))

## Part One 
print('Part One:', version_sum)

## Part Two 
print('Part Two:', total)