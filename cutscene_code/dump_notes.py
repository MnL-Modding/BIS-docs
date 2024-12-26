#!/usr/bin/env python3
import itertools

import mnllib


def print_bytes(header: str, data: bytes):
    try:
        decoded_string = data.decode(mnllib.MNL_NOTE_ENCODING).replace('\x00', '\n')
        if decoded_string.strip() == '':
            return
        print(f"----- {header} -----\n{decoded_string}\n")
    except UnicodeDecodeError:
        pass


print("========== FEvent Scripts ==========")
fevent_manager = mnllib.FEventScriptManager()
for room_id, chunk_triple in enumerate(fevent_manager.fevent_chunks):
    for triple_index, chunk in enumerate(chunk_triple):
        if not isinstance(chunk, mnllib.FEventScript):
            continue

        for subroutine_index, subroutine in enumerate(chunk.subroutines):
            print_bytes(f"FEvent room 0x{room_id:04X}, chunk triple index {triple_index}, subroutine {subroutine_index}", subroutine.footer)


print("\n========== Battle Scripts ==========")
battle_manager = mnllib.BattleScriptManager()
for address, scripts in battle_manager.battle_scripts_files.items():
    for script_index, script in enumerate(scripts):
        for subroutine_name, subroutine in itertools.chain(
                [("post table subroutine", script.post_table_subroutine)],
                ((f"subroutine {i}", x) for i, x in enumerate(script.other_subroutines)),
                [("main subroutine", script.main_subroutine)]
        ):
            if subroutine is None:
                continue
            print_bytes(f"Battle script 0x{address | script_index:04X}, {subroutine_name}", subroutine.footer)
