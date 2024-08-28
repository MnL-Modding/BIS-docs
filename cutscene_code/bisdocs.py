import struct
import yaml

PARAM_LENGTH = [1, 2, 4, 1, 2, 4, 2, 4]
PARAM_TYPE = [0, 0, 0, 32, 32, 32, 32, 32]

with open('bis_docs_commands.yml') as file:
    command_docs = yaml.safe_load(file)

with open('overlay6table.bin', 'rb') as overlay:
    # this line is for if you choose to run this script with an extracted and decompressed overlay_0006.bin:
    # overlay.seek(0x014b08)
    for x in range(0x1E5):
        bytes_to_read = overlay.read(16)

        #save x as command ID in big endian hex AND little endian hex
        command_id_big = f'{x:04X}'
        command_id_lil = struct.pack('<H', x).hex(' ')

        #figure out if the command has a return value
        has_return_value = bytes_to_read[0] & 0b10000000 != 0
        if has_return_value: 
            return_value = " YYYY "
        else: 
            return_value = ""

        #figure out how many parameters the command has
        param_num = bytes_to_read[0] & 0b01111111
        
        #write out parameters
        param_list = " "
        for current_param_num in range(param_num):
            param_byte = bytes_to_read[1 + current_param_num // 2]
            if current_param_num % 2 == 0:
                param_id = param_byte & 0b00001111
            else:
                param_id = param_byte >> 4
            param_char = 71 + current_param_num + PARAM_TYPE[param_id]
            param_length_out = PARAM_LENGTH[param_id]
            if current_param_num >= 17:
                param_char_big = 71 + ((current_param_num >> 8) % 17) + PARAM_TYPE[param_id]
                param_char_lil = 71 + (current_param_num % 17) + PARAM_TYPE[param_id]
                if param_char_lil >= param_char_big:
                    param_char_lil += 1
                param_charout = chr(param_char_big) + chr(param_char_lil)
            else:
                param_length_out *= 2
                param_charout = chr(param_char)
            param_list += param_charout * param_length_out + " "

        #prepare completed documentation tidbits
        current_command_doc = command_docs['commands'].get(x, {})

        #print the command and the description
        command_tidbit = current_command_doc.get('name', '???')
        print(command_id_big.upper() + ": " + command_id_lil.upper() + " [XXXXXXXX] " + return_value + param_list + "- " + command_tidbit)
        if current_command_doc.get('description', None) != None:
            print(current_command_doc['description'])
        
        #print the parameters
        for current_param_num in range(param_num):
            param_byte = bytes_to_read[1 + current_param_num // 2]
            if current_param_num % 2 == 0:
                param_id = param_byte & 0b00001111
            else:
                param_id = param_byte >> 4
            param_char = 71 + current_param_num + PARAM_TYPE[param_id]
            param_length_out = PARAM_LENGTH[param_id]
            if current_param_num >= 17:
                param_char_big = 71 + ((current_param_num >> 8) % 17) + PARAM_TYPE[param_id]
                param_char_lil = 71 + (current_param_num % 17) + PARAM_TYPE[param_id]
                if param_char_lil >= param_char_big:
                    param_char_lil += 1
                param_charout = chr(param_char_big) + chr(param_char_lil)
            else:
                param_length_out *= 2
                param_charout = chr(param_char)
            try:
                param_tidbit = current_command_doc['parameters'][current_param_num]
            except (KeyError, IndexError):
                param_tidbit = None
            if param_tidbit is None:
                param_tidbit = '???'
            print("    " + param_charout * param_length_out + ("  " * (4 - PARAM_LENGTH[param_id])) + " - " + param_tidbit)
        
        #line indent (and return value tip)
        return_tidbit = current_command_doc.get('returns', '???')
        if has_return_value:
            print()
            print("    YYYY     - Returns: " + return_tidbit)
        print()
        print()
