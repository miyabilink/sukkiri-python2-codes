def print_monster_name(monster):
    # monsterはディクショナリで受け取る
    # (1)モンスターの名前と属性を取得する
    # (2)取得した属性に対応する記号をELEMENT_SYMBOLSから取得する
    # (3)後述

    # モンスター名を表示する
    print(f'{symbol}{monster.name}{symbol}', end='')