def print_monster_name(monster):
    # monsterはディクショナリで受け取る
    # (1)モンスターの名前と属性を取得する
    # (2)取得した属性に対応する記号をELEMENT_SYMBOLSから取得する
    # (3)取得した属性に対応する記号をELEMENT_COLORSから取得する

    # モンスター名を表示する
    print(f'\033[{color}m{symbol}{monster.name}{symbol}\033[0m ', end='')