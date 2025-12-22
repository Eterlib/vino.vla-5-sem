#!/usr/bin/env bash
# запускать из корневой директории вашего гит-репозитория

HIM="Лукьянчиков Никита"
BASE_DIR=$(pwd)

find "$BASE_DIR" -type d -name "check" | grep "2025" | while read -r CHECK_DIR; do
    FILE_PATH="$CHECK_DIR/remote"

    # Получаем относительный путь без GNU realpath
    RELATIVE_PATH="${CHECK_DIR#$BASE_DIR/}"
    RELATIVE_PATH="${RELATIVE_PATH%/check}"

    cat << EOF > "$FILE_PATH"
[remote]
"$HIM:$RELATIVE_PATH/1" = []
"$HIM:$RELATIVE_PATH/2" = []
"$HIM:$RELATIVE_PATH/3" = []
EOF

    echo "Файл создан: $FILE_PATH"
done

